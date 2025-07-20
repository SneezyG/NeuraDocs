# app/api.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.rag_pipeline import RAGPipeline

app = FastAPI()
rag = RAGPipeline()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(req: QueryRequest):
    response = rag.query(req.query)
    return {
        "answer": response["answer"],
        "sources": response["sources"]
    }
