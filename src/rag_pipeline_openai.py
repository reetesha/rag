from langchain_openai import ChatOpenAI

def retrieve_answer(db, query):
    # Retrieve relevant documents
    results = db.similarity_search(query, k=3)

    # Combine retrieved context
    context = "\n".join([doc.page_content for doc in results])

    # Build prompt
    prompt = f"""
You are a helpful assistant. Answer the question using only the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    # Call LLM
    llm = ChatOpenAI(temperature=0)
    response = llm.invoke(prompt)

    return response.content
