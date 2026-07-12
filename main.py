from ingest import ingest_documents
from graph import build_rag_graph

def run_interactive_system():
    print("Ingestión")
    ingest_documents()
    
    print("\nConsulta")
    print("Listo (Escriba 'exit' para salir)")
    app = build_rag_graph()
    
    while True:
        user_input = input("\nEscriba su pregunta: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Saliendo de RAG")
            break
            
        # Correr el grafo con el input del usuario
        inputs = {"question": user_input}
        result = app.invoke(inputs)
        
        print("\n=== RESPUESTA ===")
        print(f"Pregunta: {result['question']}")
        print(f"Respuesta: {result['answer']}")
        print("====================\n")

if __name__ == "__main__":
    run_interactive_system()