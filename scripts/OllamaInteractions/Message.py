import ollama

def send(prompt:str) -> None:
    response = ollama.chat(model='phi', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])

def receive() -> str:
    return ""

def start(prompt:str) -> None:
    return
