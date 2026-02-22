# ModelIt! CAST Science Resources — Session Protocols

## Use this document to continue working in a new Claude Code / PowerShell session.

---

## 1. PROJECT OVERVIEW

**Project:** CAST/ModelIt! Science Curriculum Materials
**Repository:** `cast-science-resources` (GitHub fork: `alexandriasworld1234-source/cast-science-resources`)
**Working Directory:** `C:\Users\ginja\cast-science-resources`
**Status:** Grade 5 complete (10 lessons), Grade 6 complete (10 lessons), Grade 8 complete (10 lessons)

---

## 2. STANDING REQUIREMENT — THREE MATERIALS PER LESSON

**WHENEVER creating ModelIt lessons, ALL THREE materials must ALWAYS be generated — no exceptions:**

1. **Student Presentation** (.pptx) — 9 slides, branded with CAST/ModelIt brand colors
2. **Student Activity Pack** (.docx) — 8 sections: Pre-Assessment, Rubric, Component Analysis, Model Sketch, Simulation Observations, Research & Extend, Reflection, STEM Challenge
3. **Teacher's Guide** (.docx) — 8 sections: NGSS Unpacking, CAST Alignment, Background Content, LEVER Framework, Slide-by-Slide Facilitation, Answer Key, STEM Guidance, Differentiation, Misconceptions

**Exemplar:** G05-L01 "When Trees Become Matches" — use as the gold standard for branding, structure, depth, and detail.

---

## 3. BRAND COLORS (PPT & DOCX)

```python
# PowerPoint (pptx.dml.color.RGBColor)
NAVY      = RGBColor(0x0D, 0x1B, 0x2A)   # Primary dark
BRAND_BLUE = RGBColor(0x1A, 0x47, 0x80)  # Headings, buttons
MID_BLUE   = RGBColor(0x2E, 0x86, 0xAB)  # Accents, shapes
LIGHT_BLUE = RGBColor(0x7E, 0xC8, 0xE3)  # Table headers, highlights
SKY_BLUE   = RGBColor(0x5D, 0xB7, 0xDE)  # ModelIt! logo background
ACCENT_ORANGE = RGBColor(0xE6, 0x7E, 0x22) # STEM / engineering highlights
DARK       = RGBColor(0x1A, 0x1A, 0x2E)  # Body text
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)

# Word Documents (docx.shared.RGBColor)
# Same hex values but imported from docx.shared
```

---

## 4. PPT SLIDE STRUCTURE (9 Slides)

| Slide | Title | Key Elements |
|-------|-------|-------------|
| 1 | Cover | ModelIt! logo centered, "Student Lesson" header, title (38pt), subtitle (15pt italic), NGSS badge (right), cover image (bottom-left), diagonal corner shapes |
| 2 | Learning Objectives | "What You Will Learn Today" (34pt), left column: Learning Goals (16pt bullets), right column: Key Vocabulary (bold term + italic definition) |
| 3 | Big Question | "The Big Question" (34pt), question (26pt bold), context paragraph, landscape image (right) |
| 4 | LEVER Framework | "Today We Will Build a Model!" (34pt), intro text, numbered LEVER steps (1-5), modeling image (right) |
| 5 | Activity 1: Sort | "Sort the Components" (34pt), instructions, component list, think-pair-share prompt, discussion image (right) |
| 6 | Activity 2: Connect | "Connect with Arrows" (34pt), (+) positive and (-) negative definitions, "Think About It" question, image (right) |
| 7 | Activity 3: Simulate | "Run the Simulation!" (34pt), scenarios list, ModelIt platform placeholder box (right) |
| 8 | Discoveries | "What Did We Discover?" (34pt), bullet findings, answer box, cover image reuse (right) |
| 9 | STEM Challenge | "STEM Challenge: [Title]" (32pt), mission, challenge scenario, "Think Like an Engineer" questions, image (right), career connection bar (navy bg, orange label) |

**PPT Dimensions:** 10" wide × 7.5" tall, blank layout #6

---

## 5. LESSON DATA STRUCTURE (46 fields per lesson)

Each lesson dictionary requires these fields:

```python
{
    "id": "G08-L01",                    # Grade-Lesson ID
    "title": "Lesson Title",            # Display title
    "subtitle": "Engaging Subtitle",    # Descriptive tagline
    "ngss": "MS-LS4-4, MS-LS4-6",     # NGSS Performance Expectations
    "ngss_desc": "Full PE text...",     # Full NGSS description
    "big_question": "Driving question?", # Phenomenon question
    "objectives": [...],                # 4 learning objectives
    "vocabulary": [("Term", "Def"),...], # 4 vocabulary pairs
    "components": [("Name", "Desc", True/False),...],  # 4 components (True=external)
    "think_about_it": "...",            # Think-pair-share prompt
    "scenarios": [("Name", "Instructions"),...],  # 3 simulation scenarios
    "sim_scenarios": [("Name", "Settings", "Prediction prompt"),...],  # 3 detailed scenarios
    "discoveries": [...],               # 4 key findings
    "answer": "...",                    # Answer to the Big Question
    "stem_title": "...",               # STEM challenge title
    "stem_mission": "...",             # Engineering mission statement
    "stem_scenario": "...",            # Challenge scenario
    "stem_questions": [...],           # 3 guiding questions
    "stem_design_qs": [...],           # 4 design thinking questions
    "career": "...",                   # Career connection text
    "images": {                        # 5 images with prompts
        "cover": ("filename.png", "AI prompt"),
        "landscape": (...),
        "modeling": (...),
        "discussion": (...),
        "stem": (...)
    },
    "pre_assessment": [...],           # 4 pre-assessment questions
    "extend_components": [("Name", "Desc"),...],  # 3 extension components
    "reflections": [...],              # 5 reflection questions
    "dimensions": [("Type", "Title", "Description"),...],  # 3 NGSS dimensions
    "cast_items": [...],               # 3 CAST alignment items
    "cast_questions": [("Type:", "Question"),...],  # 2 CAST-style questions
    "background_intro": "...",         # Teacher background intro
    "background_sections": [("Title", "Content"),...],  # 4 background sections
    "lever_L": "...",                  # LEVER Locate description
    "lever_E": "...",                  # LEVER Establish description
    "lever_V": "...",                  # LEVER Visualize description
    "lever_Ev": "...",                 # LEVER Evaluate description
    "lever_R": "...",                  # LEVER Revise description
    "slides_guide": [{...},...],       # 9 slide facilitation guides
    "sort_reasoning": "...",           # Expected sorting rationale
    "relationships": [("Connection", "Sign", "Explanation"),...],  # 3 relationships
    "sim_answers": [("Scenario", "Answer"),...],  # 2 simulation answer keys
    "reflection_exemplars": [("Q", "A"),...],  # 2 reflection exemplars
    "stem_intro": "...",               # STEM introduction guidance
    "stem_concepts": [("Concept", "Explanation"),...],  # 3 key concepts
    "stem_eval": [("Level", "Criteria"),...],  # 4-level rubric
    "support": [...],                  # 3 scaffolds for struggling learners
    "extensions": [...],               # 3 advanced extensions
    "cross_curr": [("Subject", "Connection"),...],  # 3 cross-curricular
    "misconceptions": [("Misconception", "Reality", "Response"),...],  # 3 misconceptions
}
```

---

## 6. IMAGE GENERATION PROTOCOL

**API:** OpenRouter with NanoBanana model `google/gemini-2.5-flash-image`
**API Key:** Stored in `~/.env` as `OPENROUTER_API_KEY` (NEVER hardcode)
**Cost:** ~$0.04 per image, ~$1.90 per 50 images

**PROMPT TEMPLATE:**
```
Create a photorealistic, cinematic, ultra-crisp image of [SCENE]
featuring a diverse, multicultural group with Black people centered
(a mix of skin tones and ethnicities represented), age-accurate for
[AGE RANGE] (no one looks like an adult if they're a kid).
Style: modern education / future-ready / middle school coolness,
confident, aspirational, realistic. Composition: clean framing,
natural body proportions, realistic hair detail (coils, curls, locs, braids).
Camera/lighting: soft natural window light, shallow depth of field,
35mm/50mm look. Quality: high-resolution, professional editorial photo.
```

**DIVERSITY GUIDELINES:**
- 70-80% Black and Brown children
- Good mix of Black and Brown children, with diverse representation
- Teachers/adults should appear as adults in leadership roles
- Non-stereotypical, culturally responsive imagery
- Everyone in leadership roles, flattering/empowering positions
- PHOTOREALISTIC only — no cartoons or illustrations
- "Middle school cool" aesthetic

**5 Images Per Lesson:**
1. `cover` — Dramatic phenomenon/topic image
2. `landscape` — Students engaged in related activity
3. `modeling` — Students at computers building models
4. `discussion` — Teacher-led classroom discussion
5. `stem` — Students doing STEM challenge

---

## 7. FILE STRUCTURE

```
cast-science-resources/
├── scripts/
│   ├── create_lesson_materials.py      # G05-L01 exemplar generator
│   ├── create_all_lessons_L02_L10.py   # G05 batch generator (L02-L10)
│   ├── lesson_data_L02_L10.py          # G05 lesson data
│   ├── create_all_lessons_G06.py       # G06 batch generator (all 10)
│   ├── lesson_data_G06.py             # G06 lesson data
│   ├── create_all_lessons_G08.py       # G08 batch generator (all 10)
│   └── lesson_data_G08.py             # G08 lesson data
├── materials/
│   ├── grade-05/
│   │   ├── G05-L01/ through G05-L10/  # Each contains:
│   │   │   ├── G0X-L0X-Student-Presentation.pptx
│   │   │   ├── G0X-L0X-Student-Activity-Pack.docx
│   │   │   ├── G0X-L0X-Teachers-Guide.docx
│   │   │   └── images/ (5 PNGs)
│   ├── grade-06/
│   │   ├── G06-L01/ through G06-L10/  # Same structure
│   ├── grade-08/
│   │   ├── G08-L01/ through G08-L10/  # Same structure
├── reference/
│   └── NGSS-Badge-Certification/
│       ├── GAP-ANALYSIS.md
│       └── *.pdf (4 reference docs)
└── PROTOCOLS.md (this file)
```

---

## 8. NGSS STANDARDS COVERAGE

### Grade 5 Lessons
| Lesson | NGSS | Topic |
|--------|------|-------|
| G05-L01 | 5-ESS2-1 | When Trees Become Matches (Wildfires) |
| G05-L02 | 5-LS2-1 | Nature's Recycling System (Decomposition) |
| G05-L03 | 5-PS3-1 | Powered by the Sun (Energy Transfer) |
| G05-L04 | 5-ESS2-1 | When Rain Becomes a River (Water Cycle) |
| G05-L05 | 5-ESS3-1 | Breathing in the City (Air Quality) |
| G05-L06 | 5-LS1-1 | The Secret Life of Seeds (Plant Growth) |
| G05-L07 | 5-PS1-3 | Kitchen Chemistry (States of Matter) |
| G05-L08 | 5-LS2-1 | Predator vs. Prey (Population Balance) |
| G05-L09 | 5-ESS1-2 | Starlight Is Old Light (Space) |
| G05-L10 | 5-PS2-1 | The Gravity Challenge (Forces) |

### Grade 6 Lessons
| Lesson | NGSS | Topic |
|--------|------|-------|
| G06-L01 | MS-LS1-1/2 | Why Can't You See Your Own Cells? |
| G06-L02 | MS-ESS2-2 | When the Earth Cracks Open (Plate Tectonics) |
| G06-L03 | MS-PS3-3/4 | Why Your Hot Cocoa Betrays You (Thermal Energy) |
| G06-L04 | MS-ESS2-1/3 | The Rock That Remembers Everything (Rock Cycle) |
| G06-L05 | MS-PS1-1/2 | Slime Is Serious Science (Molecular Structure) |
| G06-L06 | MS-LS1-3 | Your Body Is a City of Trillions (Body Systems) |
| G06-L07 | MS-LS1-6 | The Invisible Plant Factory (Photosynthesis) |
| G06-L08 | MS-ESS3-2 | Can You Outsmart a Disaster? (Natural Hazards) |
| G06-L09 | MS-PS1-3/6 | Your Sneakers Are Made of Dinosaurs (Synthetic Materials) |
| G06-L10 | MS-LS2-2/3/5 | The Secret War in Your Backyard (Ecosystems) |

### Grade 8 Lessons
| Lesson | NGSS | Topic |
|--------|------|-------|
| G08-L01 | MS-LS4-4/6 | Superbugs (Antibiotic Resistance) |
| G08-L02 | MS-LS2-1/4 | Reef Bleaching (Ecosystem Collapse) |
| G08-L03 | MS-ESS3-3/4 | Phone's Dirty Secret (E-Waste) |
| G08-L04 | MS-ESS2-5/6 | Hurricanes Getting Angrier |
| G08-L05 | MS-PS3-1/2 | Roller Coaster Equation (Energy) |
| G08-L06 | MS-PS2-1/2 | Concussion Problem (Forces) |
| G08-L07 | MS-LS1-5/7 | Food Into Dunks (Cell Respiration) |
| G08-L08 | MS-LS3-1/2 | Genetics (Inheritance) |
| G08-L09 | MS-PS4-1/2 | Music Is a Wave (Wave Properties) |
| G08-L10 | MS-PS1-4/5 | Hand Warmers (Chemical Reactions) |

---

## 9. LEVER FRAMEWORK

Every lesson follows the LEVER scientific modeling framework:
1. **L**ocate — Identify system COMPONENTS (parts)
2. **E**stablish — Connect with RELATIONSHIPS (+ or -)
3. **V**isualize — Build the model in ModelIt!
4. **E**valuate — Run SIMULATIONS to test scenarios
5. **R**evise — Improve model based on evidence

---

## 10. API KEY MANAGEMENT

```python
# ALWAYS load from ~/.env — NEVER hardcode
import dotenv as _dotenv
import os
_dotenv.load_dotenv(os.path.join(os.path.expanduser('~'), '.env'))
API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
```

**~/.env file location:** `C:\Users\ginja\.env`
**Contains:**
```
GOOGLE_AI_STUDIO_API_KEY=<key>
OPENROUTER_API_KEY=<key>
```

---

## 11. GITHUB WORKFLOW

- **Fork repo:** `alexandriasworld1234-source/cast-science-resources`
- **Branch:** `master`
- **Push command:** `git push origin master`
- **Auth:** GitHub CLI (`gh auth`) — device flow method
- **Account:** `alexandriasworld1234-source`

---

## 12. PYTHON DEPENDENCIES

```
python-pptx     # PowerPoint generation
python-docx     # Word document generation
Pillow           # Image handling (aspect ratio)
requests         # API calls
python-dotenv    # .env file loading
pymupdf          # PDF reading (fitz)
```

---

## 13. NGSS BADGE CERTIFICATION (FUTURE WORK)

A gap analysis is stored at `reference/NGSS-Badge-Certification/GAP-ANALYSIS.md`.

**Key findings:**
- Core approach is sound — LEVER framework maps well to NGSS
- **Must organize lessons into coherent UNITS with storylines** (biggest gap)
- **Must add explicit Crosscutting Concept (CCC) integration** to student activities
- **Must create 3D assessment tasks** integrating SEP + DCI + CCC
- Must add "Return to Phenomenon" moments and formative checkpoints

**Reference PDFs in repo:**
- EQuIP Detailed Guidance March 2021
- NGSS Lesson Screener
- TAPS SEPs
- NGSS articles January 2026

---

## 14. HOW TO GENERATE NEW LESSONS

1. **Create lesson data** in `scripts/lesson_data_G[XX].py` following the 46-field structure
2. **Copy the batch generator** from an existing grade and update:
   - Import source (`from lesson_data_G[XX] import ALL_LESSONS`)
   - `GRADE_LABEL` (e.g., "6th Grade")
   - `AGE_RANGE` (e.g., "11-12 years old")
   - `BASE_DIR` output path (e.g., `materials/grade-06`)
3. **Run the generator:** `python scripts/create_all_lessons_G[XX].py`
4. **Retry any failed images** — check output for `[!] No image in response`
5. **Rebuild PPTs** for lessons with retried images
6. **Push to repo:** `git add materials/grade-[XX]/ scripts/*G[XX]* && git commit && git push`

---

## 15. QUICK COMMANDS

```bash
# Generate all Grade 8 lessons
cd cast-science-resources/scripts
python create_all_lessons_G08.py

# Test lesson data loads
python -c "from lesson_data_G08 import ALL_LESSONS; print(len(ALL_LESSONS))"

# Check image count
ls materials/grade-08/G08-L*/images/ | wc -l

# Push to GitHub
git add . && git commit -m "message" && git push origin master
```
