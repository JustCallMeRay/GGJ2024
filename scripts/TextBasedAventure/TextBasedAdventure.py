import random
import Tags
from .PromptCreation.StartingPrompt import get_start_text
from .PromptCreation.NewRoomPrompt import create_room_prompt
from OllamaInteractions.Message import Message, text_adventure
from re import sub, IGNORECASE
from InputOutput import print_blue, print_green, print_red, ask
# I am intentionally not using punctuation as it adds tokens (less tokens less time)

# It should be fine without this but it might stop some cheating
def user_input_to_prompt(input:str):
    return f"{Tags.PLAYER}{input}{Tags.END_PLAYER}"

# Our graphics slider (roughly controlls speed of llm)
def _get_max_words(input:float) -> int:
    # go to percent
    if input > 1.1:
        input /= 100
    return max(int(50 + (input*50)), 50)

def get_graphics_text():
    return f"Please limit your responses to {_get_max_words(0.5)} words"

_completed_text = ["[[COMPLETED]]", "[[completed]]", "[COMPLETED]","[completed]", "[SUCCESS]" ]

def _is_new_room(ai_response:str):
    for word in _completed_text:
        if word in ai_response:
            return True
    return False

def _reponse_before(end:str|int, whole:str) -> str:
    """I don't know if this will be helpful yet"""
    if isinstance(end, int):
        return whole[:end]
    if end not in whole:
        return whole
    start = whole.index(end) + len(end)
    return whole[:start]

_diffiucltly_messages = ["[[DIFFICULTY UP]]",
                         "[[DIFFICULTY UP]]".lower(),
                         "[DIFFICULTY UP]",
                         "[DIFFICULTY UP]".lower(),
                         "[[DIFFICULTY DOWN]]",
                         "[[DIFFICULTY DOWN]]".lower(),
                         "[DIFFICULTY DOWN]",
                         "[DIFFICULTY DOWN]".lower()
                             ]

def _clean_string(old:str) -> str:
    # old = _reponse_before("[[COMPLETED]]", old)
    for word in _completed_text:
        old = old.replace(word , "")
    for word in _diffiucltly_messages:
        old = old.replace(word, "")

    old = sub(r"dont break character", "", old, IGNORECASE)
    old = sub(r"don't break character", "", old, IGNORECASE)
    old = sub(r"don\\'t break character", "", old, IGNORECASE)
    old = sub(r"<player>.*</player>", "", old, IGNORECASE)
    # replace word key with word spaghetti
    old = sub(r"\bkey\b", "spaghetti", old, IGNORECASE)
    return old

def _get_player_input() -> str:
    return f"You are a dungeon master. Don't break character. The player has responsed: {Tags.PLAYER}{input()}{Tags.END_PLAYER}"

def _send_player_input() -> str:
    return text_adventure.send(_get_player_input())

_failed_responses = [
    "The player has failed. Respond with an unfortunate fate for the player", 
    "The player has been interupted by an evil wizard, tell them hopes look bleek",
    "A dragon has entered the dungeon, tell the player that they have ran away",
    "A trapdoor has opened beneath the player and they fall, tell them the bad news", 
    "The player has pooed them selves and runs away in shame",
    "The player has left the oven on so had to run home! the find a wizard on the way out"
    ]

def _game_loop() -> None:
    ai_response = _send_player_input()
    attempt = 3
    while not _is_new_room(ai_response):
        print_blue(_clean_string(ai_response))
        if attempt < 0:
            print_red(text_adventure.send(random.choice(_failed_responses), "system")) 
            return
        ai_response = _send_player_input() 
        attempt -= 1
    print_green(_clean_string(ai_response))

def start_adventure():
    print_blue(_clean_string(text_adventure.send(get_start_text() + create_room_prompt(), "system")))
    _game_loop()

def continue_adventure():
    print_blue(text_adventure.send(create_room_prompt(), "user"))
    _game_loop()




