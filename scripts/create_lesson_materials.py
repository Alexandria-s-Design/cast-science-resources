"""
ModelIt Lesson Materials Generator v3
Creates PowerPoint, Student Activity Pack (Word), and Teacher's Guide (Word)
with AI-generated images via NanoBanana (OpenRouter API).

Output: .pptx for presentations, .docx for documents

Features:
- Blue diagonal geometric corners (TPT branding)
- AI-generated photorealistic images
- 70-80% Black and Brown children representation
- Middle school cool aesthetic
- NGSS standards unpacking
- LEVER methodology
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from docx import Document
from docx.shared import Inches as DocxInches, Pt as DocxPt, RGBColor as DocxRGB
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import requests
import base64
import os
import time

# ============================================
# CONFIGURATION
# ============================================
LESSON_ID = "G05-L01"
LESSON_TITLE = "When Trees Become Matches"
LESSON_SUBTITLE = "California's Burning Season and the Earth Systems That Fuel It"
NGSS_STANDARD = "5-ESS2-1"
GRADE_LEVEL = "5th Grade"
AGE_RANGE = "10-11 years old"

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'materials', 'grade-05', LESSON_ID)
IMAGES_DIR = os.path.join(OUTPUT_DIR, 'images')

# API Configuration
OPENROUTER_API_KEY = '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'

# ============================================
# BRAND COLORS
# ============================================
NAVY = RGBColor(0x0D, 0x1B, 0x2A)
BRAND_BLUE = RGBColor(0x1A, 0x47, 0x80)
MID_BLUE = RGBColor(0x2E, 0x86, 0xAB)
LIGHT_BLUE = RGBColor(0x7E, 0xC8, 0xE3)
SKY_BLUE = RGBColor(0x5D, 0xB7, 0xDE)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_TEXT = RGBColor(0x1A, 0x1A, 0x1A)

# Word colors
DOCX_NAVY = DocxRGB(0x0D, 0x1B, 0x2A)
DOCX_BRAND_BLUE = DocxRGB(0x1A, 0x47, 0x80)
DOCX_MID_BLUE = DocxRGB(0x2E, 0x86, 0xAB)

# Cost tracking
total_image_cost = 0.0

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)


# ============================================
# IMAGE GENERATION (NanoBanana via OpenRouter)
# ============================================

def generate_image(scene_description, filename, setting="modern classroom"):
    """
    Generate a photorealistic educational image using NanoBanana.
    Uses the approved prompt template for diversity and style.
    """
    global total_image_cost

    prompt = f'''Create a photorealistic, cinematic, ultra-crisp image of {scene_description} in {setting} featuring a diverse, multicultural group with Black people centered (a mix of skin tones and ethnicities represented), age-accurate for {AGE_RANGE} (no one looks like an adult if they're a kid).

Style: modern education / future-ready / "middle school coolness"—confident, aspirational, realistic.

Composition: clean framing, strong focal subject, natural body proportions, believable clothing textures, realistic hair detail (coils, curls, locs, braids), subtle emotion and authentic interaction.

Camera/lighting: soft natural window light + gentle fill, shallow depth of field, 35mm/50mm look, high dynamic range, sharp eyes, realistic skin texture.

Quality: high-resolution, crisp edges, minimal noise, professional editorial photo.

If tech overlays appear: keep them subtle, readable, and physically plausible (not cluttered), with realistic reflections and occlusion.'''

    print(f"  Generating: {filename}...")

    try:
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {OPENROUTER_API_KEY}',
                'Content-Type': 'application/json',
            },
            json={
                'model': 'google/gemini-2.5-flash-image',
                'messages': [{'role': 'user', 'content': prompt}],
                'modalities': ['image', 'text']
            },
            timeout=180
        )

        if response.status_code == 200:
            data = response.json()
            choices = data.get('choices', [])

            if choices:
                message = choices[0].get('message', {})
                images = message.get('images', [])

                if images:
                    img = images[0]
                    if isinstance(img, dict):
                        img_url = img.get('image_url', {}).get('url', '')
                        if img_url.startswith('data:image'):
                            base64_data = img_url.split(',')[1]
                            filepath = os.path.join(IMAGES_DIR, filename)
                            with open(filepath, 'wb') as f:
                                f.write(base64.b64decode(base64_data))

                            # Track cost
                            usage = data.get('usage', {})
                            cost = usage.get('cost', 0)
                            total_image_cost += cost
                            print(f"    [OK] Saved: {filename} (${cost:.4f})")
                            return filepath

            print(f"    [!] No image in response for {filename}")
            return None
        else:
            print(f"    [X] Error {response.status_code}: {response.text[:200]}")
            return None

    except Exception as e:
        print(f"    [X] Exception: {e}")
        return None


def generate_all_lesson_images():
    """Generate all images needed for the lesson materials."""
    print("\n" + "=" * 60)
    print("GENERATING LESSON IMAGES")
    print("=" * 60)

    images = {}

    # Image 1: Cover - Students collaborating on wildfire project
    images['cover'] = generate_image(
        "5th grade students collaborating on a science modeling project about California wildfires, gathered around a laptop showing a diagram, one student confidently pointing at the screen while others lean in engaged",
        "cover-students-collaborating.png",
        "modern classroom with natural lighting"
    )
    time.sleep(2)  # Rate limiting

    # Image 2: California landscape - fire season
    images['landscape'] = generate_image(
        "California golden hillside during fire season with dry grass and scattered oak trees, warm sunset lighting, a diverse suburban community visible in the distance, educational documentary style",
        "california-fire-season.png",
        "outdoor California landscape"
    )
    time.sleep(2)

    # Image 3: Students discussing/comparing
    images['discussion'] = generate_image(
        "a small group of 5th grade students having an animated science discussion, some pointing at a shared screen, others taking notes, showing genuine curiosity and engagement, one student explaining to others",
        "students-discussion.png",
        "bright modern classroom or maker space"
    )
    time.sleep(2)

    # Image 4: Student working on model
    images['modeling'] = generate_image(
        "a focused 5th grade student working on a laptop showing a simple diagram with connected nodes and arrows, the student looks confident and engaged, other students visible in background collaborating",
        "student-modeling.png",
        "modern classroom with Chromebooks"
    )
    time.sleep(2)

    # Image 5: STEM Challenge - engineering design
    images['stem'] = generate_image(
        "5th grade students working together on an engineering design challenge, sketching on paper and discussing ideas, looking like young engineers solving a real problem, hands-on collaborative work",
        "stem-challenge.png",
        "classroom maker space with materials"
    )

    print(f"\nTotal images generated: {len([v for v in images.values() if v])}")
    print(f"Total image cost: ${total_image_cost:.4f}")

    return images


# ============================================
# POWERPOINT FUNCTIONS
# ============================================

def add_diagonal_corners(slide, prs, position='both'):
    """Add the signature blue diagonal corner design"""
    if position in ['top', 'both']:
        shape1 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE,
            Inches(-0.5), Inches(-0.5), Inches(4), Inches(1.5))
        shape1.fill.solid()
        shape1.fill.fore_color.rgb = NAVY
        shape1.line.fill.background()

        shape2 = slide.shapes.add_shape(MSO_SHAPE.PARALLELOGRAM,
            Inches(2.5), Inches(0), Inches(3), Inches(0.8))
        shape2.fill.solid()
        shape2.fill.fore_color.rgb = MID_BLUE
        shape2.line.fill.background()

        shape3 = slide.shapes.add_shape(MSO_SHAPE.PARALLELOGRAM,
            Inches(3.5), Inches(0.5), Inches(2.5), Inches(0.4))
        shape3.fill.solid()
        shape3.fill.fore_color.rgb = LIGHT_BLUE
        shape3.line.fill.background()

    if position in ['bottom', 'both']:
        shape4 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE,
            Inches(6.5), Inches(6), Inches(4), Inches(1.5))
        shape4.fill.solid()
        shape4.fill.fore_color.rgb = NAVY
        shape4.line.fill.background()
        shape4.rotation = 180

        shape5 = slide.shapes.add_shape(MSO_SHAPE.PARALLELOGRAM,
            Inches(4.5), Inches(6.7), Inches(3), Inches(0.8))
        shape5.fill.solid()
        shape5.fill.fore_color.rgb = MID_BLUE
        shape5.line.fill.background()

        shape6 = slide.shapes.add_shape(MSO_SHAPE.PARALLELOGRAM,
            Inches(4), Inches(6.3), Inches(2.5), Inches(0.4))
        shape6.fill.solid()
        shape6.fill.fore_color.rgb = LIGHT_BLUE
        shape6.line.fill.background()


def add_modelit_logo(slide, x, y, width=3):
    """Add ModelIt! logo box"""
    logo_bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(y), Inches(width), Inches(0.9))
    logo_bg.fill.solid()
    logo_bg.fill.fore_color.rgb = SKY_BLUE
    logo_bg.line.fill.background()

    icon = slide.shapes.add_shape(MSO_SHAPE.OVAL,
        Inches(x + 0.15), Inches(y + 0.25), Inches(0.4), Inches(0.4))
    icon.fill.solid()
    icon.fill.fore_color.rgb = WHITE
    icon.line.fill.background()

    text_box = slide.shapes.add_textbox(
        Inches(x + 0.6), Inches(y + 0.15), Inches(width - 0.8), Inches(0.6))
    tf = text_box.text_frame
    p = tf.paragraphs[0]
    p.text = "ModelIt!"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.font.name = "Comic Sans MS"


def add_image_to_slide(slide, image_path, x, y, width, height):
    """Add an image to a slide, with fallback placeholder if image doesn't exist."""
    if image_path and os.path.exists(image_path):
        slide.shapes.add_picture(image_path, Inches(x), Inches(y), Inches(width), Inches(height))
        return True
    else:
        # Fallback placeholder
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(0xF0, 0xF5, 0xFA)
        box.line.color.rgb = MID_BLUE
        box.line.width = Pt(2)
        return False


def create_powerpoint(images):
    """Create the student presentation PowerPoint with real images."""
    output_path = os.path.join(OUTPUT_DIR, f'{LESSON_ID}-Student-Presentation.pptx')
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # SLIDE 1: Cover
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs)
    add_modelit_logo(slide, 3.5, 1.5)

    # Add cover image
    if images.get('cover'):
        add_image_to_slide(slide, images['cover'], 0.5, 4.8, 3.5, 2.3)

    header = slide.shapes.add_textbox(Inches(1), Inches(2.8), Inches(8), Inches(0.6))
    tf = header.text_frame
    p = tf.paragraphs[0]
    p.text = "Student Lesson"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    title = slide.shapes.add_textbox(Inches(0.5), Inches(3.3), Inches(9), Inches(1.2))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = LESSON_TITLE
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE
    p.alignment = PP_ALIGN.CENTER

    sub = tf.add_paragraph()
    sub.text = LESSON_SUBTITLE
    sub.font.size = Pt(16)
    sub.font.italic = True
    sub.font.color.rgb = DARK_TEXT
    sub.alignment = PP_ALIGN.CENTER

    # SLIDE 2: The Question
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "The Big Question"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    question = slide.shapes.add_textbox(Inches(1), Inches(2.3), Inches(8), Inches(1))
    tf = question.text_frame
    p = tf.paragraphs[0]
    p.text = "Why does California burn at the same time every year?"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE
    p.alignment = PP_ALIGN.CENTER

    # Add landscape image
    if images.get('landscape'):
        add_image_to_slide(slide, images['landscape'], 1.5, 3.5, 7, 3.5)

    # SLIDE 3: What We'll Build
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Today We Will Build a Model!"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    content = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(5), Inches(4))
    tf = content.text_frame
    tf.word_wrap = True

    items = [
        "Identify the COMPONENTS (parts) of the California fire system",
        "Connect them with RELATIONSHIPS (how they affect each other)",
        "Run SIMULATIONS to see what happens during drought",
        "Make PREDICTIONS about fire conditions"
    ]
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"{i+1}. {item}"
        p.font.size = Pt(18)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(14)

    # Add modeling image
    if images.get('modeling'):
        add_image_to_slide(slide, images['modeling'], 5.8, 2.5, 3.8, 3.2)

    # SLIDE 4: Activity 1 - Sort Components
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Activity 1: Sort the Components"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    content = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(4.5), Inches(3.5))
    tf = content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Your components:"
    p.font.size = Pt(20)
    p.font.bold = True

    components = ["Rainfall", "Dry Vegetation", "Wind", "Fire Spread"]
    for comp in components:
        p = tf.add_paragraph()
        p.text = f"   * {comp}"
        p.font.size = Pt(18)

    p = tf.add_paragraph()
    p.text = "\nSort them into INTERNAL and EXTERNAL!"
    p.font.size = Pt(16)
    p.font.italic = True
    p.font.color.rgb = BRAND_BLUE

    # Platform screenshot placeholder (team will add)
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(5.5), Inches(2.2), Inches(4), Inches(3.5))
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xF0, 0xF5, 0xFA)
    box.line.color.rgb = MID_BLUE

    text_box = slide.shapes.add_textbox(Inches(5.7), Inches(3.5), Inches(3.6), Inches(1))
    tf = text_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "[ModelIt Platform Screenshot - Sorting Activity]"
    p.font.size = Pt(11)
    p.font.italic = True
    p.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p.alignment = PP_ALIGN.CENTER

    # SLIDE 5: Activity 2 - Connect
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Activity 2: Connect with Arrows"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    content = slide.shapes.add_textbox(Inches(0.5), Inches(2.2), Inches(9), Inches(2))
    tf = content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Draw arrows to show HOW components affect each other:"
    p.font.size = Pt(20)

    p = tf.add_paragraph()
    p.text = "(+) POSITIVE: When one goes UP, the other goes UP"
    p.font.size = Pt(18)
    p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "(-) NEGATIVE: When one goes UP, the other goes DOWN"
    p.font.size = Pt(18)
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "\nThink: When RAINFALL goes UP, does DRY VEGETATION go UP or DOWN?"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE

    # Add discussion image
    if images.get('discussion'):
        add_image_to_slide(slide, images['discussion'], 2.5, 4.8, 5, 2.5)

    # SLIDE 6: Activity 3 - Simulate
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Activity 3: Run the Simulation!"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    content = slide.shapes.add_textbox(Inches(0.5), Inches(2.2), Inches(4.5), Inches(4))
    tf = content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Test these scenarios:"
    p.font.size = Pt(20)
    p.font.bold = True

    scenarios = [
        "1. Drought: Turn RAINFALL OFF",
        "2. Windy Day: Turn WIND ON",
        "3. Fire Season: Both conditions!"
    ]
    for s in scenarios:
        p = tf.add_paragraph()
        p.text = s
        p.font.size = Pt(18)
        p.space_before = Pt(10)

    p = tf.add_paragraph()
    p.text = "\nWatch the graphs change!"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE

    # Platform screenshot placeholder
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(5.2), Inches(2.2), Inches(4.3), Inches(4))
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xF0, 0xF5, 0xFA)
    box.line.color.rgb = MID_BLUE

    text_box = slide.shapes.add_textbox(Inches(5.4), Inches(3.8), Inches(3.9), Inches(1))
    tf = text_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "[ModelIt Platform Screenshot - Simulation Results]"
    p.font.size = Pt(11)
    p.font.italic = True
    p.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p.alignment = PP_ALIGN.CENTER

    # SLIDE 7: Discussion
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "What Did We Discover?"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    content = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(5.5), Inches(4.5))
    tf = content.text_frame
    tf.word_wrap = True

    discoveries = [
        "California's dry season = more fire risk",
        "Drought makes vegetation into FUEL",
        "Wind helps fire SPREAD faster",
        "These Earth systems work TOGETHER"
    ]
    for i, d in enumerate(discoveries):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"* {d}"
        p.font.size = Pt(22)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(14)

    # Add cover image again for discussion
    if images.get('cover'):
        add_image_to_slide(slide, images['cover'], 6.2, 3, 3.3, 2.8)

    # SLIDE 8: STEM Challenge Preview
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs, 'top')

    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "STEM Challenge: Firebreak Engineers!"
    p.font.size = Pt(34)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    content = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(5), Inches(4))
    tf = content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Your Mission:"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE

    p = tf.add_paragraph()
    p.text = "Design firebreaks to protect Willow Creek from wildfire!"
    p.font.size = Pt(18)
    p.space_before = Pt(10)

    p = tf.add_paragraph()
    p.text = "\nYou learned: Removing DRY VEGETATION breaks the fire chain."
    p.font.size = Pt(16)
    p.space_before = Pt(10)

    p = tf.add_paragraph()
    p.text = "\nNow apply it like real engineers!"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE

    # Add STEM image
    if images.get('stem'):
        add_image_to_slide(slide, images['stem'], 5.5, 2.5, 4, 3.5)

    prs.save(output_path)
    print(f"[OK] Created: {output_path}")
    return output_path


# ============================================
# WORD DOCUMENT HELPERS
# ============================================

def set_cell_shading(cell, color_hex):
    """Set background color of a table cell"""
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color_hex)
    cell._tc.get_or_add_tcPr().append(shading)


def add_name_date_line(doc):
    """Add Name/Date line to page"""
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    row = table.rows[0]
    row.cells[0].text = "Name: _______________________________"
    row.cells[1].text = "Date: _______________"
    for cell in row.cells:
        cell.paragraphs[0].runs[0].font.size = DocxPt(11)
    doc.add_paragraph()


# ============================================
# STUDENT ACTIVITY PACK (WORD)
# ============================================

def create_student_activity_pack():
    """Create the student activity pack as Word document"""
    output_path = os.path.join(OUTPUT_DIR, f'{LESSON_ID}-Student-Activity-Pack.docx')
    doc = Document()

    # Set margins
    for section in doc.sections:
        section.top_margin = DocxInches(0.75)
        section.bottom_margin = DocxInches(0.75)
        section.left_margin = DocxInches(0.75)
        section.right_margin = DocxInches(0.75)

    # ========== COVER PAGE ==========
    doc.add_paragraph()
    doc.add_paragraph()

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("ModelIt!")
    run.bold = True
    run.font.size = DocxPt(48)
    run.font.color.rgb = DOCX_NAVY

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Student Activity Pack")
    run.font.size = DocxPt(28)
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph()

    lesson_title = doc.add_paragraph()
    lesson_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = lesson_title.add_run(LESSON_TITLE)
    run.bold = True
    run.font.size = DocxPt(32)
    run.font.color.rgb = DOCX_NAVY

    lesson_sub = doc.add_paragraph()
    lesson_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = lesson_sub.add_run(LESSON_SUBTITLE)
    run.italic = True
    run.font.size = DocxPt(16)

    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()

    # Name/Date on cover
    add_name_date_line(doc)

    info = doc.add_paragraph()
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = info.add_run(f"Grade Level: {GRADE_LEVEL}  |  Standard: {NGSS_STANDARD}")
    run.font.size = DocxPt(12)

    doc.add_page_break()

    # ========== TABLE OF CONTENTS ==========
    toc_title = doc.add_paragraph()
    run = toc_title.add_run("What's Inside")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    toc_items = [
        ("1. Scoring Rubric", "How your work will be assessed"),
        ("2. Model Recording Page", "Sketch your model"),
        ("3. Simulation Observations", "Record what happens"),
        ("4. Research & Extend", "Add new components"),
        ("5. STEM Challenge", "Firebreak Engineers!"),
    ]

    for item, desc in toc_items:
        p = doc.add_paragraph()
        run = p.add_run(item)
        run.bold = True
        run.font.size = DocxPt(14)
        p.add_run(f"  -  {desc}").font.size = DocxPt(12)

    doc.add_page_break()

    # ========== SCORING RUBRIC ==========
    rubric_title = doc.add_paragraph()
    run = rubric_title.add_run("Scoring Rubric")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    rubric_intro = doc.add_paragraph()
    rubric_intro.add_run("This rubric shows how your modeling work will be assessed.").font.size = DocxPt(11)

    doc.add_paragraph()

    rubric_data = [
        ["Skill", "4 - Expert", "3 - Proficient", "2 - Developing", "1 - Beginning"],
        ["Components", "All correct", "Most correct", "Some correct", "Needs help"],
        ["Relationships", "All arrows correct", "Most correct", "Some correct", "Needs help"],
        ["Simulation", "Multiple scenarios", "Runs scenarios", "With guidance", "Needs help"],
        ["Explanation", "Clear with evidence", "Explains well", "Partial", "Needs help"],
    ]

    table = doc.add_table(rows=len(rubric_data), cols=5)
    table.style = 'Table Grid'

    for i, row_data in enumerate(rubric_data):
        for j, cell_text in enumerate(row_data):
            cell = table.rows[i].cells[j]
            cell.text = cell_text
            cell.paragraphs[0].runs[0].font.size = DocxPt(9)
            if i == 0:
                cell.paragraphs[0].runs[0].bold = True
                set_cell_shading(cell, "1A4780")
                cell.paragraphs[0].runs[0].font.color.rgb = DocxRGB(0xFF, 0xFF, 0xFF)

    doc.add_page_break()

    # ========== MODEL RECORDING PAGE ==========
    model_title = doc.add_paragraph()
    run = model_title.add_run("Model Recording Page")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    doc.add_paragraph("Sketch your model before or after building it in ModelIt!")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("My Components:")
    run.bold = True

    comp_table = doc.add_table(rows=2, cols=2)
    comp_table.style = 'Table Grid'
    labels = ["EXTERNAL (inputs):", "INTERNAL (inside system):"]
    for i, cell in enumerate(comp_table.rows[0].cells):
        cell.text = labels[i]
        cell.paragraphs[0].runs[0].bold = True
    for cell in comp_table.rows[1].cells:
        cell.text = "\n\n\n"

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("My Model Sketch:")
    run.bold = True

    sketch_table = doc.add_table(rows=1, cols=1)
    sketch_table.style = 'Table Grid'
    sketch_table.rows[0].cells[0].text = "\n\n\n\n\n\n\n\n\n\n"

    doc.add_paragraph()
    doc.add_paragraph("Key: (+) = both go UP together  |  (-) = one UP, other DOWN")

    doc.add_page_break()

    # ========== SIMULATION OBSERVATIONS ==========
    sim_title = doc.add_paragraph()
    run = sim_title.add_run("Simulation Observations")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    scenarios = [
        ("Scenario 1: DROUGHT", "Turn RAINFALL OFF"),
        ("Scenario 2: WINDY DAY", "Turn WIND ON"),
        ("Scenario 3: FIRE SEASON", "RAINFALL OFF + WIND ON"),
    ]

    for title, instruction in scenarios:
        p = doc.add_paragraph()
        run = p.add_run(title)
        run.bold = True
        run.font.color.rgb = DOCX_BRAND_BLUE

        doc.add_paragraph(instruction)
        doc.add_paragraph("What happened?")

        response_table = doc.add_table(rows=1, cols=1)
        response_table.style = 'Table Grid'
        response_table.rows[0].cells[0].text = "\n\n"
        doc.add_paragraph()

    doc.add_page_break()

    # ========== RESEARCH & EXTEND ==========
    research_title = doc.add_paragraph()
    run = research_title.add_run("Research & Extend")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    doc.add_paragraph("Find ONE new component that affects California wildfires:")

    examples = ["Temperature", "Humidity", "Mountain slopes", "Santa Ana winds", "Human activity"]
    for ex in examples:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(ex)

    doc.add_paragraph()
    doc.add_paragraph("My new component: ________________________________")
    doc.add_paragraph("How does it connect? Draw and explain:")

    sketch = doc.add_table(rows=1, cols=1)
    sketch.style = 'Table Grid'
    sketch.rows[0].cells[0].text = "\n\n\n\n"

    doc.add_page_break()

    # ========== STEM CHALLENGE ==========
    stem_title = doc.add_paragraph()
    run = stem_title.add_run("STEM CHALLENGE: Firebreak Engineers")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    p = doc.add_paragraph()
    run = p.add_run("YOUR MISSION")
    run.bold = True
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph("You learned that DRY VEGETATION is the FUEL for fire spread. Real engineers use FIREBREAKS - areas with no fuel - to stop fires!")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("THE CHALLENGE:")
    run.bold = True

    doc.add_paragraph("Design firebreaks to protect Willow Creek. You have budget for only 3 firebreaks. Where will you put them?")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("THINK LIKE AN ENGINEER:")
    run.bold = True

    questions = [
        "Which direction does fire spread fastest? (Wind!)",
        "Should firebreaks be uphill or downhill from town?",
        "How does this connect to your model?"
    ]
    for q in questions:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(q)

    doc.add_paragraph()
    doc.add_paragraph("Draw your design (town center, forest around, wind arrows, 3 firebreaks):")

    design_box = doc.add_table(rows=1, cols=1)
    design_box.style = 'Table Grid'
    design_box.rows[0].cells[0].text = "\n\n\n\n\n\n\n\n\n\n"

    doc.add_paragraph()
    doc.add_paragraph("Explain your design:")
    explain_box = doc.add_table(rows=1, cols=1)
    explain_box.style = 'Table Grid'
    explain_box.rows[0].cells[0].text = "\n\n\n"

    doc.save(output_path)
    print(f"[OK] Created: {output_path}")
    return output_path


# ============================================
# TEACHER'S GUIDE (WORD)
# ============================================

def create_teachers_guide():
    """Create the teacher's guide as Word document"""
    output_path = os.path.join(OUTPUT_DIR, f'{LESSON_ID}-Teachers-Guide.docx')
    doc = Document()

    for section in doc.sections:
        section.top_margin = DocxInches(0.75)
        section.bottom_margin = DocxInches(0.75)
        section.left_margin = DocxInches(0.75)
        section.right_margin = DocxInches(0.75)

    # ========== COVER ==========
    doc.add_paragraph()
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("ModelIt! Teacher's Guide")
    run.bold = True
    run.font.size = DocxPt(36)
    run.font.color.rgb = DOCX_NAVY

    doc.add_paragraph()
    lesson = doc.add_paragraph()
    lesson.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = lesson.add_run(f"{LESSON_ID}: {LESSON_TITLE}")
    run.bold = True
    run.font.size = DocxPt(24)

    doc.add_paragraph()

    # Quick reference table
    quick_ref = [
        ["Grade Level", GRADE_LEVEL],
        ["NGSS Standard", NGSS_STANDARD],
        ["Time", "40-45 minutes"],
        ["Materials", "Student devices, Activity Pack"],
        ["Prep Required", "None"],
    ]

    table = doc.add_table(rows=len(quick_ref), cols=2)
    table.style = 'Table Grid'
    for i, (label, value) in enumerate(quick_ref):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[0].paragraphs[0].runs[0].bold = True
        set_cell_shading(table.rows[i].cells[0], "7EC8E3")
        table.rows[i].cells[1].text = value

    doc.add_page_break()

    # ========== NGSS UNPACKING ==========
    standards_title = doc.add_paragraph()
    run = standards_title.add_run("NGSS Standards Unpacking")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    p = doc.add_paragraph()
    run = p.add_run("Performance Expectation: 5-ESS2-1")
    run.bold = True
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph("Develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and/or atmosphere interact.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("How This Lesson Addresses the Standard:")
    run.bold = True

    connections = [
        ("Geosphere", "California terrain affects fire spread"),
        ("Biosphere", "Vegetation serves as fuel"),
        ("Hydrosphere", "Rainfall determines dryness"),
        ("Atmosphere", "Wind drives fire behavior"),
    ]

    for sphere, connection in connections:
        p = doc.add_paragraph()
        run = p.add_run(f"{sphere}: ")
        run.bold = True
        p.add_run(connection)

    doc.add_page_break()

    # ========== LEVER FRAMEWORK ==========
    lever_title = doc.add_paragraph()
    run = lever_title.add_run("The LEVER Framework")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    doc.add_paragraph("LEVER guides students through authentic scientific modeling:")

    lever_phases = [
        ("L - LOCATE", "Identify system components"),
        ("E - ESTABLISH", "Determine relationships (+/-)"),
        ("V - VISUALIZE", "Build the model"),
        ("E - EVALUATE", "Run simulations, analyze"),
        ("R - REVISE", "Improve based on evidence"),
    ]

    for phase, desc in lever_phases:
        p = doc.add_paragraph()
        run = p.add_run(phase + ": ")
        run.bold = True
        run.font.color.rgb = DOCX_BRAND_BLUE
        p.add_run(desc)

    doc.add_page_break()

    # ========== ANSWER KEY ==========
    answer_title = doc.add_paragraph()
    run = answer_title.add_run("Answer Key")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    p = doc.add_paragraph()
    run = p.add_run("Component Sorting:")
    run.bold = True
    doc.add_paragraph("EXTERNAL: Rainfall, Wind")
    doc.add_paragraph("INTERNAL: Dry Vegetation, Fire Spread")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Relationships:")
    run.bold = True
    doc.add_paragraph("Rainfall --> Dry Vegetation = NEGATIVE")
    doc.add_paragraph("Dry Vegetation --> Fire Spread = POSITIVE")
    doc.add_paragraph("Wind --> Fire Spread = POSITIVE")

    doc.add_page_break()

    # ========== STEM CHALLENGE GUIDANCE ==========
    stem_title = doc.add_paragraph()
    run = stem_title.add_run("STEM Challenge: Teacher Guidance")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    p = doc.add_paragraph()
    run = p.add_run("How to Introduce:")
    run.bold = True
    run.font.color.rgb = DOCX_BRAND_BLUE

    intro = '''Say: "You discovered that DRY VEGETATION is the FUEL for fire spread. Real engineers create FIREBREAKS - areas where they remove vegetation so fire has nothing to burn. Now YOU will become Firebreak Engineers!"'''
    doc.add_paragraph(intro)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Key Concepts:")
    run.bold = True

    concepts = [
        "Wind direction matters (Santa Ana winds from east)",
        "Fire spreads uphill faster",
        "Firebreaks go BETWEEN fire source and what you protect",
    ]
    for c in concepts:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(c)

    doc.save(output_path)
    print(f"[OK] Created: {output_path}")
    return output_path


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    ensure_output_dir()

    print("\n" + "=" * 60)
    print("ModelIt! Lesson Materials Generator v3")
    print(f"{LESSON_ID}: {LESSON_TITLE}")
    print("With AI Image Generation (NanoBanana)")
    print("=" * 60)

    # Generate images
    images = generate_all_lesson_images()

    print("\n" + "=" * 60)
    print("CREATING MATERIALS")
    print("=" * 60 + "\n")

    # Create materials
    ppt_path = create_powerpoint(images)
    activity_path = create_student_activity_pack()
    guide_path = create_teachers_guide()

    print("\n" + "=" * 60)
    print("COMPLETE!")
    print("=" * 60)
    print(f"\nLocation: {OUTPUT_DIR}")
    print(f"\nFiles created:")
    print(f"  - {LESSON_ID}-Student-Presentation.pptx")
    print(f"  - {LESSON_ID}-Student-Activity-Pack.docx")
    print(f"  - {LESSON_ID}-Teachers-Guide.docx")
    print(f"\nImages generated: {len([v for v in images.values() if v])}")
    print(f"Total image cost: ${total_image_cost:.4f}")
    print("=" * 60)
