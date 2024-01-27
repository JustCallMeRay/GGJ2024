def print_blue(text:str):
    print("\033[94m" + text + "\033[0m")

def print_green(text:str):
    print("\033[92m" + text + "\033[0m")

def print_red(text:str):
    print("\033[91m" + text + "\033[0m")

def ask(text:str):
    return input(text)