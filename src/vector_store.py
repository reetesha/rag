import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DB_PATH = "vector_store/faiss_index"

def get_vector_store(docs):
    embeddings = HuggingFaceEmbeddings()

    if os.path.exists(DB_PATH):
        try:
            print("Loading existing vector DB...")
            return FAISS.load_local(
                DB_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
        except Exception as e:
            print("Vector DB incompatible. Rebuilding...")
            print(e)

    print("Creating new vector DB...")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)
    return db
