from loader import load_and_split
from vector_store import create_vector_store
from rag_pipeline import retrieve_answer

def main():
    print("Loading documents...")
    docs = load_and_split("data/policy.txt")

    print("Creating vector store...")
    db = create_vector_store(docs)

    while True:
        query = input("\nAsk a question (or type exit): ")

        if query.lower() == "exit":
            break

        answer = retrieve_answer(db, query)
        print(answer)

if __name__ == "__main__":
    main()
