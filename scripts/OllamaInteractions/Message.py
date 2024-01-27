import ollama

def send(prompt:str) -> str:
    response = ollama.chat(model='phi', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    return response['message']['content']

def receive() -> str:
    return ""

def start(prompt:str) -> None:
    return
