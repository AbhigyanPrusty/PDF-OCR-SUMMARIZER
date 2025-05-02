import pytesseract
from pdf2image import convert_from_path
import re

# Set the path to your Tesseract installation (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set the path to your Poppler installation (adjust if needed)
POPPLER_PATH = r"C:\Program Files\Poppler\poppler-24.08.0\Library\bin"

def clean_text(text):
    # Remove non-ASCII characters and collapse multiple spaces
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def ocr_pdf(pdf_path):
    from pdf2image import pdfinfo_from_path
    info = pdfinfo_from_path(pdf_path, poppler_path=POPPLER_PATH)
    total_pages = info.get("Pages", 1)

    full_text = ""
    for i in range(1, total_pages + 1):
        pages = convert_from_path(pdf_path, dpi=200, first_page=i, last_page=i, poppler_path=POPPLER_PATH)
        raw_text = pytesseract.image_to_string(pages[0])
        cleaned_text = clean_text(raw_text)
        full_text += f"\n--- Page {i} ---\n{cleaned_text}"

    return full_text
