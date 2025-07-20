# 🧠 NeuraDocs – A Rag AI-powered backend that answer questions using internal documentation.

**NeuraDocs** is an API service that answers technical questions using your company's internal PDF documentation. It leverages Retrieval-Augmented Generation (RAG) to ground responses in your own knowledge base, enabling fast, accurate, and explainable answers.

## [See NeuraDocs Code Repo](.)

---

## 🚀 Key Features

- 🔍 Semantic search over internal PDFs using vector embeddings
- 🤖 GPT-powered answers with citations from your actual docs
- 📄 Automatic PDF parsing, chunking, and indexing
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- 🧾 REST API for internal use or integration with tools/UIs

---

## 🧰 Technologies Used

- **Python** – Core language
- **FastAPI** – REST API framework
- **LangChain** – RAG orchestration and text processing
- **OpenAI** – Embeddings and chat completions (GPT-3.5/GPT-4)
- **Qdrant** – High-performance vector database
- **PyMuPDF (fitz)** – PDF parsing
- **dotenv** – Environment configuration

---

## 🧠 Retrieval-Augmented Generation (RAG) Pipeline

1. **PDF Parsing**: Extract text from PDFs using PyMuPDF.
2. **Chunking**: Split text into overlapping semantic chunks using LangChain.
3. **Embedding**: Encode chunks into vector embeddings using OpenAI.
4. **Storage**: Store vectors and metadata in Qdrant.
5. **Querying**:
   - Embed user query
   - Search similar chunks from vector DB
   - Prompt LLM with retrieved content
6. **Response**: Return generated answer with traceable sources.

---

## 📡 API Endpoint

### `POST /ask`

- Accepts a natural language query.
- Returns a AI-generated answer based on internal documentation.
- Includes document metadata for context traceability.

---

## 📎 Example Use Cases

- Internal dev documentation Q&A
- AI-powered engineering assistant
- Knowledge base augmentation
- Automated onboarding and support tools
