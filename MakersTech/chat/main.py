import ollama
from .funtions import FUNCTIONS_LIST, TOOLS

MODEL = 'llama3.2'

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
                if function_name in FUNCTIONS_LIST:
                    result = FUNCTIONS_LIST[function_name](**arguments)
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
            f"Context: Your goal is to provide a friendly, concise, and informative response to the user query: "
            f'"{prompt}". function used: {response['message']} ,Use the following information to construct your response: '
            f'{results if results else "results are empty or Currently out of stock."} '
            "Focus on engaging the user and guiding them effectively, as this is a tech store. Keep responses brief and direct."
            )

        return call_chat(prompt=output_prompt, tools=None)

    except Exception as e:
        print(f"Error al iniciar chat: {e}")
        return None