from random import randint, choice
from OllamaInteractions import Message
from .PromptCreation.StartingPrompt import get_start_text
from InputOutput import print_blue, print_green, print_red

Hashes = ["GOST",
"HAS-160",
"HAS",
"HAVAL",
"MD2",
"MD4",
"MD5",
"RadioGatún",
"RIPEMD-64",
"RIPEMD-160",
"RIPEMD-320",
"RIPEMD",
"SHA-1",
"SHA-224",
"SHA-256",
"SHA-384",
"SHA-512",
"SHA",
"Skein",
"Snefru",
"Tiger",
"Whirlpool",
"FSB",
"ECOH",
"SWIFFT"]
Hashes = [ h.lower() for h in Hashes ]

# doesn't use wizard, all code
def guess_the_hash():
    number = str(randint(23_4231, 68_3271))
    return "Tell the player to guess the hash function used to create the following number {number}"

def _guess_the_hash_response(player_input:str):
    words = player_input.lower().split(" ");
    for word in words:
        if word in Hashes:
            return True
    for hash in Hashes:
        for word in words:
            if hash in word:
                # make it a bit easier
                return True
    return False

def _wizard_response(success:bool):
    if (success):
        return "Tell the player they did well and guessed the hash function correctly"
    else: 
        return "Tell the player they did not guess the hash and you are upset with them"

def run_guess_the_hash(player_input):
    # printed by ollama
    success = _guess_the_hash_response(player_input)
    return _wizard_response(success)


_wizard_names = ["Magnus Carlson", "Clembrior Smith", "Stagasgore Cook" ]

_mortal_adjectives = ["foolish", "unworthy", "powerless", "", "feeble", "pathetic", "puny", "pitiful", "insignificant" ]

_mortal_nouns = ["mortal", "human"]

_start_words = ["Ah!,", ""]

_output_text = [f"""You are jumped by an evil wizard: {choice(_start_words)} {choice(_mortal_adjectives).capitalize()} {choice(_mortal_nouns)}! Welcome to my realm, where I, {choice(_wizard_names)} , shall challenge your {choice(_mortal_adjectives)} intellect with a game I call "Guess The Hash!" Prepare yourself for the ultimate test of cryptographic prowess. I shall present you with a hash output, and you, {choice(_mortal_adjectives)} {choice(_mortal_nouns)}, must grope in the darkness of your {choice(_mortal_adjectives)} knowledge to identify the algorithm that created it.
Let the game commence, and may your {choice(_mortal_adjectives) } attempts amuse me! Here is your first challenge:
""", f"""{choice(_start_words)}, {choice(_mortal_adjectives) } {choice(_mortal_nouns)}! Prepare yourself for a game that will test the limits of your {choice(_mortal_adjectives)} intellect. I present to you "Guess The Hash!" You think you can decipher the cryptographic mysteries that I, {choice(_wizard_names)}, have concocted? Very well, let the game begin!""", 
f"""
{choice(_start_words)} {choice(_mortal_adjectives).capitalize()} {choice(_mortal_nouns)}! Prepare your {choice(_mortal_adjectives)} self for a game of intellect that surpasses your {choice(_mortal_adjectives)} understanding! I, {choice(_wizard_names)}, present to you the grand challenge – "Guess The Hash!" In this game, you will be given a mysterious output, a cryptographic enigma! Your task, {choice(_mortal_adjectives)} {choice(_mortal_nouns)}, is to fumble through the abyss of cryptographic knowledge and unveil the wretched algorithm that birthed the given hash."""]

def go():
    m = Message.guess_the_hash
    print_blue(m.sendNoChat(get_start_text(False) + guess_the_hash()))
    success = _guess_the_hash_response(input("Your guess >"))
    if success:
        print_green(m.sendNoChat(_wizard_response(success)))
    else:
        print_red(m.sendNoChat(_wizard_response(success)))
    return success

if __name__ == "__main__":
    print(go())