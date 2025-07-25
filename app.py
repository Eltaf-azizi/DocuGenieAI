import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb


load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")


# Load documents from directory
documents = SimpleDirectoryReader('./documentation').load_data()


# Initialize chromadb
chroma_client = chromadb.PersistentClient(path="./storage")



# Load a chroma collection
collection_name = 'dev_docs_collection'



try:
    chroma_collection = chroma_client.get_collection(collection_name)

except Exception:
    chroma_collection = chroma_client.create_collection(collection_name)




# Wrap chromadb as vector store
vector_store = ChromaVectorStore(chroma_collection)



# Create vector index
index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)



# Save storage context for later use
index.storage_context.persist('./storage')


print("Documents index successfuly")