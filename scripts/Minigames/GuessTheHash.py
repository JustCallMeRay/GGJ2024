from random import randint
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
    return f"Tell the player to guess the hash function used to create the following number {number}"

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

if __name__ == "__main__":
    print(guess_the_hash())
    pi = input()
    print(run_guess_the_hash(pi))