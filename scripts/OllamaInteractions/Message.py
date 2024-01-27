import ollama

previous_messages = []
last_response = ""

def send(prompt:str) -> str:
    previous_messages.append(
    {
        'role': 'user',
        'content': prompt,
    })
    response = ollama.chat(model='phi', messages=previous_messages)
    last_response = response['message']['content']
    return last_response

def receive() -> str:
    return last_response

def start(prompt:str) -> str:
    return send(prompt)

if __name__ == "__main__":
    pass

