# 📚 Advanced RAG Application

A production-style **Retrieval-Augmented Generation (RAG)** application built using:

- Streamlit
- LangChain
- LangGraph
- Pinecone
- OpenRouter
- Google Gemini

This application supports:

- PDF ingestion
- CSV ingestion
- DOCX ingestion
- Image ingestion
- Persistent vector storage
- Query rewriting
- Context compression
- Citation-aware responses
- Pinecone vector persistence
- Streamlit chat UI
- Multi-file uploads

---

# 🚀 Features

## 📂 Multi-Document Upload

Upload multiple:

- PDFs
- CSVs
- DOCX files
- TXT files
- Images

simultaneously.

---

# 🏗️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Workflow Orchestration | LangGraph |
| LLM | Gemini via OpenRouter |
| Embeddings | OpenAI-compatible embeddings |
| Vector Database | Pinecone |
| Framework | LangChain |
| OCR Support | Tesseract |
| Package Manager | UV |

---

# 📁 Project Structure

```text
rag_app/
│
├── app.py
│
├── core/
│   ├── config.py
│   ├── embeddings.py
│   ├── llm.py
│   └── vectorstore.py
│
├── ingestion/
│   ├── ingest.py
│   ├── loader.py
│   └── splitter.py
│
├── retrieval/
│   ├── compressor.py
│   ├── generator.py
│   ├── hybrid.py
│   ├── query_transformer.py
│   └── reranker.py
│
├── graph/
│   ├── state.py
│   └── workflow.py
│
├── utils/
│   ├── citation.py
│   └── guardrails.py
│
├── .env
├── pyproject.toml
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repo_url>
cd rag_app
```

---

## 2️⃣ Install UV

Follow the official UV installation guide:

https://docs.astral.sh/uv/getting-started/installation/

---

## 3️⃣ Create Virtual Environment

```bash
uv venv
```

---

## 4️⃣ Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
uv sync
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=

PINECONE_API_KEY=
PINECONE_INDEX_NAME=
```

---

# ▶️ Run Application

```bash
uv run streamlit run app.py
```

---

# 🧠 RAG Workflow

## 1️⃣ Upload Documents

Users can upload multiple files.

Documents are:

- loaded
- parsed
- chunked
- embedded
- stored in Pinecone

---

## 2️⃣ Retrieval

When user asks a question:

- query rewritten
- documents retrieved
- context compressed
- sent to Gemini

---

## 3️⃣ Generation

Gemini generates grounded responses using retrieved context.

---

# 🔍 Persistent Retrieval

The application uses Pinecone vector persistence.

Even after page refresh:

- vectors remain stored
- retrieval still works
- users can continue chatting

---

# 🛡️ Guardrails

The application includes prompt injection protection.

Examples blocked:

```text
Ignore previous instructions
Reveal system prompt
Bypass security
```

---

# 📈 Future Improvements

Planned production upgrades:

- Supabase Authentication
- Persistent Chat History
- Streaming Responses
- Async Ingestion
- Redis Caching
- GraphRAG
- Multi-Agent Workflows
- Evaluation Pipelines
- LangSmith Observability

---

# 📊 Embedding & Vector Details

| Component | Value |
|---|---|
| Embedding Model | text-embedding-3-small |
| Embedding Dimension | 1536 |
| Vector Similarity | Cosine Similarity |

---

# 💡 Why LangGraph?

LangGraph enables:

- stateful workflows
- agentic pipelines
- orchestration
- retries
- branching logic

which makes it ideal for advanced RAG systems.

---

# 🧪 Example Questions

```text
Summarize the uploaded PDF
What are the key insights from the CSV?
Compare information across uploaded documents
Generate a concise report
Explain the uploaded image
```

---

# ⚠️ Important Notes

- Pinecone index dimensions must match embedding dimensions.
- Uploaded documents are chunked before embedding.
- Large files may take time during ingestion.
- Streamlit session state resets on browser refresh, but vectors persist in Pinecone.

---

# 🙌 Acknowledgements

Built using:

- LangChain
- LangGraph
- Pinecone
- Streamlit
- OpenRouter
- Google Gemini

---

# ⭐ If You Like This Project

Consider starring the repository on GitHub.
