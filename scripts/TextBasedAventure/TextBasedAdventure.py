import random
import Tags
from .PromptCreation.StartingPrompt import get_start_text
from .PromptCreation.NewRoomPrompt import create_room_prompt
from OllamaInteractions.Message import Message, text_adventure
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

def _is_new_room(ai_response:str):
    if "[[COMPLETED]]" in ai_response:
        return True
    if "[[completed]]" in ai_response.lower():
        return True

def _reponse_before(end:str|int, whole:str) -> str:
    """I don't know if this will be helpful yet"""
    if isinstance(end, int):
        return whole[:end]
    if end not in whole:
        return whole
    start = whole.index(end) + len(end)
    return whole[:start]

def _clean_string(old:str) -> str:
    old = _reponse_before("[[COMPLETED]]", old)
    old = old.replace("[[COMPLETED]]", "")
    old = old.replace("[[completed]]", "")
    old = old.replace("[[DIFFICULTY UP]]", "")
    old = old.replace("[[DIFFICULTY DOWN]]", "")
    return old

def _get_player_input() -> str:
    return f"{Tags.PLAYER}{input()}{Tags.END_PLAYER}"

def _send_player_input() -> str:
    return text_adventure.send(_get_player_input())

def _game_loop() -> None:
    ai_response = _send_player_input()
    while not _is_new_room(ai_response):
        print(_clean_string(ai_response))
        ai_response = _send_player_input()
    print(_clean_string(ai_response))

def start_adventure():
    print(text_adventure.send(get_start_text() + create_room_prompt()), "system")
    _game_loop()

def continue_adventure():
    print(text_adventure.send(create_room_prompt()), "system")
    _game_loop()




