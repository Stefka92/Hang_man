"""
importing the package for the program
"""
import random


def hangman(word):
    """
    declaring the function hangman and passing word as a argument
    """

    wrong = 0   # declaring wrong and setting as 0 
    stages = [
     "",
     "________        ",
     "|               ", 
     "|        |      ",
     "|        0      ",
     "|       /|\     ",
     "|       / \     ",
     "|               "]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")   # displaying the message to the user 
    guesses = []
    while wrong < len(stages) - 1:   # if the user guess is less than -1 then 
        print("\n")
        msg = "Guess a letter: "   # asking the user to guess a letter 
        char = input(msg)   # getting the guessed letter as a input 
        if char in guesses:   # if the entered char matches with the word then, 
            print("You already guessed the letter '{}', try again.".format(char))
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
        print("Previous Guesses: {}".format(guesses))  # displaying the Previous guesses by the user 
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:  # if _ is not in board then print 
            print("You win!")  # telling to the user that he or she won 
            print(" ".join(board))
            win = True
            break
    if not win:  # if not in board then 
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))   

#  number of words declared 
words = ["python", "java", "kotlin", "javascript", "ruby", "c++", "c#", "swift", "go", "scala",
         "php", "perl", "r", "matlab", "julia", "groovy", "objective-c", "rust", "dart", "elixir"]

word = random.choice(words)
hangman(word)