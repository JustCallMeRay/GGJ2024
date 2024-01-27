
from typing import Tuple

# doesn't use wizard (new AI instance)
def rate_the_joke():
    return "Ask the player to tell you a joke, if it is funny enough you will let them through"

def rate_the_joke_success():
    return "The player's joke was funny and you let them through to the next room"

def rate_joke_fail():
    return "Tell the player why their joke was bad and that they will not be let through to the next room"

def rate_joke_too_many_attempts():
    return "Tell the player their jokes are bad but you pitty them for living in sadness and that is why you are letting them through"

def get_rating(player_input:str) -> str:
    # TODO give the input to the AI and get a response
    return ""

def _reponse_after(start_after:str, whole:str) -> str:
    if isinstance(start_after, int):
        return whole[start_after:]
    start = whole.index(start_after) + len(start_after)
    return whole[start:]

def was_success(player_input:str) -> Tuple[bool,str]:
    ai_text = get_rating(player_input)
    if "GOOD" in ai_text:
        return True, _reponse_after("GOOD", ai_text)
    if "BAD" in ai_text:
        return False, _reponse_after("BAD", ai_text)
    if "MED" in ai_text:
        return True, _reponse_after("MED", ai_text)

    lower = ai_text.lower()
    if "good" in lower:
        return True, _reponse_after(ai_text.index("good"), ai_text)
    if "bad" in lower:
        return False, _reponse_after(ai_text.index("bad"), ai_text)
    if "med" in lower:
        return True, _reponse_after(ai_text.index("med"), ai_text)
    
    return True, "I don't fully get this joke but I think I like it"

def go(message):
    while True:
        print(message.sendNoChat(rate_the_joke()))
        joke = input("Enter joke")
        q = "You are a human with opionions and a sense of humor. Respond only with the rating\
        for the following dad joke on a scale of GOOD, MED or BAD as if you were a human\
        at a work event, your rating should always be the first line of your response then any follow up: \
        <JOKE>" + joke + "</JOKE>"
        response = message.sendNoChat(q)
        print(response)
        success, msg = was_success(response)
        print(msg)
        if success:
            break


          