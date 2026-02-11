from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

def load_and_split(path):
    loader = TextLoader(path)
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)
    return docs
