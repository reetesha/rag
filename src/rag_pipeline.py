from langchain_ollama import OllamaLLM

def retrieve_answer(db, query):
    results = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in results])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    llm = OllamaLLM(model="llama3")
    response = llm.invoke(prompt)

    return response
