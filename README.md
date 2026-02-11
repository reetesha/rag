**Description**: Built a Retrieval-Augmented Generation (RAG) assistant that ingests documents, generates embeddings, stores them in a FAISS vector database, retrieves relevant context based on user queries, and generates answers using an LLM. The system includes a Streamlit UI, persistent vector storage, and modular architecture to simulate a production-style GenAI pipeline.

**Steps to run the app:**

1. pip install -r requirements.txt
2. Run the app 
**streamlit run src/app.py**

**GenAI system I built:**

I built a document-based question-answering assistant using a Retrieval-Augmented Generation architecture. The system has two main pipelines: an ingestion pipeline and a query pipeline.


In the ingestion pipeline, documents are loaded, chunked, converted into embeddings using a sentence-transformer model, and stored in a FAISS vector database. The vector index is persisted to disk to avoid recomputation.

In the query pipeline, when a user asks a question through a Streamlit UI, the query is embedded and used to retrieve the most relevant document chunks. These chunks are passed as context to an LLM, which generates a grounded answer.

I structured the project into separate modules for loading, retrieval, and generation, which reflects how production systems are typically designed. In a real enterprise setup, this architecture would be extended with caching, guardrails, and observability layers.

**Flow step by step:**

1. The system works in five steps:
2. Document ingestion and chunking
3. Embedding generation
4. Vector storage and persistence
5. Similarity-based retrieval
6. Context-augmented answer generation

Retrieval ensures that the model answers based on grounded knowledge rather than relying purely on its training data, which significantly reduces hallucination.

**Architecture Explanation**

**User → UI → Retriever → Vector DB → Context → LLM → Answer**

Retrieval reduces hallucination and improves factual accuracy by grounding answers in enterprise data.

**Why RAG Instead of Fine-Tuning**
RAG is preferred when knowledge changes frequently or documents are large, because updating a vector database is much cheaper and faster than retraining or fine-tuning a model.

**Tradeoffs**
Some key tradeoffs include chunk size selection, retrieval latency, embedding quality, and managing hallucinations. Larger chunks improve context but reduce retrieval precision, while smaller chunks improve retrieval but may lose semantic continuity.

Improvements
Redis semantic caching
Hybrid search (BM25 + vector)
Guardrails for PII filtering
Observability for latency and accuracy

**Learning:** At scale, ingestion runs as batch pipelines, vector indexes are sharded, and retrieval services are deployed independently to reduce latency.

Latency: Latency mainly comes from embedding and LLM inference, so caching and smaller models are key optimization techniques.

**Elevator Pitch:** I built a RAG-based knowledge assistant that retrieves context from a vector database and generates grounded answers using an LLM, with persistent storage and a UI to simulate a production architecture.

**It demonstrates:**

Distributed thinking
Data pipeline thinking
Retrieval systems
AI integration
UI layer


**Sample Input Questions to Try**
**Easy queries (direct match)**

How many sick leaves are allowed?

How many annual leaves do employees get?

Is remote work allowed?

Medium queries (semantic retrieval)

These test embeddings better:

What is the leave policy?

Can employees work from home?

What benefits do employees receive?

Hard queries (multi-line retrieval)
Tell me about company policies related to employees.

What rules should employees follow regarding expenses?


These test chunk retrieval and context joining.


**High-Level Architecture**

<img width="371" height="530" alt="image" src="https://github.com/user-attachments/assets/0670ae49-d36c-44d8-87b9-52ff43d079cf" />

**App Output :**

<img width="1031" height="546" alt="image" src="https://github.com/user-attachments/assets/364c3e48-f1fc-4273-a81e-916dbdb49025" />

![Uploading image.png…]()





