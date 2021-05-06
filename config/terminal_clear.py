import os


class Clear:
    """
    Clearing screen based on lambda function
    """
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')
