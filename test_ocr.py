# test_ocr.py
from utils.ocr import ocr_pdf

if __name__ == "__main__":
    sample_pdf = "C:/Users/abhig/Downloads/Documents/IA32.pdf"  # Make sure this PDF exists in the project directory
    try:
        result = ocr_pdf(sample_pdf)
        print("OCR completed successfully.")
        print("Extracted text preview:\n", result[:1000])  # print first 1000 chars
        with open("test_output.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("Output written to test_output.txt")
    except Exception as e:
        print("Error during OCR:", e)
