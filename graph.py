from typing import List, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langgraph.graph import StateGraph, START, END
from ingest import get_vectorstore

#Definir el estado
class GraphState(TypedDict):
    question: str
    documents: List[Document]
    answer: str

#Definir los nodos
def retrieve_node(state: GraphState):
    print("Recuperando contexto...")
    question = state["question"]
    vectorstore = get_vectorstore()
    
    docs = vectorstore.similarity_search(question, k=5) # recupera los dos chunks más relevantes
    return {"documents": docs}

def generate_node(state: GraphState):
    print("Generando respuesta...")
    question = state["question"]
    documents = state["documents"]
    
    
    context = "\n\n".join([doc.page_content for doc in documents]) # Formatea el contexto
    
    # Prompt inicial para el LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = f"""Eres un asistente de datos inteligente. Debes responder la pregunta basándote ÚNICAMENTE en el contexto provisto. 
    Puedes usar sinónimos, sumar números y hacer deducciones lógicas siempre y cuando la información provenga directamente de este contexto.
    Si la información necesaria para responder no se encuentra en absoluto dentro del contexto, debes responder exactamente: "No puedo responder a esto basándome en los documentos proporcionados." 
    Bajo ninguna circunstancia debes inventar información o usar conocimiento de internet.
    
    Contexto: {context}
    
    Pregunta: {question}
    
    Answer:"""
    
    
    response = llm.invoke(prompt)
    return {"answer": response.content}

def build_rag_graph():
    workflow = StateGraph(GraphState)
    
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("generate", generate_node)
    
    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)
    
    return workflow.compile()