
# import message class
from OllamaInteractions.Message import Message



from PromptCreation.StartingPrompt import get_start_text
import PromptHelpers
from random import choice as random_choice
from enum import Enum
import RateThejoke
import GuessTheHash

has_wizard_instance:bool = False;

enum = {"RATE_THE_JOKE":False,"GUESS_THE_HASH":False}

current_minigame:None|str = None

oli = Message()

def get_minigame_start():
    if current_minigame == "RATE_THE_JOKE":
        return RateThejoke.rate_the_joke()
    if current_minigame == "GUESS_THE_HASH":
        return GuessTheHash.guess_the_hash()
    
    
    
    else:
        raise Exception("I did not execpt this to happen")

def _get_success_no_wizard(player_input:str):
    if current_minigame == "RATE_THE_JOKE":
        success, response = RateThejoke.was_success(player_input)
    if current_minigame == "GUESS_THE_HASH":
        return GuessTheHash.guess_the_hash()

def get_success_state(game_uses_wizard, player_input:str):
    if not game_uses_wizard:
        _get_success_no_wizard(player_input)



def run_minigame():
    text = "";
    keys:list[str] = [key for key in enum.keys()] # urgh
    game = random_choice(keys)
    if not has_wizard_instance:
        text = get_start_text(enum[game]);
    text += get_minigame_start()
    oli.send(text)
    
    






