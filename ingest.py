import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector

load_dotenv()

def get_vectorstore():
    embeddings = OpenAIEmbeddings()
    connection = os.getenv("DATABASE_URL")
    
    return PGVector(
        embeddings=embeddings,
        collection_name="assignment_docs",
        connection=connection,
        use_jsonb=True,
    )

def ingest_documents():
    
    with open("sample_data.txt", "r", encoding="utf-8") as file:
        sample_text = file.read()
    
    doc = Document(page_content=sample_text, metadata={"source": "sample_data.txt"})
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents([doc])
    
    print(f"Documento separado en {len(chunks)} chunks.")
    
    #Guardar en PGvector
    vectorstore = get_vectorstore()
    vectorstore.drop_tables()
    vectorstore.create_tables_if_not_exists()
    vectorstore.create_collection()
    vectorstore.add_documents(chunks)
    
    print("Completado")

if __name__ == "__main__":
    ingest_documents()