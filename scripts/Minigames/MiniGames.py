
# import message class
from OllamaInteractions.Message import Message, wizard

from Minigames.PromptCreation.StartingPrompt import get_start_text
import PromptHelpers
from random import choice as random_choice
from enum import Enum
from . import RateThejoke
from . import GuessTheHash
from . import Punchline

has_wizard_instance:bool = False

enum = {
    "RATE_THE_JOKE":False,
    "GUESS_THE_HASH":False,
    "PUNCHLINE":False
    }

current_minigame:None|str = None

def _run_current_minigame():
    global current_minigame
    if current_minigame == "RATE_THE_JOKE":
        return RateThejoke.go()
    if current_minigame == "GUESS_THE_HASH":
        return GuessTheHash.go()
    if current_minigame == "PUNCHLINE":
        return Punchline.go()
    else:
        raise Exception("I did not execpt this to happen")

def _get_success_no_wizard(player_input:str):
    success =False
    if current_minigame == "RATE_THE_JOKE":
        success, response = RateThejoke.was_success(player_input)
    if current_minigame == "GUESS_THE_HASH":
        return GuessTheHash.guess_the_hash()
    return success

def get_success_state(game_uses_wizard, player_input:str):
    if not game_uses_wizard:
        _get_success_no_wizard(player_input)



def run_minigame():
    while True:
        text = ""
        keys:list[str] = [key for key in enum.keys()] # urgh
        game = random_choice(keys)
        global current_minigame
        current_minigame = game
        if not has_wizard_instance:
            text = get_start_text(enum[game])
        _run_current_minigame()
        



