import ollama

class Message:

    previous_messages = []
    last_response = ""

    def __init__(self):
        pass

    def send(self, prompt:str) -> str:
        self.previous_messages.append(
        {
            'role': 'user',
            'content': prompt,
        })
        response = ollama.chat(model='phi', messages=self.previous_messages)
        self.last_response = response['message']['content']
        return self.last_response

    def receive(self) -> str:
        return self.last_response

    def start(self, prompt:str) -> str:
        return self.send(prompt)

if __name__ == "__main__":
    
    m = Message()
    m.send("I have an orange")

    m.send("What fruit do I have?")

    print(m.receive())

