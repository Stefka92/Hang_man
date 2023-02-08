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
    while not guessed and tries > 0:
        guess = input ("Please guess a letter").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("WHoops it looks like you have already guessed that please try again")
            elif guess not in word:
                print(guess, "not in word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Bravo", guess, "is correct")
                guessed_letters.append(guess)

        elif len('guess') == len('word') and guess.isalpha():

        else:
        print("Not valid try again\n")
            print(display_hangman_lives(tries))
            print(completed_word)
    

