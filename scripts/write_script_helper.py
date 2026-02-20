# Helper script to write the main lesson generator
import os

OUTPUT = r"C:\Users\ginja\cast-science-resources\scripts\create_all_lessons_L02_L10.py"

script = ''

# ============================================================
# PART 1: Header and imports
# ============================================================
script += '''"""
ModelIt Lesson Materials Generator - Batch Version
Creates PowerPoint, Student Activity Pack (Word), and Teacher's Guide (Word)
for G05-L02 through G05-L10 with AI-generated images via OpenRouter API.

Based on create_lesson_materials.py (G05-L01 generator).
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from docx import Document
from docx.shared import Inches as DocxInches, Pt as DocxPt, RGBColor as DocxRGB, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import requests
import base64
import os
import sys
import time
from PIL import Image

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
ACCENT_ORANGE = RGBColor(0xE6, 0x7E, 0x22)

DOCX_NAVY = DocxRGB(0x0D, 0x1B, 0x2A)
DOCX_BRAND_BLUE = DocxRGB(0x1A, 0x47, 0x80)
DOCX_MID_BLUE = DocxRGB(0x2E, 0x86, 0xAB)
DOCX_LIGHT_BLUE = DocxRGB(0x7E, 0xC8, 0xE3)
DOCX_ORANGE = DocxRGB(0xE6, 0x7E, 0x22)

OPENROUTER_API_KEY = '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'
AGE_RANGE = '10-11 years old'
GRADE_LEVEL = '5th Grade'

total_image_cost = 0.0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'materials', 'grade-05')

'''

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(script)

print("Part 1 written successfully")
