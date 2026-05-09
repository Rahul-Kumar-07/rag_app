from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    TextLoader,
    Docx2txtLoader
)

from langchain_core.documents import Document

from utils.ocr import extract_text_from_image

SUPPORTED_IMAGES = [".png", ".jpg", ".jpeg"]

def load_file(path: str):

    if path.endswith(".pdf"):
        return PyPDFLoader(path).load()

    elif path.endswith(".csv"):
        return CSVLoader(path).load()

    elif path.endswith(".txt"):
        return TextLoader(path).load()

    elif path.endswith(".docx"):
        return Docx2txtLoader(path).load()

    elif any(path.endswith(ext) for ext in SUPPORTED_IMAGES):
        text = extract_text_from_image(path)

        return [
            Document(
                page_content=text,
                metadata={"source": path}
            )
        ]

    else:
        raise ValueError(f"Unsupported file type: {path}")