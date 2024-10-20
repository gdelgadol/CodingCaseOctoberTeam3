import ollama
from MakersTech.MakersTechApp import views

MODEL = 'llama3.2'

FUNCTIONS = {}

TOOLS = [
    {
    'type': 'function',
    'function': {
        'name': '',
        'description': '',
        'parameters': {
            'type': 'object',
            'properties': {
            'number': {
                'type': '',
                'description': '',
                },
            },
            'required': [''],
            },
        },
    },
    ]

def call_chat(prompt: str, tools=None):
    try:
        messages = [{'role': 'user', 'content': prompt}]
        if tools:
            response = ollama.chat(
                model=MODEL,
                messages=messages,
                tools=tools)
        else:
            response = ollama.chat(
                model=MODEL,
                messages=messages)
        
        if 'tool_calls' in response['message']:
            for tool_call in response['message']['tool_calls']:
                function_name = tool_call['function']['name']
                arguments = tool_call['function']['arguments']
                
                # Verificar si la función existe en el registro
                if function_name in FUNCTIONS:
                    # Llamar a la función y obtener el resultado
                    result = FUNCTIONS[function_name](**arguments)
                    return response, result

        return response, None

    except Exception as e:
        print(f"Error al llamar al chatbot: {e}")
        return None, None

def start_chat(prompt: str):
    try:
        response, results = call_chat(
            prompt=prompt,
            tools=TOOLS
        )
        output_prompt = (
            f"Context: Your goal is to provide a friendly and informative response to the user query: "
            f'"{prompt}". Use the following information to construct your response: '
            f'{results if results else "No result from function."} '
            "Ensure the response is engaging and guides the user towards making a purchase decision. (short responce)"
            )
        return call_chat(prompt=output_prompt, tools=None)

    except Exception as e:
        print(f"Error al iniciar chat: {e}")
        return None