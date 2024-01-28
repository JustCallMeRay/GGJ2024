
from typing import Tuple
from OllamaInteractions import Message
from InputOutput import print_blue, print_green, print_red, ask
from .PromptCreation.StartingPrompt import get_start_text
from random import choice
_wizard_names = ["Magnus Carlson", "Clembrior Smith", "Stagasgore Cook" ]

_mortal_adjectives = ["foolish", "unworthy", "powerless", "", "feeble", "pathetic", "puny", "pitiful", "insignificant", "inadequate" ]

_mortal_nouns = ["mortal", "human"]

_start_words = ["Ah!,", "Ahah", "We meet again", "", "Hmph!" ]

_bad_joke_reponses = [f"""{choice(_start_words)}, {choice(_mortal_adjectives) } {choice(_mortal_nouns)}! Your attempt at humor is as laughable as your {choice(_mortal_nouns)} existence. I, {choice(_wizard_names)}, find your joke to be as dull as a rusted blade in my arsenal. Your words lack the wit and brilliance befitting a mastermind such as myself. Your {choice(_mortal_adjectives)} attempts at amusement are like a candle flickering in the vast darkness of my superior intellect.

Try harder, if you dare, to amuse the Lord of Destruction with a joke worthy of eliciting even the faintest smirk. Until then, revel in the realization of your inadequacy in the presence of {choice(_wizard_names)}!""", f"""{choice(_start_words)}, {choice(_mortal_adjectives) } {choice(_mortal_nouns)} Your attempt at humor is as {choice(_mortal_nouns)} as your understanding of cryptographic complexities, {choice(_mortal_nouns)}. I find your joke lacking in wit and utterly beneath the standards of {choice(_wizard_names)} refined taste. Perhaps you should focus less on jesting and more on honing your {choice(_mortal_adjectives)} intellect to stand a chance in the challenges that lie ahead. Your jests are as weak as your grasp on reality, {choice(_mortal_nouns)}!""",
"Tell the player why their joke was bad and that they will not be let through to the next room"]


# doesn't use wizard (new AI instance)
def rate_the_joke():
    return "Ask the player to tell you a joke, if it is funny enough you will let them through"

def rate_the_joke_success():
    return "The player's joke was funny and you let them through to the next room"

def rate_joke_fail():
    return choice(_bad_joke_reponses) 

def rate_joke_too_many_attempts():
    return "Tell the player their jokes are bad but you pitty them for living in sadness and that is why you are letting them through"

def get_rating(player_input:str) -> str:
    # TODO give the input to the AI and get a response
    return ""

def _reponse_after(start_after:str|int, whole:str) -> str:
    if isinstance(start_after, int):
        return whole[start_after:]
    start = whole.index(start_after) + len(start_after)
    return whole[start:]

_good_variations = ["GOOD", "MED", "not bad"]
_bad_variations = ["BAD", "NOT GOOD"]

def _clean_string(input:str) -> str:
    for bad_word in _good_variations + _bad_variations:
        input = input.replace(f"[[{bad_word}]]", "")
        input = input.replace(f"[{bad_word}]", "")
        input = input.replace(f"[[{bad_word}]]".lower(), "")
        input = input.replace(f"[{bad_word}]".lower(), "")
        input = input.replace(bad_word, "")
    return input


def _confident_in(word, ai_text) -> Tuple[bool, str]:
    if f"[[{word}]]" in ai_text:
        return True, _reponse_after(f"[[{word}]]", ai_text)
    if f"[{word}]" in ai_text:
        return True, _reponse_after(f"[{word}]", ai_text)
    return False, ""

def _uncondifent_in(word, ai_text) -> Tuple[bool, str]:
    if f"[[{word}]]".lower() in ai_text.lower():
        return True, _reponse_after(f"[[{word}]]", ai_text.lower())
    if f"[{word}]".lower() in ai_text.lower():
        return True, _reponse_after(f"[{word}]", ai_text.lower())
    return False, ""

def _very_unconfident_in(word, ai_text) -> Tuple[bool, str]:
    if word in ai_text:
        return True, _reponse_after(word, ai_text)
    if word.lower() in ai_text.lower():
        return True, _reponse_after(word.lower(), ai_text.lower())
    return False, ""


def was_success(ai_text:str) -> Tuple[bool,str]:
    for word in _good_variations:
        success, string = _confident_in(word, ai_text)
        if success:
            return success, string
    for word in _bad_variations:
        success, string = _confident_in(word, ai_text)
        if success:
            return False, string
    for word in _good_variations:
        success, string = _uncondifent_in(word, ai_text)
        if success:
            return success, string
    for word in _bad_variations:
        success, string = _uncondifent_in(word, ai_text)
        if success:
            return False, string
    for word in _bad_variations:
        success, string = _very_unconfident_in(word, ai_text)
        if success:
            return False, string
    for word in _good_variations:
        success, string = _very_unconfident_in(word, ai_text)
        if success:
            return success, string
    
    return True, "I don't fully get this joke but I think I like it"

def go():
    message = Message.rate_the_joke
    while True:
        print_blue(message.sendNoChat(get_start_text(False) + rate_the_joke()))
        joke = input("Enter joke >")
        if len(joke) < 15:
            response = message.sendNoChat(rate_joke_fail())
        else:
            q = "Act as if you are at an open mic night work event. Always respond with [[GOOD]] or [[BAD]]\
            your rating should always be the first line of your response then any follow up:" + joke
            response = message.sendNoChat(q)
        print_blue(response)
        success, msg = was_success(response)
        if success:
            print_green(_clean_string(msg))
            break
        else:
            print_red(_clean_string(msg))

if __name__ == "__main__":
    print(go())
          