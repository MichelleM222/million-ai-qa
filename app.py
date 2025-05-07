from pdf_reader import extract_text_from_pdf
from qa_engine import QAEngine

def main():
    print("Cargando documento...")
    raw_text = extract_text_from_pdf("data/TECHNICAL_TEST_ENGINEER_AI_MILLION.pdf")
    
    print("Inicializando motor de preguntas...")
    qa = QAEngine(raw_text)

    print("¡Listo! Puedes empezar a hacer preguntas sobre el contenido del PDF.")
    while True:
        query = input("\nPregunta (o escribe 'salir'): ")
        if query.lower() == "salir":
            break
        answer = qa.ask(query)
        print(f"Respuesta: {answer}")

if __name__ == "__main__":
    main()