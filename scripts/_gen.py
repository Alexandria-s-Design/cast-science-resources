import os
OUT = r"C:/Users/ginja/cast-science-resources/scripts/create_all_lessons_L02_L10.py"
lines = []

def w(*args):
    lines.extend(args)

w(
    "#!/usr/bin/env python3",
    "# ModelIt! Batch Lesson Materials Generator G05-L02 through G05-L10",
    "",
    "from pptx import Presentation",
    "from pptx.util import Inches, Pt",
    "from pptx.dml.color import RGBColor",
    "from pptx.enum.text import PP_ALIGN, MSO_ANCHOR",
    "from pptx.enum.shapes import MSO_SHAPE",
    "from docx import Document",
    "from docx.shared import Inches as DocxInches, Pt as DocxPt, RGBColor as DocxRGB, Cm",
    "from docx.enum.text import WD_ALIGN_PARAGRAPH",
    "from docx.enum.table import WD_TABLE_ALIGNMENT",
    "from docx.oxml.ns import qn",
    "from docx.oxml import OxmlElement",
    "import requests, base64, os, time",
    "from PIL import Image",
    "",
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write("
".join(lines))
print(f"Done: {os.path.getsize(OUT)} bytes")
