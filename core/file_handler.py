import os
import PyPDF2
from docx import Document
from PIL import Image
import pytesseract
import cv2

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return extract_txt(file_path)

    elif ext == ".pdf":
        return extract_pdf(file_path)

    elif ext == ".docx":
        return extract_docx(file_path)

    elif ext in [".png", ".jpg", ".jpeg"]:
        return extract_image(file_path)

    else:
        raise ValueError("Unsupported file format")


def extract_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def extract_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_image(path):
    img = cv2.imread(path)
    text = pytesseract.image_to_string(img)
    return text
