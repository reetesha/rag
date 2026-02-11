
import streamlit as st
from loader import load_and_split
from vector_store import get_vector_store
from rag_pipeline import retrieve_answer

st.title("Enterprise RAG Assistant")

if "db" not in st.session_state:
    docs = load_and_split("data/policy.txt")
    st.session_state.db = get_vector_store(docs)

query = st.text_input("Ask a question")

if query:
    answer = retrieve_answer(st.session_state.db, query)
    st.write(answer)
