# app/vector_store.py

from typing import List
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

import os
from dotenv import load_dotenv
load_dotenv()

COLLECTION_NAME = "doc_chunks"

client = QdrantClient(url=os.getenv("QDRANT_HOST", "http://localhost:6333"))

def init_collection():
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
        )

def ingest_chunks(chunks: List[dict]):
    init_collection()
    texts = [chunk["content"] for chunk in chunks]
    metadatas = [{"source": c["source"], "chunk_id": c["chunk_id"]} for c in chunks]

    embeddings = OpenAIEmbeddings()
    vectorstore = Qdrant.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        collection_name=COLLECTION_NAME,
        url=os.getenv("QDRANT_HOST", "http://localhost:6333"),
    )
    print(f"Ingested {len(texts)} chunks into Qdrant.")
