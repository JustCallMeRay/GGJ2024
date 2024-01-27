try:
    import ollama
except ImportError :
    print("You don't have olama, please go get it!")
    raise
import pprint

class Message:


    def __init__(self):
        self.last_response = ""
        self.previous_messages = []
        pass

    def send(self, prompt:str, role="user") -> str:
        retries = 10 # retry if we don't get a response
        self.previous_messages.append(
        {
            'role': role,
            'content': prompt,
        })
        # print("\033[92m Sent: ")
        # pprint.pprint(self.previous_messages)
        while True:
            response = ollama.chat(model='phi', messages=self.previous_messages)
            retries -= 1
            if retries < 0 or response['message']['content'] != "":
                break
        if response['message']['content'] == "":
            response['message']['content'] = "I don't know what to say"
        # print("\033[96m Received: ")
        # pprint.pprint(response)
        # print("\033[0m")
        self.previous_messages.append(response['message'])
        self.last_response = response['message']['content']
        return self.last_response

    def sendNoChat(self, prompt:str, role = "user") -> str:
        response = ollama.chat(model='phi', messages=[
        {
            'role': role,
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

