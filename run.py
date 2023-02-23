"""
importing the random words from words.py file
"""
import random
import colorama
from colorama import Fore, Style
from words import words


colorama.just_fix_windows_console()

stages = [
    """
 +----+
 |    |
 O    |
      |
      |
      |
=========
     """,
    """
 +----+
 |    |
 O    |
 |    |
      |
      |
=========
    """,
    """
 +----+
 |    |
 O    |
/|    |
      |
      |
=========
    """,
    """
 +----+
 |    |
 O    |
/|\\  |
      |
      |
=========
    """,
    """
 +----+
 |    |
 O    |
/|\\  |
/     |
      |
=========
    """,
    """
 +----+
 |    |
 X    |
/|\\  |
/ \\  |
      |
=========
    """
]


def create_username():
    """
    allows user to create a username
    """
    return input("Enter your username:").lower()


username = create_username()
print("Welcome:", username)


def hangman(words, stages):
    """
    declaring the function hangman and passing word as a argument
    """

    wrong = 0  # declaring wrong and settingas 0
    rletters = list(words)
    board = ["_"] * len(words)
    win = False
    print("Welcome to Hangman, My life depends on you...\n")
    guesses = []
    hint_used = False
    while wrong < len(stages):   # if the user guess is less than -1 then
        print("\n")
        e = wrong + 1
        if e < len(stages):
            print("\n".join(stages[0: e]))
        print((" ".join(board)))
        print(Fore.BLUE + "Attempts remaining: {}/{}".format(
         len(stages) - 1 - wrong, len(stages) - 1) + Style.RESET_ALL)
        print(Fore.RED + "Previous Guesses:{}".format(
         guesses
        ) + Style.RESET_ALL)
        msg = (Fore.YELLOW + "Guess a letter,hint, or word:" + Style.RESET_ALL)
        char = input(msg)   # getting the guessed letter as a input

        if char == "hint":  # provides a hint to the user
            if not hint_used:
                hint = [la for la in rletters if la not in guesses]
                print("hint:A letter not yet guessed is'{}'".format(hint[0]))
                hint_used = True
                continue
            else:
                print("The hint has already been used.")
                continue

        if len(char) > 1:
            if char == words:
                print("Congratulations!You guessed the word {}!".format(words))
                win = True
                board = list(words)
                break
            else:
                print("Incorrect word try again")
                wrong += 1
                continue

        if set(board) == set(words):
            print("Congratulations! You guessed the word {}!".format(words))
            win = True
            break

        if not char.isalpha():  # if the entered char is not a letter
            print("Invalid input.Enter a single letter, the word, or 'hint'.")
            continue

        if len(char) > len(words):
            print("Incorrect word. Try again.")
            if wrong < len(stages) - 1:
                wrong += 1
            continue

        if char in guesses:   # if the entered char matches with the word then,
            print("You already guessed the letter '{}',try again".format(char))
            continue

        guesses.append(char)
        if char in rletters:
            cinds = [i for i, letter in enumerate(rletters) if letter == char]
        else:
            cinds = []
        for cind in cinds:
            board[cind] = char
            rletters[cind] = '$'
        else:
            if char not in words:
                wrong += 1
                print("wrong guess!The letter '{}' is not in the word.".format(char))
       
        if "_" not in board and wrong < len(stages) - 1:
            print("You win!")  # telling to the user that they won
            print(" ".join(board))
            win = True
            break

    if not win:  # if out of guesses show correct answer
        print("\n".join(stages[0: wrong]))
        print("You lose! The word was {}.".format(words))


def play_again():
    """
    Asks the user if they want to play again
    """
    response = input("Would to play again? (yes/no) ").lower()
    if response == "yes":
        hangman(words, stages)
    elif response == "no":
        print("Thanks for playing!Come back soon")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again()


words = random.choice(words)
hangman(words, stages)
play_again()
