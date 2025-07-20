# app/pdf_loader.py

import os
import fitz  # PyMuPDF
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFLoader:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def load_pdf_text(self, pdf_path: str) -> str:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def load_and_chunk(self, folder_path: str) -> List[dict]:
        chunks = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf"):
                full_path = os.path.join(folder_path, filename)
                text = self.load_pdf_text(full_path)
                split_texts = self.splitter.split_text(text)
                for i, chunk in enumerate(split_texts):
                    chunks.append({
                        "content": chunk,
                        "source": filename,
                        "chunk_id": i
                    })
        return chunks
