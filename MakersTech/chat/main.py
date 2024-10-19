import ollama

def call_chat(prompt: str):
    try:
        formatted_prompt = prompt + 'extremly short responce'

        response = ollama.chat(model='llama3.2',
                               messages=[{'role': 'user',
                                          'content': formatted_prompt}])

        return response
    except Exception as e:
        print(f"Error al llamar al chatbot: {e}")
        return None