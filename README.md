# 🧠 NeuraDocs – Internal Docs AI Q&A Service

**NeuraDocs** is an internal API that answers technical questions using your company's internal PDF documentation. It leverages Retrieval-Augmented Generation (RAG) to ground responses in your own knowledge base, enabling fast, accurate, and explainable answers.

---

## 🚀 Key Features

- 🔍 Semantic search over internal PDFs using vector embeddings
- 🤖 GPT-powered answers with citations from your actual docs
- 📄 Automatic PDF parsing, chunking, and indexing
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- 🧾 REST API for internal use or integration with tools/UIs

---

## 🏗️ Architecture

```text
[PDF Documents]
      ↓
 [PDF Parser]
      ↓
[Text Chunker (LangChain)]
      ↓
[Embedder (OpenAI Embeddings)]
      ↓
[Vector Store (Qdrant)]
      ↓
        ┌────────────┐
        │  User Query│
        └─────┬──────┘
              ↓
      [Embed Query]
              ↓
   [Similarity Search (Top-k)]
              ↓
[Prompt LLM with Retrieved Context]
              ↓
     [Generated Answer + Sources]
