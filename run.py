import random 
from words import random_words


def get_words():
    """
    This function generates a 
    random word for the user to guess.  
    """
    word = random.choices(random_words)
    return word.upper()

def play_game(words):
    """
    This function operates the main game,
    it allows the user 6 incorrect guesses before the man is hung.
    """
    completed_word = ["_"] * len(words)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("MY life depends on you.... No pressure\n")
    print(display_hangman_lives(tries))
    print(completed_word)
    

