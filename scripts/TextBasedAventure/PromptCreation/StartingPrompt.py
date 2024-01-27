### Creates the first "start a chat" prompt to the llm
import scripts.Tags as Tags

import PromptHelpers

def _room_end_tag() -> str:
    return "When a room is completed write [[COMPLETED]] on a sinlge line at the start of your response"

def _diffiucltly_text() -> str:
    """This is so the llm understands the difuclty system"""
    text = "If the player wants difficulty change, the first line should be [[DIFFICULTY UP]] or [[DIFFICULTY DOWN]]"
    return text

def get_start_text() -> str:
    """This happens once at the start of the game"""
    # TODO edit and expand
    start = "You are simulating a text based adventure..."
    return "\n".join([start, _room_end_tag(), PromptHelpers.saftey_text(), _diffiucltly_text()])

