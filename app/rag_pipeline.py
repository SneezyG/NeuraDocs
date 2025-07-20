# app/rag_pipeline.py

from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

COLLECTION_NAME = "doc_chunks"

class RAGPipeline:
    def __init__(self):
        self.embedding = OpenAIEmbeddings()
        self.vectorstore = Qdrant(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embedding,
            url=os.getenv("QDRANT_HOST", "http://localhost:6333")
        )
        self.llm = ChatOpenAI(temperature=0.0)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5}),
            return_source_documents=True
        )

    def query(self, user_input: str) -> dict:
        result = self.qa_chain(user_input)
        return {
            "answer": result["result"],
            "sources": [doc.metadata for doc in result["source_documents"]]
        }
