from pathlib import Path
from pypdf import PdfReader
from docx import Document

def load_txt(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="ignore")

def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def load_docx(path: str) -> str:
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def load_file(path: str) -> str:
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".txt":
        return load_txt(str(path))
    if suffix == ".pdf":
        return load_pdf(str(path))
    if suffix == ".docx":
        return load_docx(str(path))
    raise ValueError(f"Unsupported file type: {suffix}")
