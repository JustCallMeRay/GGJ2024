try:
    import ollama
except ImportError :
    print("You don't have olama, please go get it!")
    raise

class Message:


    def __init__(self):
        self.last_response = ""
        self.previous_messages = []
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

    def sendNoChat(self, prompt:str) -> str:
        response = ollama.chat(model='phi', messages=[
        {
            'role': 'user',
            'content': prompt,
        }])
        return response['message']['content']

    def receive(self) -> str:
        return self.last_response

    def start(self, prompt:str) -> str:
        return self.send(prompt)

wizard = Message()
rate_the_joke = Message()
text_adventure = Message()
guess_the_hash = Message()

if __name__ == "__main__":
    
    m = Message()
    m.send("I have an orange")

    m.send("What fruit do I have?")

    print(m.receive())

