from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_deepseek import ChatDeepSeek
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.getenv("DEEPSEEK_API_KEY")

# FastAPI app
app = FastAPI()

# Embedding and vectorstore
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("vectorstore", embedding_model, allow_dangerous_deserialization=True)

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


prompt = PromptTemplate.from_template("""
You are a friendly agent of Vlad. Answer the question about him based on the following context. 
If context doesn't help you to answer the question, say exactly: "Sorry, I don't know, my lazy master didn't tell me that 😖"

Context:
{context}

Question: {input}
""")

combine_docs_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=prompt
)

chain = create_retrieval_chain(
    retriever=db.as_retriever(),
    combine_docs_chain=combine_docs_chain
)

# def main():
#     while True:
#         question = input("Ask a question about Vlad (or 'exit'): ").strip()
#         if question.lower() in {"exit", "quit"}:
#             break
#
#         result = chain.invoke({"input": question})
#         print("\nAnswer:", result["answer"])
#         print("-" * 50)

# if __name__ == "__main__":
#     main()


# Pydantic model for request
class QuestionRequest(BaseModel):
    question: str

# Endpoint
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    result = chain.invoke({"input": request.question})
    return {"answer": result["answer"]}


# class Question(BaseModel):
#     query: str
