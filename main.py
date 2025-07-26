from fastapi import FASTAPI
from dotenv import load_dotenv
import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")


app = FASTAPI()



# Load precomputed index from storage
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()




@app.get("/")
async def root():
    return {"message": "developer documentation chatbot is running"}




@app.get("/query/")
async def query_docs(question: str):
    response = index.as_query_engine().query(question)
    return {"response": str(response)}


