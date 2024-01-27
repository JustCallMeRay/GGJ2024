import random
import Tags
from PromptCreation import StartingPrompt
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

def start_adventure():
    text_adventure.send(StartingPrompt.get_start_text())

def is_new_room(ai_response:str):
    if "[[COMPLETED]]" in ai_response:
        return True
    if "[[completed]]" in ai_response.lower():
        return True
    