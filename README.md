# PDF OCR Summarizer

This project extracts text from scanned PDF documents using OCR (Optical Character Recognition) and summarizes the content using a Hugging Face transformer model.

---

## Features

-  Extracts text from scanned or image-based PDFs using Tesseract OCR
-  Summarizes the extracted text using a Hugging Face NLP model (`distilbart-cnn-12-6`)
-  Environment-based configuration for API keys
-  Modular Python codebase

---

## Requirements

- Python 3.7+
- Tesseract OCR
- Poppler for PDF rendering
- Hugging Face account with a valid API token

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/pdf-ocr-summarizer.git
cd pdf-ocr-summarizer
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Install Tesseract OCR:**

- Download from: https://github.com/tesseract-ocr/tesseract
- Set the Tesseract path in `ocr.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

4. **Install Poppler:**

- Download from: https://blog.alivate.com.au/poppler-windows/
- Set the Poppler path in `ocr.py`:

```python
POPPLER_PATH = r"C:\Program Files\Poppler\poppler-24.08.0\Library\bin"
```

---

## Setup Environment

1. Create a `.env` file:

```env
HUGGINGFACE_API_KEY=your_huggingface_token_here
```

You can get a token from https://huggingface.co/settings/tokens

---

## Running the Project

1. Place a scanned or image-based PDF inside the project folder (e.g., `document.pdf`).

2. Modify `main.py` (or use a script) to run:

```python
from ocr import ocr_pdf
from summarizer import summarize_text

text = ocr_pdf("document.pdf")
summary = summarize_text(text)
print(summary)
```

---

## Running Tests

```bash
python test_summarizer.py
```

---

## Model Used

- `sshleifer/distilbart-cnn-12-6` — a smaller and faster version of BART trained for summarization tasks.

---

## Notes

- The Hugging Face free tier includes limited inference tokens per month.
- Large PDFs might be truncated due to model input limits (e.g., 1024 tokens).
- OCR accuracy depends on PDF quality and resolution.

---
