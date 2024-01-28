
from random import choice as random_choice
from random import random as random_float

# list of nouns all should be funny
_nouns_funny = ["beans", "a lake of beans", "eggs", "a cat", "alphabetty spagetti", "an elephant (never mentioned)"]

_nouns_quest = ["key", "bookshelf", "cat treats"]

_nouns_interactables = ["danish pastry", "crosiont"]

def create_room_prompt(nouns:str|None = None):
    if nouns is None:
        nouns = random_choice(_nouns_funny)
    elif random_float() > 0.5: 
        nouns += random_choice(_nouns_funny)
    if random_float() > 0.6 :
        nouns += f", {random_choice(_nouns_quest)}"
    if random_float() > 0.8 :
        nouns += f", {random_choice(_nouns_interactables)}"
    
    if nouns == "" or nouns is None:
        nouns = random_choice(_nouns_funny)

    return f"This room should contain {nouns} and anything else the player needs to escape"

if __name__ == "__main__":
    print(create_room_prompt())