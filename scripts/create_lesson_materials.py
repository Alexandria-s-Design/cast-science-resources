"""
ModelIt Lesson Materials Generator v2
Creates PowerPoint, Student Activity Pack (Word), and Teacher's Guide (Word)
matching the official TPT branding style.

Output: .pptx for presentations, .docx for documents (user converts to PDF later)

Brand Elements:
- Blue diagonal geometric corners (navy, medium blue, light blue layers)
- ModelIt! logo with molecule/network icon
- Science doodle border concept for B&W worksheet pages
- Student Name/Date on every page
- STEM Challenge included with detailed teacher guidance
- Recording Page included
- NGSS unpacking with Framework references
- LEVER methodology explanation
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
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

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

# Lesson configuration
LESSON_ID = "G05-L01"
LESSON_TITLE = "When Trees Become Matches"
LESSON_SUBTITLE = "California's Burning Season and the Earth Systems That Fuel It"
NGSS_STANDARD = "5-ESS2-1"
GRADE_LEVEL = "5th Grade"

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'materials', 'grade-05', LESSON_ID)


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'images'), exist_ok=True)


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


def add_image_placeholder(slide, x, y, width, height, description):
    """Add a placeholder box for images with description"""
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(y), Inches(width), Inches(height))
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xF0, 0xF5, 0xFA)
    box.line.color.rgb = MID_BLUE
    box.line.width = Pt(2)

    text_box = slide.shapes.add_textbox(
        Inches(x + 0.2), Inches(y + height/2 - 0.3),
        Inches(width - 0.4), Inches(0.6))
    tf = text_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"[IMAGE: {description}]"
    p.font.size = Pt(11)
    p.font.italic = True
    p.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p.alignment = PP_ALIGN.CENTER


def create_powerpoint():
    """Create the student presentation PowerPoint"""
    output_path = os.path.join(OUTPUT_DIR, f'{LESSON_ID}-Student-Presentation.pptx')
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # SLIDE 1: Cover
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_diagonal_corners(slide, prs)
    add_modelit_logo(slide, 3.5, 1.8)

    header = slide.shapes.add_textbox(Inches(1), Inches(3.2), Inches(8), Inches(0.6))
    tf = header.text_frame
    p = tf.paragraphs[0]
    p.text = "Student Lesson"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    title = slide.shapes.add_textbox(Inches(0.5), Inches(3.8), Inches(9), Inches(1.2))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = LESSON_TITLE
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE
    p.alignment = PP_ALIGN.CENTER

    sub = tf.add_paragraph()
    sub.text = LESSON_SUBTITLE
    sub.font.size = Pt(18)
    sub.font.italic = True
    sub.font.color.rgb = DARK_TEXT
    sub.alignment = PP_ALIGN.CENTER

    add_image_placeholder(slide, 3, 5.2, 4, 1.8,
        "California hillside showing dry golden grass and scattered trees during fire season. Warm sunset lighting. Culturally diverse community visible in distance.")

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

    question = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1.5))
    tf = question.text_frame
    p = tf.paragraphs[0]
    p.text = "Why does California burn at the same time every year?"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE
    p.alignment = PP_ALIGN.CENTER

    add_image_placeholder(slide, 2, 4, 6, 2.8,
        "Split image: Left shows green California hillside in spring (rainy season). Right shows same hillside golden/brown in fall (fire season). Diverse group of 5th graders pointing at both images, discussing the difference. 70% students of color.")

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

    content = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(8.5), Inches(4))
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
        p.font.size = Pt(22)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(18)

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
        p.font.size = Pt(20)

    p = tf.add_paragraph()
    p.text = "\nSort them into two groups!"
    p.font.size = Pt(18)
    p.font.italic = True
    p.font.color.rgb = BRAND_BLUE

    add_image_placeholder(slide, 5.5, 2.2, 4, 3.5,
        "Screenshot placeholder: ModelIt interface showing component sorting activity. Show the drag-and-drop area with Internal and External labels. Clean, educational style.")

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

    content = slide.shapes.add_textbox(Inches(0.5), Inches(2.2), Inches(9), Inches(3.5))
    tf = content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Draw arrows to show HOW components affect each other:"
    p.font.size = Pt(20)

    relationships = [
        "(+) POSITIVE: When one goes UP, the other goes UP",
        "(-) NEGATIVE: When one goes UP, the other goes DOWN"
    ]
    for rel in relationships:
        p = tf.add_paragraph()
        p.text = rel
        p.font.size = Pt(18)
        p.space_before = Pt(12)

    p = tf.add_paragraph()
    p.text = "\nThink: When RAINFALL goes UP, does DRY VEGETATION go UP or DOWN?"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE

    add_image_placeholder(slide, 2.5, 5, 5, 1.8,
        "Diagram showing: Rainfall --(-)--> Dry Vegetation --(+)--> Fire Spread <--(+)-- Wind. Clean arrows with +/- labels. Educational style matching ModelIt aesthetic.")

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
    p.text = "\nWatch the graphs!"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE

    add_image_placeholder(slide, 5.2, 2.2, 4.3, 4,
        "Screenshot placeholder: ModelIt simulation results showing activity graphs. Display how Dry Vegetation and Fire Spread increase when Rainfall is OFF. Clear, educational visualization.")

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

    content = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(8.5), Inches(4.5))
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
        p.font.size = Pt(24)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(16)

    add_image_placeholder(slide, 7, 4.5, 2.5, 2.5,
        "Group of diverse 5th grade students (70% students of color) having an animated discussion, pointing at a laptop screen showing their model. Engaged, curious expressions.")

    prs.save(output_path)
    print(f"[OK] Created: {output_path}")
    return output_path


# ============================================
# WORD DOCUMENT - HELPER FUNCTIONS
# ============================================

def add_page_header(doc, text):
    """Add a styled page header"""
    section = doc.sections[-1]
    header = section.header
    if not header.paragraphs:
        p = header.add_paragraph()
    else:
        p = header.paragraphs[0]
    p.text = text
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.runs[0] if p.runs else p.add_run()
    run.font.size = DocxPt(9)
    run.font.color.rgb = DOCX_BRAND_BLUE


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


def set_cell_shading(cell, color_hex):
    """Set background color of a table cell"""
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color_hex)
    cell._tc.get_or_add_tcPr().append(shading)


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

    # Image placeholder
    img_para = doc.add_paragraph()
    img_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = img_para.add_run("[IMAGE PLACEHOLDER: California wildfire landscape - golden hills, blue sky, diverse community in distance]")
    run.italic = True
    run.font.size = DocxPt(10)
    run.font.color.rgb = DocxRGB(0x66, 0x66, 0x66)

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
    rubric_intro.add_run("This rubric shows how your modeling work will be assessed. Each skill is rated 1-4.").font.size = DocxPt(11)

    doc.add_paragraph()

    # Rubric table
    rubric_data = [
        ["Skill", "4 - Expert", "3 - Proficient", "2 - Developing", "1 - Beginning"],
        ["Components", "All components correctly identified and sorted", "Most components correct", "Some components correct", "Needs help identifying components"],
        ["Relationships", "All arrows correct direction and +/- signs", "Most relationships correct", "Some relationships correct", "Needs help with relationships"],
        ["Simulation", "Runs multiple scenarios, explains patterns", "Runs scenarios, observes patterns", "Runs simulation with guidance", "Needs help running simulation"],
        ["Explanation", "Clear cause-effect explanation with evidence", "Explains connections", "Partial explanation", "Needs help explaining"],
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
            elif j == 0:
                cell.paragraphs[0].runs[0].bold = True

    doc.add_page_break()

    # ========== MODEL RECORDING PAGE ==========
    model_title = doc.add_paragraph()
    run = model_title.add_run("Model Recording Page")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    doc.add_paragraph("Use this page to sketch your model before or after building it in ModelIt!")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("My Components:")
    run.bold = True
    run.font.size = DocxPt(14)

    # Component boxes
    comp_table = doc.add_table(rows=2, cols=2)
    comp_table.style = 'Table Grid'
    labels = ["EXTERNAL Components\n(inputs from outside):", "INTERNAL Components\n(happen inside system):"]
    for i, cell in enumerate(comp_table.rows[0].cells):
        cell.text = labels[i]
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = DocxPt(10)
    for cell in comp_table.rows[1].cells:
        cell.text = "\n\n\n"

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("My Model Sketch:")
    run.bold = True
    run.font.size = DocxPt(14)

    doc.add_paragraph("Draw your components as circles. Draw arrows between them. Label each arrow with (+) or (-).")

    # Big sketch box
    sketch_table = doc.add_table(rows=1, cols=1)
    sketch_table.style = 'Table Grid'
    sketch_table.rows[0].cells[0].text = "\n\n\n\n\n\n\n\n\n\n"

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Key:")
    run.bold = True
    doc.add_paragraph("(+) = When one goes UP, the other goes UP")
    doc.add_paragraph("(-) = When one goes UP, the other goes DOWN")

    doc.add_page_break()

    # ========== SIMULATION OBSERVATIONS ==========
    sim_title = doc.add_paragraph()
    run = sim_title.add_run("Simulation Observations")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    doc.add_paragraph("Run each scenario and record what you observe in the graphs!")

    scenarios = [
        ("Scenario 1: DROUGHT", "Turn RAINFALL to OFF. Watch the simulation.",
         "What happens to DRY VEGETATION?", "What happens to FIRE SPREAD?"),
        ("Scenario 2: WINDY DAY", "Turn WIND to ON. Watch the simulation.",
         "What happens to FIRE SPREAD?", "Why do you think this happens?"),
        ("Scenario 3: FIRE SEASON", "Turn RAINFALL OFF and WIND ON.",
         "What happens to all the components?", "This is California in fall - why?"),
    ]

    for title, instruction, q1, q2 in scenarios:
        p = doc.add_paragraph()
        run = p.add_run(title)
        run.bold = True
        run.font.size = DocxPt(14)
        run.font.color.rgb = DOCX_BRAND_BLUE

        doc.add_paragraph(instruction)

        doc.add_paragraph(q1)
        response_table = doc.add_table(rows=1, cols=1)
        response_table.style = 'Table Grid'
        response_table.rows[0].cells[0].text = "\n\n"

        doc.add_paragraph(q2)
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

    doc.add_paragraph("Scientists are always adding to their models when they learn new information. Now it's your turn!")

    p = doc.add_paragraph()
    run = p.add_run("Research Challenge:")
    run.bold = True
    run.font.size = DocxPt(14)

    doc.add_paragraph("Find ONE new component that could affect California wildfires. Examples to research:")

    examples = ["Temperature / Heat waves", "Humidity levels", "Mountain slopes", "Santa Ana winds", "Human activity", "Invasive grasses"]
    for ex in examples:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(ex)

    doc.add_paragraph()
    doc.add_paragraph("My new component: ________________________________")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("How does it connect to the model?")
    run.bold = True

    doc.add_paragraph("Draw an arrow FROM or TO your new component. Label it (+) or (-).")

    sketch = doc.add_table(rows=1, cols=1)
    sketch.style = 'Table Grid'
    sketch.rows[0].cells[0].text = "\n\n\n\n"

    doc.add_paragraph()
    doc.add_paragraph("Explain the relationship: _______________________________________________")
    doc.add_paragraph("________________________________________________________________")

    doc.add_page_break()

    # ========== STEM CHALLENGE ==========
    stem_title = doc.add_paragraph()
    run = stem_title.add_run("STEM CHALLENGE")
    run.bold = True
    run.font.size = DocxPt(28)
    run.font.color.rgb = DOCX_NAVY

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Firebreak Engineers")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_BRAND_BLUE

    add_name_date_line(doc)

    # Mission box
    mission = doc.add_paragraph()
    run = mission.add_run("YOUR MISSION")
    run.bold = True
    run.font.size = DocxPt(16)
    run.font.color.rgb = DOCX_NAVY

    doc.add_paragraph("You've just learned that DRY VEGETATION is the FUEL that makes fires spread. Real firefighters and land managers use this knowledge to create FIREBREAKS - areas with no fuel where fire cannot spread!")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Your engineering challenge:")
    run.bold = True
    run.font.size = DocxPt(14)

    doc.add_paragraph("Design a firebreak system to protect a small community surrounded by dry forest.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("THE SCENARIO:")
    run.bold = True
    run.font.size = DocxPt(14)
    run.font.color.rgb = DOCX_BRAND_BLUE

    scenario_text = """Willow Creek is a small town surrounded by dry grassland and forest. Fire season is coming! The town council has hired YOUR engineering team to design firebreaks that will protect the community.

You have a LIMITED BUDGET - you can only clear 3 firebreak zones. Where will you put them for maximum protection?"""
    doc.add_paragraph(scenario_text)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("MATERIALS (grab from around the room!):")
    run.bold = True
    run.font.size = DocxPt(12)

    materials = ["Paper (to draw your map)", "Pencil/markers", "Your brain and teamwork!"]
    for m in materials:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(m)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("YOUR DESIGN STEPS:")
    run.bold = True
    run.font.size = DocxPt(14)
    run.font.color.rgb = DOCX_BRAND_BLUE

    steps = [
        "SKETCH the town in the center of your paper",
        "Draw the surrounding forest and grassland (the FUEL!)",
        "Add wind arrows showing Santa Ana winds come from the EAST",
        "Draw your 3 firebreak zones - where will you remove vegetation?",
        "Explain WHY you chose each location"
    ]
    for i, step in enumerate(steps, 1):
        p = doc.add_paragraph()
        run = p.add_run(f"Step {i}: ")
        run.bold = True
        p.add_run(step)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("THINK LIKE AN ENGINEER:")
    run.bold = True
    run.font.size = DocxPt(12)

    questions = [
        "Which direction does fire spread fastest? (Remember: wind!)",
        "Should firebreaks be uphill or downhill from town?",
        "How does this connect to your model? (Hint: What happens when you reduce Dry Vegetation?)"
    ]
    for q in questions:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(q)

    doc.add_page_break()

    # STEM Challenge Design Page
    design_title = doc.add_paragraph()
    run = design_title.add_run("My Firebreak Design")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    add_name_date_line(doc)

    p = doc.add_paragraph()
    run = p.add_run("Team Members: ")
    run.bold = True
    p.add_run("_________________________________________________")

    doc.add_paragraph()
    doc.add_paragraph("Draw your map here (town in center, forest around, wind direction, and your 3 firebreaks):")

    # Big design box
    design_box = doc.add_table(rows=1, cols=1)
    design_box.style = 'Table Grid'
    design_box.rows[0].cells[0].text = "\n\n\n\n\n\n\n\n\n\n\n\n"

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Explain your design:")
    run.bold = True

    doc.add_paragraph("Firebreak #1 location and reason:")
    fb1 = doc.add_table(rows=1, cols=1)
    fb1.style = 'Table Grid'
    fb1.rows[0].cells[0].text = "\n\n"

    doc.add_paragraph("Firebreak #2 location and reason:")
    fb2 = doc.add_table(rows=1, cols=1)
    fb2.style = 'Table Grid'
    fb2.rows[0].cells[0].text = "\n\n"

    doc.add_paragraph("Firebreak #3 location and reason:")
    fb3 = doc.add_table(rows=1, cols=1)
    fb3.style = 'Table Grid'
    fb3.rows[0].cells[0].text = "\n\n"

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("CONNECTION TO YOUR MODEL:")
    run.bold = True
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph("How does your firebreak design connect to what you learned in ModelIt?")
    conn = doc.add_table(rows=1, cols=1)
    conn.style = 'Table Grid'
    conn.rows[0].cells[0].text = "\n\n\n"

    doc.save(output_path)
    print(f"[OK] Created: {output_path}")
    return output_path


# ============================================
# TEACHER'S GUIDE (WORD)
# ============================================

def create_teachers_guide():
    """Create the teacher's guide as Word document with enhanced content"""
    output_path = os.path.join(OUTPUT_DIR, f'{LESSON_ID}-Teachers-Guide.docx')
    doc = Document()

    # Set margins
    for section in doc.sections:
        section.top_margin = DocxInches(0.75)
        section.bottom_margin = DocxInches(0.75)
        section.left_margin = DocxInches(0.75)
        section.right_margin = DocxInches(0.75)

    # ========== COVER PAGE ==========
    doc.add_paragraph()

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("ModelIt!")
    run.bold = True
    run.font.size = DocxPt(48)
    run.font.color.rgb = DOCX_NAVY

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Teacher's Guide")
    run.font.size = DocxPt(28)
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph()

    lesson = doc.add_paragraph()
    lesson.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = lesson.add_run(f"{LESSON_ID}: {LESSON_TITLE}")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = sub.add_run(LESSON_SUBTITLE)
    run.italic = True
    run.font.size = DocxPt(14)

    doc.add_paragraph()
    doc.add_paragraph()

    # Quick reference table
    quick_ref = [
        ["Grade Level", GRADE_LEVEL],
        ["NGSS Standard", NGSS_STANDARD],
        ["Time", "40-45 minutes (can split across 2 days)"],
        ["Materials", "Student devices with ModelIt access, Activity Pack"],
        ["Prep Required", "None - lesson is self-contained"],
    ]

    table = doc.add_table(rows=len(quick_ref), cols=2)
    table.style = 'Table Grid'
    for i, (label, value) in enumerate(quick_ref):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[0].paragraphs[0].runs[0].bold = True
        set_cell_shading(table.rows[i].cells[0], "7EC8E3")
        table.rows[i].cells[1].text = value

    doc.add_page_break()

    # ========== NGSS STANDARDS UNPACKING ==========
    standards_title = doc.add_paragraph()
    run = standards_title.add_run("NGSS Standards Unpacking")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Performance Expectation: 5-ESS2-1")
    run.bold = True
    run.font.size = DocxPt(14)
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph("Develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and/or atmosphere interact.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("How This Lesson Addresses the Standard:")
    run.bold = True
    run.font.size = DocxPt(12)

    connections = [
        ("Geosphere", "California's terrain and slopes affect how fires spread"),
        ("Biosphere", "Vegetation (living plants) serves as fuel for fires"),
        ("Hydrosphere", "Rainfall (or lack of it) determines how dry vegetation becomes"),
        ("Atmosphere", "Wind patterns and weather drive fire behavior"),
    ]

    for sphere, connection in connections:
        p = doc.add_paragraph()
        run = p.add_run(f"{sphere}: ")
        run.bold = True
        p.add_run(connection)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("From A Framework for K-12 Science Education (NRC, 2012):")
    run.bold = True
    run.font.size = DocxPt(12)
    run.font.color.rgb = DOCX_BRAND_BLUE

    framework_quote = doc.add_paragraph()
    framework_quote.style = 'Quote'
    framework_quote.add_run("\"Earth's major systems are the geosphere, the hydrosphere, the atmosphere, and the biosphere. These systems interact in multiple ways to affect Earth's surface materials and processes. The ocean supports a variety of ecosystems and organisms, shapes landforms, and influences climate. Winds and clouds in the atmosphere interact with the landforms to determine patterns of weather.\" (p. 187)")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Key Disciplinary Core Idea (ESS2.A):")
    run.bold = True

    doc.add_paragraph("Earth's major systems interact in multiple ways to affect Earth's surface materials and processes. Students should understand that these interactions create observable phenomena - in this case, the predictable fire seasons in California.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Science & Engineering Practices Addressed:")
    run.bold = True
    run.font.size = DocxPt(12)

    practices = [
        ("Developing and Using Models", "Students build a computational model showing system interactions"),
        ("Analyzing and Interpreting Data", "Students observe simulation graphs and identify patterns"),
        ("Constructing Explanations", "Students explain cause-effect relationships in the system"),
        ("Engaging in Argument from Evidence", "Students predict and justify what will happen under different conditions"),
    ]

    for practice, description in practices:
        p = doc.add_paragraph()
        run = p.add_run(f"- {practice}: ")
        run.bold = True
        p.add_run(description)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Crosscutting Concepts:")
    run.bold = True
    run.font.size = DocxPt(12)

    ccc = [
        ("Cause and Effect", "Central to this lesson - students trace how drought causes dry vegetation, which causes fire spread"),
        ("Systems and System Models", "Students explicitly build a model of Earth system interactions"),
    ]

    for concept, desc in ccc:
        p = doc.add_paragraph()
        run = p.add_run(f"- {concept}: ")
        run.bold = True
        p.add_run(desc)

    doc.add_page_break()

    # ========== LEVER FRAMEWORK ==========
    lever_title = doc.add_paragraph()
    run = lever_title.add_run("The LEVER Framework")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("What is LEVER?")
    run.bold = True
    run.font.size = DocxPt(14)
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph("LEVER is ModelIt's pedagogical framework for teaching systems thinking through computational modeling. Each phase guides students through authentic scientific practices while building deep conceptual understanding.")

    doc.add_paragraph()
    lever_phases = [
        ("L - LOCATE the System",
         "Students identify the components (parts) of the system they're studying.",
         "Students sort components into INTERNAL (happening inside the system) and EXTERNAL (inputs from outside).",
         "\"What are the important parts of this system?\" \"What can we control vs. what happens naturally?\""),

        ("E - ESTABLISH Relationships",
         "Students determine HOW components affect each other.",
         "Students draw arrows with (+) for positive relationships and (-) for negative relationships.",
         "\"When this goes UP, does that go UP or DOWN?\" \"How do these parts connect?\""),

        ("V - VISUALIZE & Model",
         "Students build their model in the ModelIt platform.",
         "Students arrange components and create the network of relationships.",
         "\"How should we organize this?\" \"Does our model match our thinking?\""),

        ("E - EVALUATE Outcomes",
         "Students run simulations and analyze the results.",
         "Students observe graphs, test scenarios, and identify patterns.",
         "\"What happens when...?\" \"Why do you think that happened?\""),

        ("R - REVISE & Extend",
         "Students improve their model based on new information.",
         "Students add components from research, fix errors, and explore extensions.",
         "\"What's missing?\" \"How could we make this more accurate?\""),
    ]

    for phase, description, student_action, questions in lever_phases:
        p = doc.add_paragraph()
        run = p.add_run(phase)
        run.bold = True
        run.font.size = DocxPt(12)
        run.font.color.rgb = DOCX_BRAND_BLUE

        doc.add_paragraph(description)

        p = doc.add_paragraph()
        run = p.add_run("Student Action: ")
        run.bold = True
        p.add_run(student_action)

        p = doc.add_paragraph()
        run = p.add_run("Key Questions: ")
        run.italic = True
        p.add_run(questions)

        doc.add_paragraph()

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Why LEVER Works:")
    run.bold = True
    run.font.size = DocxPt(12)

    reasons = [
        "Mirrors authentic scientific practice (scientists build, test, and revise models)",
        "Builds from concrete (components) to abstract (relationships)",
        "Encourages productive struggle and exploration",
        "Centers student reasoning over memorization",
        "Connects to NGSS three-dimensional learning (SEPs, DCIs, CCCs)",
    ]
    for r in reasons:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(r)

    doc.add_page_break()

    # ========== LESSON FLOW ==========
    flow_title = doc.add_paragraph()
    run = flow_title.add_run("Lesson Flow & Timing")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    doc.add_paragraph()

    flow_table = [
        ["Phase", "Time", "What Students Do", "Teacher Role"],
        ["LOCATE", "8-10 min", "Sort components into Internal/External", "Facilitate sorting discussion; ask \"Which can we control?\""],
        ["ESTABLISH", "8-10 min", "Connect components with arrows (+/-)", "Guide with \"When X goes UP, does Y go UP or DOWN?\""],
        ["VISUALIZE & EVALUATE", "10-12 min", "Run simulations, test scenarios, observe graphs", "Let students explore; ask \"What did you notice?\""],
        ["REVISE & EXTEND", "10-15 min", "Research and add new components", "Provide resources; celebrate extensions"],
    ]

    table = doc.add_table(rows=len(flow_table), cols=4)
    table.style = 'Table Grid'

    for i, row_data in enumerate(flow_table):
        for j, cell_text in enumerate(row_data):
            cell = table.rows[i].cells[j]
            cell.text = cell_text
            if i == 0:
                cell.paragraphs[0].runs[0].bold = True
                set_cell_shading(cell, "1A4780")
                cell.paragraphs[0].runs[0].font.color.rgb = DocxRGB(0xFF, 0xFF, 0xFF)

    doc.add_paragraph()

    # ========== ANSWER KEY ==========
    answer_title = doc.add_paragraph()
    run = answer_title.add_run("Answer Key")
    run.bold = True
    run.font.size = DocxPt(18)
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
    doc.add_paragraph("Rainfall --> Dry Vegetation = NEGATIVE (more rain = less dry plants)")
    doc.add_paragraph("Dry Vegetation --> Fire Spread = POSITIVE (more fuel = more fire)")
    doc.add_paragraph("Wind --> Fire Spread = POSITIVE (more wind = fire spreads faster)")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Simulation Results:")
    run.bold = True
    doc.add_paragraph("Drought (Rainfall OFF): Dry Vegetation UP, Fire Spread UP")
    doc.add_paragraph("Windy (Wind ON): Fire Spread UP significantly")
    doc.add_paragraph("Fire Season (both): Maximum fire risk - this is California fall!")

    doc.add_page_break()

    # ========== STEM CHALLENGE TEACHER GUIDANCE ==========
    stem_title = doc.add_paragraph()
    run = stem_title.add_run("STEM Challenge: Teacher Guidance")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    subtitle = doc.add_paragraph()
    run = subtitle.add_run("Firebreak Engineers")
    run.bold = True
    run.font.size = DocxPt(18)
    run.font.color.rgb = DOCX_BRAND_BLUE

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Purpose of This Challenge:")
    run.bold = True
    run.font.size = DocxPt(12)

    doc.add_paragraph("This STEM challenge extends students' model understanding into real-world engineering application. Students apply their knowledge that DRY VEGETATION is the fuel for fire spread by designing firebreaks - areas where vegetation is removed to stop fire progression.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Connection to the Model:")
    run.bold = True
    run.font.size = DocxPt(12)

    doc.add_paragraph("In their ModelIt simulation, students saw that reducing Dry Vegetation reduces Fire Spread. Firebreaks are the real-world application of this relationship. Engineers and land managers create firebreaks to protect communities by interrupting the fuel chain.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("How to Introduce This Challenge:")
    run.bold = True
    run.font.size = DocxPt(14)
    run.font.color.rgb = DOCX_BRAND_BLUE

    intro_script = """
Say to students:

\"You've just discovered something important in your model - that DRY VEGETATION is the FUEL that makes fires spread. Real firefighters and land managers use this exact knowledge every day!

They create something called FIREBREAKS - areas where they remove all the vegetation so fire has nothing to burn. It's like creating a wall of 'no fuel' that fire can't cross.

Now YOU are going to become Firebreak Engineers. A small town called Willow Creek needs your help. Fire season is coming, and they need you to design where to put firebreaks to protect their community.

Here's the challenge: You only have enough budget for THREE firebreaks. Where will you put them to give the town the BEST protection?

Think about what you learned in your model. Think about wind direction. Think about where fire would come from. Then design your solution!\"
"""
    doc.add_paragraph(intro_script)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Materials Needed:")
    run.bold = True
    run.font.size = DocxPt(12)

    doc.add_paragraph("- Paper (regular copy paper works fine)")
    doc.add_paragraph("- Pencils/markers")
    doc.add_paragraph("- That's it! This is designed as a NO-PREP challenge.")

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Facilitation Tips:")
    run.bold = True
    run.font.size = DocxPt(12)

    tips = [
        "Let students work in pairs or small groups for richer discussion",
        "Don't give away the \"right\" answer - there are multiple good solutions!",
        "Ask probing questions: \"Why did you put that firebreak there?\" \"What about the wind direction?\"",
        "Encourage students to reference their MODEL when explaining their design",
        "Have groups share and compare designs at the end - celebrate different solutions",
    ]
    for tip in tips:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(tip)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Key Concepts Students Should Apply:")
    run.bold = True
    run.font.size = DocxPt(12)

    concepts = [
        "Wind direction matters - Santa Ana winds come from the east in California",
        "Fire spreads uphill faster than downhill",
        "Firebreaks should be BETWEEN the fire source and what you're protecting",
        "Reducing fuel (dry vegetation) reduces fire spread - directly from their model!",
    ]
    for c in concepts:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(c)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Extension Opportunity:")
    run.bold = True
    run.font.size = DocxPt(12)

    doc.add_paragraph("After the design challenge, have students return to ModelIt and ADD \"Firebreaks\" as a new component with a NEGATIVE relationship to Fire Spread. Run the simulation to see how firebreaks affect the system!")

    doc.add_page_break()

    # ========== DIFFERENTIATION ==========
    diff_title = doc.add_paragraph()
    run = diff_title.add_run("Differentiation Strategies")
    run.bold = True
    run.font.size = DocxPt(24)
    run.font.color.rgb = DOCX_NAVY

    diff_data = [
        ("Support", [
            "Pre-label some relationships on the recording page",
            "Provide sentence starters for explanations",
            "Pair with stronger partner for simulation analysis",
            "Use visual cues (color-coded arrows) for +/- relationships",
        ]),
        ("Challenge", [
            "Add 3+ research components to the model",
            "Calculate fire risk percentages from simulation data",
            "Research real California fire data and compare to model predictions",
            "Create a presentation explaining their extended model",
        ]),
        ("English Language Learners", [
            "Provide visual vocabulary cards for key terms",
            "Pair with English-proficient partner",
            "Allow drawing/labeling instead of written explanations",
            "Use home language for initial brainstorming",
        ]),
    ]

    for category, strategies in diff_data:
        p = doc.add_paragraph()
        run = p.add_run(category)
        run.bold = True
        run.font.size = DocxPt(14)
        run.font.color.rgb = DOCX_BRAND_BLUE

        for s in strategies:
            p = doc.add_paragraph(style='List Bullet')
            p.add_run(s)

        doc.add_paragraph()

    # ========== COMMON MISCONCEPTIONS ==========
    misc_title = doc.add_paragraph()
    run = misc_title.add_run("Common Misconceptions")
    run.bold = True
    run.font.size = DocxPt(18)
    run.font.color.rgb = DOCX_NAVY

    misconceptions = [
        ("\"Fires are caused by bad people starting them\"",
         "While many fires are human-caused (campfires, equipment sparks), the CONDITIONS must be right for fire to spread. Without dry fuel and wind, a spark won't become a wildfire. Help students understand it's the SYSTEM that creates fire risk."),
        ("\"More firefighters would prevent fires\"",
         "Firefighters RESPOND to fires but can't change the underlying conditions (drought, dry vegetation, wind). This lesson helps students understand that fire risk is determined by Earth systems, not just human response."),
        ("\"Climate doesn't affect fires\"",
         "Fire season has lengthened significantly due to changing climate patterns. Warmer temperatures and shifting rainfall patterns directly affect vegetation dryness. The model helps students see this cause-effect chain."),
    ]

    for misconception, response in misconceptions:
        p = doc.add_paragraph()
        run = p.add_run(misconception)
        run.bold = True
        run.italic = True
        doc.add_paragraph(response)
        doc.add_paragraph()

    # ========== DISCUSSION PROMPTS ==========
    disc_title = doc.add_paragraph()
    run = disc_title.add_run("Discussion Prompts")
    run.bold = True
    run.font.size = DocxPt(18)
    run.font.color.rgb = DOCX_NAVY

    prompts = [
        "\"Why does California burn at the same time every year?\"",
        "\"What would need to change to prevent these fires?\"",
        "\"How is this connected to the water cycle?\"",
        "\"If you were a firefighter, where would you position BEFORE fire season?\"",
        "\"What could communities do to reduce fire risk?\"",
    ]
    for prompt in prompts:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(prompt)

    doc.save(output_path)
    print(f"[OK] Created: {output_path}")
    return output_path


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    ensure_output_dir()
    print("\n" + "=" * 60)
    print("ModelIt! Lesson Materials Generator v2")
    print(f"{LESSON_ID}: {LESSON_TITLE}")
    print("=" * 60 + "\n")

    ppt_path = create_powerpoint()
    activity_path = create_student_activity_pack()
    guide_path = create_teachers_guide()

    print("\n" + "=" * 60)
    print("All materials created!")
    print(f"Location: {OUTPUT_DIR}")
    print("=" * 60)
    print("\nFiles created:")
    print(f"  - {LESSON_ID}-Student-Presentation.pptx")
    print(f"  - {LESSON_ID}-Student-Activity-Pack.docx")
    print(f"  - {LESSON_ID}-Teachers-Guide.docx")
    print("\nImage placeholders included - ready for your visual API!")
