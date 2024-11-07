from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings,  ChatOpenAI
from langchain.chains import LLMChain, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from modules import db

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

#initialise the llm:
llm = ChatOpenAI(model_name= "gpt-3.5-turbo")

#Define a prompt template:
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template = "Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion:\n{question}"
)

#Create the RetrievalQA Chain: 

# Update vector store and set up retriever
retriever = db.update_chroma_vector_store()

# Initialize the chains only if retriever is available
if retriever:
    combine_docs_chain = create_stuff_documents_chain(llm, prompt_template)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)
else:
    print("Error: No documents available. Please load documents into the vector store.")


def qa_query(query):
    global chroma_vector_store
    if retriever:
         # Ensure rag_chain uses the correct input parameter (adjust as needed)
        llm_response = rag_chain.run(query=query)  # Or use question=query if that is required
        return llm_response
    else:
        return "No documents available. Please load documents into vector store."

def run_chatbot():
    print("welcome to chatbot <3 ")
    while True:
        query = input("Enter your question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Ciao!")
            break
        answer = qa_query(query)
        print(f"Answer: {answer}\n")