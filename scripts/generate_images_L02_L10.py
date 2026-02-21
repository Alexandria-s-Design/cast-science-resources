#!/usr/bin/env python3
"""Generate images for G05-L02 through G05-L10 using OpenRouter API"""
import os, time, base64, requests
from lesson_data_L02_L10 import ALL_LESSONS

API_KEY = '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'
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'materials', 'grade-05')
total_cost = 0.0

def gen_img(scene, fn, img_dir):
    global total_cost
    prompt = (f"Create a photorealistic, cinematic, ultra-crisp image of {scene} "
              "featuring a diverse, multicultural group with Black people centered "
              "(a mix of skin tones and ethnicities represented), age-accurate for "
              "10-11 years old (no one looks like an adult if they're a kid). "
              "Style: modern education / future-ready / middle school coolness, "
              "confident, aspirational, realistic. Composition: clean framing, "
              "natural body proportions, realistic hair detail (coils, curls, locs, braids). "
              "Camera/lighting: soft natural window light, shallow depth of field, "
              "35mm/50mm look. Quality: high-resolution, professional editorial photo.")
    print(f"  Generating: {fn}...")
    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={"model": "google/gemini-2.5-flash-image",
                  "messages": [{"role": "user", "content": prompt}],
                  "modalities": ["image", "text"]},
            timeout=180)
        if r.status_code == 200:
            data = r.json()
            imgs = data.get("choices", [{}])[0].get("message", {}).get("images", [])
            if imgs:
                img = imgs[0]
                url = img.get("image_url", {}).get("url", "") if isinstance(img, dict) else ""
                if url.startswith("data:image"):
                    fp = os.path.join(img_dir, fn)
                    with open(fp, "wb") as f:
                        f.write(base64.b64decode(url.split(",")[1]))
                    total_cost += data.get("usage", {}).get("cost", 0)
                    print(f"    [OK] {fn}")
                    return fp
            print(f"    [!] No image in response")
            return None
        else:
            print(f"    [X] {r.status_code}: {r.text[:200]}")
            return None
    except Exception as e:
        print(f"    [X] {e}")
        return None

def gen_all_imgs(c, img_dir):
    os.makedirs(img_dir, exist_ok=True)
    imgs = {}
    for key, (fn, scene) in c["images"].items():
        fp = os.path.join(img_dir, fn)
        if os.path.exists(fp):
            print(f"    [SKIP] {fn}")
            imgs[key] = fp
        else:
            imgs[key] = gen_img(scene, fn, img_dir)
            time.sleep(3)  # Rate limiting
    return imgs

if __name__ == "__main__":
    print("="*60)
    print("Image Generator - G05-L02 through G05-L10")
    print("Using OpenRouter API")
    print("="*60)
    print(f"\nGenerating images for {len(ALL_LESSONS)} lessons:")
    for lesson in ALL_LESSONS:
        print(f"  - {lesson['id']}: {lesson['title']}")
    print()

    start_time = time.time()
    total_images = 0

    for i, lesson in enumerate(ALL_LESSONS, 1):
        lid = lesson['id']
        img_dir = os.path.join(BASE_DIR, lid, 'images')
        print(f"\n[{i}/{len(ALL_LESSONS)}] Processing {lid}...")
        gen_all_imgs(lesson, img_dir)
        total_images += len(lesson['images'])

    elapsed = time.time() - start_time
    print("\n" + "="*60)
    print("IMAGE GENERATION COMPLETE!")
    print("="*60)
    print(f"Lessons processed: {len(ALL_LESSONS)}")
    print(f"Images attempted: {total_images}")
    print(f"Total time: {elapsed/60:.1f} minutes")
    print(f"Estimated cost: ${total_cost:.2f}")
    print("="*60)
