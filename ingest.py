from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


def ingest():
    docs = []
    for filename in os.listdir("data"):
        if filename.endswith(".md") or filename.endswith(".txt"):
            loader = TextLoader(os.path.join("data", filename), encoding='utf-8')
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    print(f"Split {len(docs)} documents into {len(chunks)} chunks.")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local("vectorstore")

if __name__ == "__main__":
    ingest()
