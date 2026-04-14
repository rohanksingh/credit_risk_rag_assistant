from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

docs = [
    "Retail segment PD increased due to unemployment and inflation.",
    "Corporate segment showed stable credit performance.",
    "Interest rate hikes impacted borrower repayment capacity.",
    "Macroeconomic stress leads to higher default probability."
]

documents = [Document(page_content=d) for d in docs]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(documents, embeddings)

os.makedirs("data/vector_store", exist_ok=True)
vector_store.save_local("data/vector_store")

print(" Vector store created!")