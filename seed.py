# ingest.py

from app.pdf_loader import PDFLoader
from app.vector_store import ingest_chunks

loader = PDFLoader()
chunks = loader.load_and_chunk("docs")
ingest_chunks(chunks)
