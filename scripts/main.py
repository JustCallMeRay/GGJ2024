from Minigames.MiniGames import run_minigame 
from TextBasedAventure.TextBasedAdventure import start_adventure, continue_adventure

from Minigames import Punchline

if __name__ != "__main__":
    print("Running main as module is not supported. Please run \"main.py\"")
# Punchline.go()

start_adventure()
run_minigame()
continue_adventure()
