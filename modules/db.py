from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStoreRetriever


documents = []


#initialise vector store to None:
chroma_vector_store = None

# Build Retriever:
#initialise retriever as None
retriever = None


#update vector store/load it when chatbot runs: 
def update_chroma_vector_store():
    global documents, chroma_vector_store, retriever
    if not documents:
        print("Warning: No documents to load into vector store.")
        return None

    if documents:
        chroma_vector_store = Chroma.from_documents(
            documents,
            embedding_model, 
            persist_directory = "./chroma_db"
        )
        retriever = VectorStoreRetriever(vector_store=chroma_vector_store)
        return retriever

