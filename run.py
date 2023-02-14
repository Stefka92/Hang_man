"""
importing the random words from words.py file
"""
import random
from words import words
import colorama
from colorama import Fore, Style

colorama.just_fix_windows_console()


def create_username():
    """
    allows user to create a username
    """
    return input("Enter your username:").lower()


username = create_username()
print("Welcome:", username)


def hangman(words):
    """
    declaring the function hangman and passing word as a argument
    """

    wrong = 0  # declaring wrong and settingas 0
    stages = [
        """
 +----+
 |    |
      |
      |
      |
      |
=========
""",
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
/|\   |
      |
      |
=========
""",
"""
 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========
""",
"""
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========
"""
     ]
 
    rletters = list(words)
    board = ["_"] * len(words)
    win = False
    print("Welcome to Hangman, My life depends on you...\n")   # displaying the message to the user 
    guesses = []
    hint_used = False
    while wrong < len(stages) - 1:   # if the user guess is less than -1 then 
        print("\n")
        msg = (Fore.YELLOW + "Please guess a letter, type 'hint' for a hint, or guess the word: "+ Style.RESET_ALL)
        char = input(msg)   # getting the guessed letter as a input

        if char == "hint": # provides a hint to the user
            if not hint_used:
                hint = [l for l in rletters if l not in guesses]
                print("Here's a hint: one of the letters not yet guessed is '{}'".format(hint[0]))
                hint_used = True
                continue
            else:
                print("The hint has already been used.")
                continue

        if len(char) > 1:
            print("Incorrect word try again")
            wrong += 1
            continue

        if char == words: # if you guess the correct word
            print("congratulations! You guessed correctly")
            win = True
            break

        if not char.isalpha(): # if the entered char is not a letter
            print("Invalid input. Please enter a single letter, the word, or 'hint'.")
            continue

        if len(char) > 1 and char != words:
            print("Invalid input. Please enter a single letter, the word, or 'hint'.")
            continue

        if char in guesses:   # if the entered char matches with the word then, 
            print("Whoops you already guessed the letter '{}', try again.".format(char))
            continue

        guesses.append(char)
        if char in rletters:  # if the character in the rletters then 
            cind = rletters.index(char) 
            board[cind] = char
            rletters[cind] = '$'
        else:  # if the character is not in the rletters then 
            wrong += 1   # update the wrong value by 1 
        print((" ".join(board)))
        print("Attempts remaining: {}/{}".format(len(stages) - 1 - wrong, len(stages) - 1))   # printing the attempts remaining
        print(Fore.RED +"Previous Guesses: {}".format(guesses)+ Style.RESET_ALL)  # displaying the Previous guesses by the user 
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board and wrong < len(stages) -1:  # if _ is not in board and number of attemps not exceeded
            print("You win!")  # telling to the user that they won 
            print(" ".join(board))
            win = True
            break
    if not win:  # if out of guesses show correct answer 
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(words))


def play_again():
    """
    Asks the user if they want to play again
    """
    response = input("Would to play again? (yes/no) ").lower()
    if response == "yes":
        hangman(words)
    elif response == "no":
        print("Thanks for playing!Come back soon")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again()


words = random.choice(words)
hangman(words)
play_again()
