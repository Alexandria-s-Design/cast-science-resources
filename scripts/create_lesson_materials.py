"""
ModelIt Lesson Materials Generator
Creates PowerPoint, Student Worksheets, and Teacher's Guide
for the California Wildfires lesson (G05-L01)
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

# Brand Colors
BRAND_BLUE_DARK = RGBColor(0x1A, 0x47, 0x80)  # Deep scientific blue
BRAND_BLUE_MID = RGBColor(0x2E, 0x86, 0xAB)   # Cell membrane blue
BRAND_BLUE_LIGHT = RGBColor(0x7E, 0xC8, 0xE3) # Light accent
BRAND_NAVY = RGBColor(0x0D, 0x1B, 0x2A)       # Dark text
BRAND_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Hex versions for PDF
HEX_BLUE_DARK = HexColor('#1A4780')
HEX_BLUE_MID = HexColor('#2E86AB')
HEX_BLUE_LIGHT = HexColor('#7EC8E3')
HEX_NAVY = HexColor('#0D1B2A')

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'materials', 'G05-L01')

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================
# POWERPOINT CREATION
# ============================================

def add_title_slide(prs, title, subtitle=""):
    """Add a title slide with blue gradient feel"""
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)

    # Background shape
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BRAND_BLUE_DARK
    bg.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = BRAND_WHITE
    p.alignment = PP_ALIGN.CENTER

    # Subtitle
    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.5), Inches(4), Inches(9), Inches(1))
        tf = sub_box.text_frame
        p = tf.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(24)
        p.font.color.rgb = BRAND_BLUE_LIGHT
        p.alignment = PP_ALIGN.CENTER

    # ModelIt branding
    brand_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(9), Inches(0.5))
    tf = brand_box.text_frame
    p = tf.paragraphs[0]
    p.text = "ModelIt | Systems Thinking for K-12"
    p.font.size = Pt(14)
    p.font.color.rgb = BRAND_BLUE_LIGHT
    p.alignment = PP_ALIGN.CENTER

    return slide

def add_content_slide(prs, title, bullets, accent_color=BRAND_BLUE_MID):
    """Add a content slide with bullet points"""
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)

    # Accent bar on left
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.15), prs.slide_height)
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent_color
    bar.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = BRAND_NAVY

    # Bullets
    content_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.3), Inches(8.8), Inches(5))
    tf = content_box.text_frame
    tf.word_wrap = True

    for i, bullet in enumerate(bullets):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"• {bullet}"
        p.font.size = Pt(22)
        p.font.color.rgb = BRAND_NAVY
        p.space_after = Pt(12)

    # Footer
    footer = slide.shapes.add_textbox(Inches(0.5), Inches(6.8), Inches(4), Inches(0.3))
    tf = footer.text_frame
    p = tf.paragraphs[0]
    p.text = "ModelIt | G05-L01"
    p.font.size = Pt(10)
    p.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    return slide

def add_question_slide(prs, question, visual_desc=""):
    """Add a driving question slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BRAND_BLUE_MID
    bg.line.fill.background()

    # Question mark accent
    q_box = slide.shapes.add_textbox(Inches(0.3), Inches(0.3), Inches(1), Inches(1.5))
    tf = q_box.text_frame
    p = tf.paragraphs[0]
    p.text = "?"
    p.font.size = Pt(80)
    p.font.bold = True
    p.font.color.rgb = BRAND_BLUE_LIGHT

    # Question text
    q_text = slide.shapes.add_textbox(Inches(0.5), Inches(2.2), Inches(9), Inches(2))
    tf = q_text.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = question
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = BRAND_WHITE
    p.alignment = PP_ALIGN.CENTER

    if visual_desc:
        desc_box = slide.shapes.add_textbox(Inches(1), Inches(5), Inches(8), Inches(1))
        tf = desc_box.text_frame
        p = tf.paragraphs[0]
        p.text = f"[{visual_desc}]"
        p.font.size = Pt(14)
        p.font.italic = True
        p.font.color.rgb = BRAND_BLUE_LIGHT
        p.alignment = PP_ALIGN.CENTER

    return slide

def add_activity_slide(prs, activity_num, activity_name, steps):
    """Add an activity instruction slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Activity number badge
    badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.3), Inches(0.3), Inches(0.8), Inches(0.8))
    badge.fill.solid()
    badge.fill.fore_color.rgb = BRAND_BLUE_DARK
    badge.line.fill.background()

    badge_text = slide.shapes.add_textbox(Inches(0.3), Inches(0.45), Inches(0.8), Inches(0.5))
    tf = badge_text.text_frame
    p = tf.paragraphs[0]
    p.text = str(activity_num)
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = BRAND_WHITE
    p.alignment = PP_ALIGN.CENTER

    # Activity name
    title_box = slide.shapes.add_textbox(Inches(1.3), Inches(0.35), Inches(8), Inches(0.7))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = activity_name
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = BRAND_NAVY

    # Steps
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.4), Inches(9), Inches(5))
    tf = content_box.text_frame
    tf.word_wrap = True

    for i, step in enumerate(steps):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = step
        p.font.size = Pt(20)
        p.font.color.rgb = BRAND_NAVY
        p.space_after = Pt(10)

    return slide

def add_diagram_slide(prs, title, description):
    """Add a slide for diagrams/visuals"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = BRAND_NAVY

    # Placeholder box for diagram
    diagram_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.2), Inches(8.5), Inches(4.5))
    diagram_box.fill.solid()
    diagram_box.fill.fore_color.rgb = RGBColor(0xF5, 0xF9, 0xFC)
    diagram_box.line.color.rgb = BRAND_BLUE_LIGHT
    diagram_box.line.width = Pt(2)

    # Description text
    desc_box = slide.shapes.add_textbox(Inches(1), Inches(2.8), Inches(8), Inches(1.5))
    tf = desc_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"[{description}]"
    p.font.size = Pt(18)
    p.font.italic = True
    p.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p.alignment = PP_ALIGN.CENTER

    return slide

def create_powerpoint():
    """Create the full student PowerPoint"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1: Title
    add_title_slide(prs,
        "When Trees Become Matches",
        "California burns every year. It's not bad luck — it's science.")

    # Slide 2: The Mystery
    add_question_slide(prs,
        "Same state. Same trees.\nEvery single year. Why?",
        "Split image: Beautiful California forest / Same forest on fire")

    # Slide 3: Driving Question
    add_question_slide(prs,
        "How do Earth's systems work together\nto create perfect fire conditions?",
        "Icons: Atmosphere + Biosphere + Hydrosphere = Fire")

    # Slide 4: What We're Building
    add_content_slide(prs, "What We're Building Today", [
        "A cause-and-effect MODEL of wildfire conditions",
        "Discover how Earth's systems connect",
        "Predict what happens when conditions change",
        "Think like a Wildfire Data Scientist"
    ])

    # Slide 5: Components Introduction
    add_content_slide(prs, "The Parts of Our Fire System", [
        "EXTERNAL — things we CAN'T control",
        "    Rainfall (weather decides)",
        "    Wind (nature decides)",
        "INTERNAL — things that CHANGE based on other things",
        "    Dry Vegetation (changes based on rain)",
        "    Fire Spread (what we're trying to understand)"
    ])

    # Slide 6: Activity 1
    add_activity_slide(prs, 1, "LOCATE — Build Your Fire System", [
        "STEP 1: Look at the components in ModelIt",
        "STEP 2: SORT them — which are External? Which are Internal?",
        "STEP 3: Click the PLUS (+) button to add each component",
        "STEP 4: You should have 4 components on your canvas",
        "",
        "Your teacher will show you how to sort in the video!"
    ])

    # Slide 7: Activity 2
    add_activity_slide(prs, 2, "ESTABLISH — Connect the Relationships", [
        "STEP 1: Click the CONNECT icon (top left)",
        "STEP 2: Draw arrows between related components:",
        "    • Rainfall → Dry Vegetation",
        "    • Dry Vegetation → Fire Spread",
        "    • Wind → Fire Spread",
        "STEP 3: Set each connection as + (positive) or − (negative)",
        "",
        "Ask yourself: When THIS goes up, does THAT go up or down?"
    ])

    # Slide 8: Relationships Diagram
    add_diagram_slide(prs,
        "The Chain Reaction",
        "Diagram: Rainfall —(−)→ Dry Vegetation —(+)→ Fire Spread ←(+)— Wind\n\nWhen rain STOPS, the dominoes fall toward FIRE")

    # Slide 9: Activity 3
    add_activity_slide(prs, 3, "VISUALIZE — Run Your Fire Model", [
        "STEP 1: Click the PLAY button (top left)",
        "STEP 2: Watch the graph — see how components change",
        "STEP 3: CREATE A DROUGHT:",
        "    • Find the LOCK icon next to Rainfall",
        "    • Lock Rainfall to OFF (0%)",
        "STEP 4: Watch what happens to Dry Vegetation and Fire Spread",
        "STEP 5: Lock WIND to ON (100%) — Santa Ana winds!"
    ])

    # Slide 10: What The Graph Shows
    add_diagram_slide(prs,
        "Reading Your Simulation",
        "Graph showing: Rainfall at 0% → Dry Vegetation climbing → Fire Spread climbing\n\nYou just simulated California's fire season!")

    # Slide 11: Activity 4
    add_activity_slide(prs, 4, "EXTEND — Play, Research, Expand", [
        "PLAY TIME! Experiment with your model:",
        "    • What if rain comes back? How fast does the system recover?",
        "    • What combination creates the WORST fire conditions?",
        "",
        "RESEARCH: What's MISSING from your model?",
        "    • Temperature / Heat waves?",
        "    • Humans (campfires, power lines)?",
        "    • Firefighters?",
        "",
        "ADD one new component based on your research!"
    ])

    # Slide 12: Earth Systems Connection
    add_content_slide(prs, "Earth Systems Working Together", [
        "ATMOSPHERE — weather, wind, temperature",
        "BIOSPHERE — plants, trees, vegetation",
        "HYDROSPHERE — rain, drought, water cycle",
        "",
        "Wildfires happen where all three OVERLAP",
        "Your model shows how they CONNECT"
    ])

    # Slide 13: Career Connection
    add_content_slide(prs, "Career Connection: Wildfire Data Scientist", [
        "Builds computer models just like yours — but BIGGER",
        "Predicts where fires will start BEFORE they happen",
        "Analyzes weather, vegetation, wind, and climate data",
        "Helps position firefighters and warn communities",
        "",
        "SALARY: $95,000 - $150,000+ per year",
        "",
        "Your simple fire model? That's step one toward this career."
    ], accent_color=RGBColor(0xE6, 0x55, 0x00))  # Orange accent for career

    # Slide 14: Reflection
    add_question_slide(prs,
        "What story does YOUR model tell?",
        "Think-Pair-Share: Explain your model to a partner")

    # Save
    output_path = os.path.join(OUTPUT_DIR, 'G05-L01-Student-Presentation.pptx')
    prs.save(output_path)
    print(f"Created: {output_path}")
    return output_path

# ============================================
# WORKSHEET PDF CREATION (Black & White)
# ============================================

class WorksheetPDF:
    def __init__(self, filename):
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=letter)
        self.width, self.height = letter
        self.margin = 0.75 * inch
        self.y = self.height - self.margin
        self.page_num = 1

    def add_header(self, title="When Trees Become Matches"):
        """Add header with name/date lines"""
        # Title
        self.c.setFont("Helvetica-Bold", 16)
        self.c.drawString(self.margin, self.y, f"ModelIt | {title}")
        self.y -= 20

        # Name and Date lines
        self.c.setFont("Helvetica", 10)
        self.c.drawString(self.margin, self.y, "Name: _______________________________")
        self.c.drawString(self.margin + 280, self.y, "Date: _______________")
        self.y -= 8

        # Line under header
        self.c.setStrokeColor(black)
        self.c.setLineWidth(1)
        self.c.line(self.margin, self.y, self.width - self.margin, self.y)
        self.y -= 20

    def add_footer(self):
        """Add footer with page number"""
        self.c.setFont("Helvetica", 8)
        self.c.setFillColor(gray)
        self.c.drawString(self.margin, 0.5 * inch, f"G05-L01 | Page {self.page_num}")
        self.c.drawRightString(self.width - self.margin, 0.5 * inch, "ModelIt | Systems Thinking for K-12")
        self.c.setFillColor(black)

    def add_section_title(self, title):
        """Add a section title"""
        if self.y < 1.5 * inch:
            self.new_page()
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(self.margin, self.y, title)
        self.y -= 8
        self.c.setLineWidth(0.5)
        self.c.line(self.margin, self.y, self.margin + 200, self.y)
        self.y -= 18

    def add_text(self, text, bold=False, indent=0):
        """Add a line of text"""
        if self.y < 1 * inch:
            self.new_page()
        font = "Helvetica-Bold" if bold else "Helvetica"
        self.c.setFont(font, 11)
        self.c.drawString(self.margin + indent, self.y, text)
        self.y -= 16

    def add_line(self, label="", width=400):
        """Add a fill-in line"""
        if self.y < 1 * inch:
            self.new_page()
        self.c.setFont("Helvetica", 11)
        if label:
            self.c.drawString(self.margin, self.y, label)
            line_start = self.margin + self.c.stringWidth(label, "Helvetica", 11) + 5
        else:
            line_start = self.margin
        self.c.line(line_start, self.y - 2, self.margin + width, self.y - 2)
        self.y -= 22

    def add_lines(self, count=3, width=450):
        """Add multiple blank lines"""
        for _ in range(count):
            if self.y < 1 * inch:
                self.new_page()
            self.c.line(self.margin, self.y, self.margin + width, self.y)
            self.y -= 22

    def add_box(self, height=100, label=""):
        """Add a drawing/answer box"""
        if self.y < height/72 + 1 * inch:
            self.new_page()
        box_top = self.y
        self.c.setStrokeColor(black)
        self.c.setLineWidth(1)
        self.c.rect(self.margin, self.y - height, self.width - 2*self.margin, height)
        if label:
            self.c.setFont("Helvetica-Oblique", 9)
            self.c.setFillColor(gray)
            self.c.drawString(self.margin + 5, self.y - 12, label)
            self.c.setFillColor(black)
        self.y -= height + 15

    def add_checkbox_item(self, text):
        """Add a checkbox item"""
        if self.y < 1 * inch:
            self.new_page()
        self.c.rect(self.margin, self.y - 10, 12, 12)
        self.c.setFont("Helvetica", 11)
        self.c.drawString(self.margin + 18, self.y - 8, text)
        self.y -= 20

    def add_circle_options(self, options):
        """Add circle-able options"""
        if self.y < 1 * inch:
            self.new_page()
        self.c.setFont("Helvetica", 11)
        x = self.margin
        for opt in options:
            self.c.drawString(x, self.y, opt)
            x += self.c.stringWidth(opt, "Helvetica", 11) + 30
        self.y -= 20

    def add_space(self, points=15):
        """Add vertical space"""
        self.y -= points

    def new_page(self):
        """Start a new page"""
        self.add_footer()
        self.c.showPage()
        self.page_num += 1
        self.y = self.height - self.margin
        self.add_header()

    def save(self):
        """Save the PDF"""
        self.add_footer()
        self.c.save()
        print(f"Created: {self.filename}")

def create_worksheets():
    """Create the student worksheet packet (B&W)"""
    output_path = os.path.join(OUTPUT_DIR, 'G05-L01-Student-Worksheets.pdf')
    pdf = WorksheetPDF(output_path)

    # Page 1: Vocabulary
    pdf.add_header()
    pdf.add_section_title("VOCABULARY")
    pdf.add_text("Match the term to the definition:")
    pdf.add_space(10)
    pdf.add_text("_____ Drought", indent=20)
    pdf.add_text("_____ Atmosphere", indent=20)
    pdf.add_text("_____ Biosphere", indent=20)
    pdf.add_text("_____ Vegetation", indent=20)
    pdf.add_text("_____ Hydrosphere", indent=20)
    pdf.add_space(10)
    pdf.add_text("A. Living things (plants, animals)", indent=40)
    pdf.add_text("B. Long period without rainfall", indent=40)
    pdf.add_text("C. The air and weather around Earth", indent=40)
    pdf.add_text("D. All the water on Earth", indent=40)
    pdf.add_text("E. Plants and trees", indent=40)

    pdf.add_space(20)
    pdf.add_section_title("MODEL PLANNING")
    pdf.add_text("Before you build in ModelIt, sort your components:")
    pdf.add_space(10)
    pdf.add_text("EXTERNAL (things we can't control):", bold=True)
    pdf.add_lines(2, 350)
    pdf.add_space(5)
    pdf.add_text("INTERNAL (things that change because of other things):", bold=True)
    pdf.add_lines(2, 350)

    # Page 2: Activity Observations
    pdf.new_page()
    pdf.add_section_title("ACTIVITY 1: LOCATE")
    pdf.add_text("List the 4 components you added to your model:")
    pdf.add_text("1. ________________________________", indent=20)
    pdf.add_text("2. ________________________________", indent=20)
    pdf.add_text("3. ________________________________", indent=20)
    pdf.add_text("4. ________________________________", indent=20)

    pdf.add_space(15)
    pdf.add_section_title("ACTIVITY 2: ESTABLISH")
    pdf.add_text("Draw your model below. Show arrows and label each + or −")
    pdf.add_box(150, "Draw your model here")

    pdf.add_text("Explain ONE relationship in your own words:")
    pdf.add_lines(3)

    # Page 3: Simulation Observations
    pdf.new_page()
    pdf.add_section_title("ACTIVITY 3: VISUALIZE")
    pdf.add_text("SIMULATION OBSERVATIONS", bold=True)
    pdf.add_space(10)

    pdf.add_text("When I turned OFF Rainfall (drought), this happened:")
    pdf.add_text("• Dry Vegetation:    went UP  /  went DOWN  /  stayed same", indent=20)
    pdf.add_text("• Fire Spread:       went UP  /  went DOWN  /  stayed same", indent=20)
    pdf.add_space(10)

    pdf.add_text("When I turned ON Wind, this happened:")
    pdf.add_text("• Fire Spread:       went UP  /  went DOWN  /  stayed same", indent=20)
    pdf.add_space(10)

    pdf.add_text("The WORST fire conditions in my model are when:")
    pdf.add_lines(2)

    pdf.add_space(15)
    pdf.add_text("Sketch what your graph looked like:", bold=True)
    pdf.add_box(120, "Sketch graph here")

    # Page 4: Research & Extend
    pdf.new_page()
    pdf.add_section_title("ACTIVITY 4: EXTEND")
    pdf.add_text("RESEARCH & EXTEND", bold=True)
    pdf.add_space(10)

    pdf.add_line("NEW COMPONENT I want to add: ")
    pdf.add_space(5)
    pdf.add_text("Is it EXTERNAL or INTERNAL? (circle one)")
    pdf.add_space(5)
    pdf.add_line("What does it connect to? ")
    pdf.add_space(5)
    pdf.add_text("Is the relationship POSITIVE (+) or NEGATIVE (−)? _____")
    pdf.add_space(5)
    pdf.add_text("Why?")
    pdf.add_lines(2)

    pdf.add_space(10)
    pdf.add_text("After adding it, my simulation showed:")
    pdf.add_lines(3)

    pdf.add_space(15)
    pdf.add_section_title("REFLECTION")
    pdf.add_text("Explain, in your own words, why California has wildfires every year:")
    pdf.add_lines(4)

    pdf.add_text("Which Earth systems interact to create fire conditions? (circle all)")
    pdf.add_space(5)
    pdf.add_text("ATMOSPHERE      BIOSPHERE      HYDROSPHERE      GEOSPHERE", indent=40)

    pdf.save()
    return output_path

# ============================================
# TEACHER'S GUIDE PDF (Color)
# ============================================

def create_teachers_guide():
    """Create the teacher's guide (Color PDF)"""
    output_path = os.path.join(OUTPUT_DIR, 'G05-L01-Teachers-Guide.pdf')

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        textColor=HEX_BLUE_DARK,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=HEX_BLUE_DARK,
        spaceBefore=15,
        spaceAfter=8,
        borderColor=HEX_BLUE_LIGHT,
        borderWidth=0,
        borderPadding=5
    )

    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=HEX_BLUE_MID,
        spaceBefore=10,
        spaceAfter=5
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leading=14
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=4
    )

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    story = []

    # Title
    story.append(Paragraph("Teacher's Guide", title_style))
    story.append(Paragraph("G05-L01: When Trees Become Matches", heading_style))
    story.append(Paragraph("California's Burning Season and the Earth Systems That Fuel It", body_style))
    story.append(Spacer(1, 20))

    # Overview Table
    overview_data = [
        ['Grade', '5th'],
        ['NGSS Standard', '5-ESS2-1'],
        ['Time', '40-45 minutes (or split across 2 days)'],
        ['Materials', 'Student devices with ModelIt access'],
    ]
    overview_table = Table(overview_data, colWidths=[1.5*inch, 4.5*inch])
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), HEX_BLUE_LIGHT),
        ('TEXTCOLOR', (0, 0), (0, -1), HEX_NAVY),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BLUE_MID),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 20))

    # Lesson Purpose
    story.append(Paragraph("LESSON PURPOSE", heading_style))
    story.append(Paragraph(
        "This lesson serves as a <b>HOOK</b> for Earth systems inquiry. Students build a simple "
        "cause-and-effect model, then identify gaps that drive further research. It's designed "
        "to drop into existing curriculum with minimal prep.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Learning Objectives
    story.append(Paragraph("LEARNING OBJECTIVES", heading_style))
    objectives = [
        "Model how lack of rainfall affects vegetation",
        "Trace cause-and-effect relationships between drought and fire conditions",
        "Explain how Earth systems (atmosphere, biosphere, hydrosphere) interact",
        "Predict what happens when one part of the system changes"
    ]
    for obj in objectives:
        story.append(Paragraph(f"• {obj}", bullet_style))
    story.append(Spacer(1, 10))

    # Pacing Guide
    story.append(Paragraph("PACING GUIDE", heading_style))
    pacing_data = [
        ['Activity', 'LEVER Phase', 'Time'],
        ['Activity 1: Build Your Fire System', 'LOCATE', '8-10 min'],
        ['Activity 2: Connect the Relationships', 'ESTABLISH', '8-10 min'],
        ['Activity 3: Run Your Fire Model', 'VISUALIZE & EVALUATE', '10-12 min'],
        ['Activity 4: Play, Research, Expand', 'REVISE & EXTEND', '10-15 min'],
    ]
    pacing_table = Table(pacing_data, colWidths=[3*inch, 1.8*inch, 1*inch])
    pacing_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEX_BLUE_DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BLUE_MID),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#F5F9FC')]),
    ]))
    story.append(pacing_table)
    story.append(Spacer(1, 15))

    # Common Misconceptions
    story.append(Paragraph("COMMON MISCONCEPTIONS", heading_style))
    misconceptions = [
        ("<b>\"Fires are caused by bad people\"</b> → Most are human-caused, but conditions must be right. Without dry fuel, fires don't spread.", bullet_style),
        ("<b>\"More firefighters = no fires\"</b> → Firefighters respond, but conditions (drought, wind) determine severity.", bullet_style),
        ("<b>\"Climate doesn't affect fires\"</b> → Fire season has lengthened significantly due to climate patterns.", bullet_style),
    ]
    for m in misconceptions:
        story.append(Paragraph(m[0], m[1]))
    story.append(Spacer(1, 10))

    # Page Break
    story.append(PageBreak())

    # Facilitation Tips
    story.append(Paragraph("FACILITATION TIPS", heading_style))
    story.append(Paragraph("<b>Activity 1:</b> Let students explore the interface. Don't over-explain.", bullet_style))
    story.append(Paragraph("<b>Activity 2:</b> Ask \"When this goes up, what happens to that?\" to guide +/− decisions.", bullet_style))
    story.append(Paragraph("<b>Activity 3:</b> Give time for students to \"break\" the model — turn things on/off. This is where insight happens.", bullet_style))
    story.append(Paragraph("<b>Activity 4:</b> Don't give answers. Ask questions. Let curiosity drive.", bullet_style))
    story.append(Spacer(1, 15))

    # Discussion Prompts
    story.append(Paragraph("DISCUSSION PROMPTS", heading_style))
    prompts = [
        "\"Why does California burn at the same time every year?\"",
        "\"What would need to change to prevent these fires?\"",
        "\"How is this connected to what we learned about the water cycle?\"",
        "\"If you were a firefighter, where would you want to be positioned BEFORE fire season?\""
    ]
    for p in prompts:
        story.append(Paragraph(f"• {p}", bullet_style))
    story.append(Spacer(1, 15))

    # Answer Key
    story.append(Paragraph("ANSWER KEY", heading_style))
    story.append(Paragraph("<b>Vocabulary Matching:</b>", subheading_style))
    story.append(Paragraph("Drought = B, Atmosphere = C, Biosphere = A, Vegetation = E, Hydrosphere = D", body_style))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>Component Sorting:</b>", subheading_style))
    story.append(Paragraph("EXTERNAL: Rainfall, Wind", body_style))
    story.append(Paragraph("INTERNAL: Dry Vegetation, Fire Spread", body_style))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>Relationships:</b>", subheading_style))
    story.append(Paragraph("• Rainfall → Dry Vegetation = NEGATIVE (more rain = less dry plants)", body_style))
    story.append(Paragraph("• Dry Vegetation → Fire Spread = POSITIVE (more fuel = more fire)", body_style))
    story.append(Paragraph("• Wind → Fire Spread = POSITIVE (more wind = fire spreads faster)", body_style))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>Simulation Observations:</b>", subheading_style))
    story.append(Paragraph("When Rainfall OFF: Dry Vegetation goes UP, Fire Spread goes UP", body_style))
    story.append(Paragraph("When Wind ON: Fire Spread goes UP", body_style))
    story.append(Paragraph("Worst conditions: No rain + High wind", body_style))
    story.append(Spacer(1, 15))

    # Differentiation
    story.append(Paragraph("DIFFERENTIATION", heading_style))
    diff_data = [
        ['Support', 'Pre-label relationships; use sentence starters for explanations'],
        ['Challenge', 'Add 3+ components; research actual fire risk percentages'],
        ['ELL', 'Provide visual vocabulary cards; pair with English-proficient partner'],
    ]
    diff_table = Table(diff_data, colWidths=[1.2*inch, 4.8*inch])
    diff_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), HEX_BLUE_LIGHT),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BLUE_MID),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(diff_table)
    story.append(Spacer(1, 15))

    # Extension Connections
    story.append(Paragraph("EXTENSION CONNECTIONS", heading_style))
    story.append(Paragraph("• <b>Water Cycle Unit:</b> Drought as part of larger pattern", bullet_style))
    story.append(Paragraph("• <b>Human Impact:</b> Adding humans/power lines to model", bullet_style))
    story.append(Paragraph("• <b>Climate Change:</b> Researching how fire season has changed over decades", bullet_style))

    # Build PDF
    doc.build(story)
    print(f"Created: {output_path}")
    return output_path

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    ensure_output_dir()
    print("\n" + "="*50)
    print("ModelIt Lesson Materials Generator")
    print("G05-L01: When Trees Become Matches")
    print("="*50 + "\n")

    ppt_path = create_powerpoint()
    worksheet_path = create_worksheets()
    guide_path = create_teachers_guide()

    print("\n" + "="*50)
    print("All materials created successfully!")
    print(f"Location: {OUTPUT_DIR}")
    print("="*50)
