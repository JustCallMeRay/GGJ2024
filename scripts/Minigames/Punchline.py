# a minigame where the player guesses the correct punchline

from InputOutput import print_blue, print_green, print_red, ask
import random
import OllamaInteractions.Message as Message

def get_joke() -> tuple[str,str]:

    # load the file jokes.txt and get a random line from the line
    with open('jokes.txt', 'r') as file:
        jokes = file.readlines()
    line = random.choice(jokes).strip()
    # split the line into the setup and the punchline divided by <>
    setup, punchline = line.split('<>')
    return setup, punchline


def go():
    m = Message.punchline
    joke = get_joke()
    print_blue("Guess which is the real punchline to this joke:")
    print_green(joke[0])
    i = random.randrange(0, 4)
    for j in range(4):
        if j == i:
            print_blue(f"{j+1}: {joke[1]}")
        else:
            punchline = m.sendNoChat("You are a funny guy. Guess the punchline to this joke, give the punchline only: " + joke[0], "system")
            punchlineFirst40Words = " ".join(punchline.split(" ")[:25]).replace("\n", "")
            print_blue(f"{j+1}: {punchlineFirst40Words}")
    answer = ask("Which is the real punchline? 1 - 4 >")
    if int(answer) == i + 1:
        print_green("You guessed correctly!")
        return True
    else:
        print_red("Wrong!")
        return False

if __name__ == "__main__":
    print(go())
