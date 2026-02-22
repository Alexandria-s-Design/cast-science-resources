# ModelIt! CAST Science Resources — Session Protocols

## Use this document to continue working in a new Claude Code / PowerShell session.

---

## 1. PROJECT OVERVIEW

**Project:** CAST/ModelIt! Science Curriculum Materials
**Repository:** `cast-science-resources` (GitHub fork: `alexandriasworld1234-source/cast-science-resources`)
**Working Directory:** `C:\Users\ginja\cast-science-resources`
**Status:** Grade 5 complete (10 lessons), Grade 6 complete (10 lessons), Grade 7 complete (10 lessons), Grade 8 complete (10 lessons), Grade 9 complete (30 lessons: 10 per level × 3 levels)

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
│   ├── create_all_lessons_G07.py       # G07 batch generator (all 10)
│   ├── lesson_data_G07.py             # G07 lesson data
│   ├── create_all_lessons_G08.py       # G08 batch generator (all 10)
│   ├── lesson_data_G08.py             # G08 lesson data
│   ├── create_all_lessons_G09.py       # G09 unified batch generator (all 3 levels)
│   ├── lesson_data_G09_L1.py          # G09 Level 1 lesson data (10 lessons)
│   ├── lesson_data_G09_L2.py          # G09 Level 2 lesson data (10 lessons)
│   ├── lesson_data_G09_L3.py          # G09 Level 3 lesson data (10 lessons)
│   └── generate_lesson_markdown.py    # Markdown lesson file generator (all grades)
├── materials/
│   ├── grade-05/
│   │   ├── G05-L01/ through G05-L10/  # Each contains:
│   │   │   ├── G0X-L0X-Student-Presentation.pptx
│   │   │   ├── G0X-L0X-Student-Activity-Pack.docx
│   │   │   ├── G0X-L0X-Teachers-Guide.docx
│   │   │   └── images/ (5 PNGs)
│   ├── grade-06/
│   │   ├── G06-L01/ through G06-L10/  # Same structure
│   ├── grade-07/
│   │   ├── G07-L01/ through G07-L10/  # Same structure
│   ├── grade-08/
│   │   ├── G08-L01/ through G08-L10/  # Same structure
│   ├── grade-09/
│   │   ├── level-1/
│   │   │   ├── G09L1-L01/ through G09L1-L10/  # Level 1: Foundations (4-5 components)
│   │   ├── level-2/
│   │   │   ├── G09L2-L01/ through G09L2-L10/  # Level 2: Advanced (6-8 components)
│   │   ├── level-3/
│   │   │   ├── G09L3-L01/ through G09L3-L10/  # Level 3: Biotech (8-10 components)
├── lessons/
│   ├── grade-06/ through grade-08/    # Markdown lesson files
│   ├── grade-09/
│   │   ├── level-1/                   # Level 1 markdown lessons
│   │   ├── level-2/                   # Level 2 markdown lessons
│   │   ├── level-3/                   # Level 3 markdown lessons
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

### Grade 7 Lessons
| Lesson | NGSS | Topic |
|--------|------|-------|
| G07-L01 | MS-ESS1-1, MS-ESS1-2 | Blood Moon (Earth-Sun-Moon System) |
| G07-L02 | MS-LS4-1, MS-LS4-2 | Your Inner Fish (Fossil Evidence) |
| G07-L03 | MS-ESS3-5 | Earth Has a Fever (Climate Change) |
| G07-L04 | MS-PS2-3, MS-PS2-5 | Invisible Force (Electromagnetism) |
| G07-L05 | MS-ESS2-4 | Recycled Dinosaur Water (Water Cycle) |
| G07-L06 | MS-LS1-8 | Hot Cheetos Make You Cry (Sensory Processing) |
| G07-L07 | MS-PS3-5 | Can't Slide Forever (Energy Transfer & Friction) |
| G07-L08 | MS-ESS1-4 | Crime Scene in Every Rock (Geologic History) |
| G07-L09 | MS-LS4-5 | Built a Better Dog (Artificial Selection) |
| G07-L10 | MS-PS4-3 | Phone Speaks in 1s and 0s (Digital Signals) |

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

### Grade 9 Level 1: Foundations of Computational Modeling
| Lesson | NGSS | Topic | Components |
|--------|------|-------|------------|
| G09L1-L01 | HS-LS1-3 | Why Do Athletes Collapse in the Heat? | 4 |
| G09L1-L02 | HS-LS1-2 | The Vaping Crisis | 5 |
| G09L1-L03 | HS-ESS1-2, HS-ETS1-2 | Can We Actually Live on Mars? | 5 |
| G09L1-L04 | HS-PS3-1, HS-PS3-3 | Why Your Phone Battery Dies So Fast | 5 |
| G09L1-L05 | HS-ESS3-6, HS-PS1-7 | The Ocean Is Turning to Acid | 5 |
| G09L1-L06 | HS-LS3-1 | Why Some People Can't Drink Milk | 5 |
| G09L1-L07 | HS-LS1-2 | How Social Media Hacks Your Brain | 5 |
| G09L1-L08 | HS-ESS3-4, HS-ETS1-3 | Fast Fashion Is Killing the Planet | 5 |
| G09L1-L09 | HS-ESS2-1 | Why Earthquakes Hit Some Cities Harder | 5 |
| G09L1-L10 | HS-ESS3-3, HS-LS2-6 | The Wildfire Feedback Loop | 5 |

### Grade 9 Level 2: Advanced Computational Modeling
| Lesson | NGSS | Topic | Components |
|--------|------|-------|------------|
| G09L2-L01 | HS-LS4-2, HS-LS4-3 | The Antibiotic Resistance Arms Race | 7 |
| G09L2-L02 | HS-ESS3-5, HS-ESS2-4 | Climate Tipping Points | 7 |
| G09L2-L03 | HS-LS2-6, HS-ETS1-4 | Why Pandemics Go Exponential | 7 |
| G09L2-L04 | HS-LS1-2, HS-ETS1-4 | The Opioid Epidemic | 7 |
| G09L2-L05 | HS-LS2-6, HS-ESS3-3 | Coral Reef Collapse | 7 |
| G09L2-L06 | HS-ESS3-4, HS-ETS1-2 | The Water-Energy-Food Nexus | 6 |
| G09L2-L07 | HS-ESS3-4, HS-PS3-4 | Urban Heat Islands | 6 |
| G09L2-L08 | HS-LS3-1, HS-LS4-5 | CRISPR Gene Drives | 7 |
| G09L2-L09 | HS-LS2-6, HS-ESS3-3 | Microplastics in the Food Chain | 7 |
| G09L2-L10 | HS-PS3-3, HS-ETS1-3 | Renewable Energy Grid Optimization | 8 |

### Grade 9 Level 3: Biotech Modeling & Simulation
| Lesson | NGSS | Topic | Components |
|--------|------|-------|------------|
| G09L3-L01 | HS-LS1-1, HS-PS2-6 | Protein Folding and Drug Design | 8 |
| G09L3-L02 | HS-LS1-4, HS-LS3-1 | Cancer Cell Signaling Networks | 9 |
| G09L3-L03 | HS-LS1-1, HS-ETS1-2 | Synthetic Biology: Engineering Life | 8 |
| G09L3-L04 | HS-LS1-2, HS-PS1-7 | Pharmacokinetics: Drug Delivery | 9 |
| G09L3-L05 | HS-LS2-6, HS-ESS3-5 | Ecosystem Tipping Points | 10 |
| G09L3-L06 | HS-LS1-2, HS-PS4-1 | Neural Network Modeling | 8 |
| G09L3-L07 | HS-LS1-5, HS-ETS1-3 | Metabolic Engineering for Biofuels | 9 |
| G09L3-L08 | HS-LS3-1, HS-LS1-4 | Gene Regulatory Networks | 10 |
| G09L3-L09 | HS-LS1-4, HS-LS4-2 | Vaccine Design Optimization | 9 |
| G09L3-L10 | HS-ESS3-5, HS-LS2-6 | Climate-Ecosystem Coupled Models | 10 |

---

## 8b. GRADE 9 LEVEL DEFINITIONS

### Level 1: Foundations of Computational Modeling
- **Target Students:** Students new to computational modeling or who need foundational skills
- **Components:** 4-5 per model
- **Model Complexity:** Linear cause-and-effect relationships, single feedback loops
- **Relationships:** Primarily positive (+) and negative (-) linear relationships
- **Key Skills:** Component identification, basic relationship mapping, simple simulation interpretation
- **Materials Design:** Scaffolded activities, explicit LEVER framework walkthrough, concrete real-world phenomena
- **Assessment Focus:** Can students identify components and trace single cause-effect chains?

### Level 2: Advanced Computational Modeling
- **Target Students:** Students who have mastered Level 1 skills and need more challenge; developing college readiness
- **Components:** 6-8 per model
- **Model Complexity:** Multiple interacting feedback loops, threshold effects, non-linear dynamics, coupled subsystems
- **Relationships:** Non-linear relationships, conditional thresholds, delayed effects, amplifying feedback
- **Key Skills:** Multi-variable analysis, identifying emergent behavior, intervention optimization, quantitative reasoning
- **Materials Design:** More open-ended investigations, less scaffolding, emphasis on model critique and revision
- **Assessment Focus:** Can students analyze multi-variable systems and predict emergent outcomes?

### Level 3: Biotech Modeling & Simulation
- **Target Students:** Advanced students pursuing computational biology / biotechnology pathways
- **Components:** 8-10 per model
- **Model Complexity:** Multi-scale systems (molecular → cellular → organism → ecosystem), optimization problems, synthetic design challenges
- **Relationships:** Complex network interactions, cascading effects, scale-dependent dynamics, stochastic elements
- **Three Core Biotech Skills:**
  1. **Multi-scale Modeling** — Connecting molecular-level processes to organism/ecosystem-level outcomes
  2. **Predictive Optimization** — Finding optimal parameter combinations for desired outcomes
  3. **Systems Biology & Synthetic Design** — Engineering biological systems using computational predictions
- **Materials Design:** Research-grade scenarios, minimal scaffolding, professional scientific vocabulary, design-build-test cycles
- **Assessment Focus:** Can students design, optimize, and defend complex multi-scale computational models?

### Level Comparison Summary
| Aspect | Level 1 | Level 2 | Level 3 |
|--------|---------|---------|---------|
| Components | 4-5 | 6-8 | 8-10 |
| Feedback Loops | Single | Multiple | Complex networks |
| Relationships | Linear | Non-linear, threshold | Multi-scale, cascading |
| Scaffolding | High | Moderate | Minimal |
| Vocabulary | Foundational | Intermediate | Research-grade |
| Assessment | Trace chains | Analyze systems | Design & optimize |
| College Readiness | Introduction | Developing | Advanced |

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
   - **For Grade 9:** `python scripts/create_all_lessons_G09.py 1 2 3` (or individual levels)
4. **Retry any failed images** — check output for `[!] No image in response`
5. **Rebuild PPTs** for lessons with retried images
6. **Generate markdown:** `python scripts/generate_lesson_markdown.py G09L1 G09L2 G09L3`
7. **Push to repo:** `git add materials/grade-[XX]/ scripts/*G[XX]* && git commit && git push`

---

## 15. QUICK COMMANDS

```bash
# Generate all Grade 8 lessons
cd cast-science-resources/scripts
python create_all_lessons_G08.py

# Generate Grade 9 (all 3 levels — 30 lessons, 150 images)
python create_all_lessons_G09.py 1 2 3

# Generate Grade 9 Level 1 only
python create_all_lessons_G09.py 1

# Test lesson data loads
python -c "from lesson_data_G08 import ALL_LESSONS; print(len(ALL_LESSONS))"
python -c "from lesson_data_G09_L1 import ALL_LESSONS; print(len(ALL_LESSONS))"

# Generate markdown lesson files
python generate_lesson_markdown.py G09L1 G09L2 G09L3

# Check image count
ls materials/grade-09/level-*/G09L*/images/ | wc -l

# Push to GitHub
git add . && git commit -m "message" && git push origin master
```
