# RAG: About Me – Streamlit Demo

This is a personal Q&A web app powered by Retrieval-Augmented Generation (RAG), where users can ask questions about me — my background, skills, projects, and more — and receive semantically grounded answers based on uploaded documents.

The goal is to demonstrate how LLMs can be combined with vector search to create a knowledge-based assistant that answers contextually accurate questions, even from unstructured personal data.

---

## Deployment 

The app is deployed via **Google Cloud Run** and publicly accessible here:
https://who-is-vlad.streamlit.app/

## 🔍 How it works

1. **Document loading** – Text file containing info about me is loaded and chunked.
2. **Embedding** – Chunks are converted into dense vector embeddings using Hugging Face model "sentence-transformers/all-MiniLM-L6-v2".
3. **Indexing** – Vectors are stored in a FAISS vector store for efficient retrieval.
4. **RAG pipeline** – On user query, relevant chunks are retrieved and passed to the language model to generate an answer.
5. **Streamlit UI** – The frontend is built with Streamlit for quick and interactive deployment.

---

