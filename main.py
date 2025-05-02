import os
import streamlit as st
from utils.ocr import ocr_pdf
from utils.summarizer import summarize_text

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    st.title("📄 PDF OCR and Summarizer (Mistral API)")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.info("Running OCR...")
        text = ocr_pdf(file_path)
        st.success("OCR completed.")

        extracted_text_path = os.path.join(OUTPUT_DIR, "extracted_text.txt")
        with open(extracted_text_path, "w", encoding="utf-8") as f:
            f.write(text)

        st.text_area("Extracted Text", text, height=300)
        st.download_button("Download Extracted Text", data=text, file_name="extracted_text.txt")

        if st.button("Summarize"):
            st.info("Generating summary...")
            summary = summarize_text(text)

            summary_path = os.path.join(OUTPUT_DIR, "summary.txt")
            with open(summary_path, "w", encoding="utf-8") as f:
                f.write(summary)

            st.success("Summary ready.")
            st.text_area("Summary", summary, height=200)
            st.download_button("Download Summary", data=summary, file_name="summary.txt")

if __name__ == "__main__":
    main()
