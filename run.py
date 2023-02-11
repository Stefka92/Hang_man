"""
importing the random words from words.py file
"""
import random
from words import words

def hangman(words):
    """
    declaring the function hangman and passing word as a argument
    """

    wrong = 0 # declaring wrong and settingas 0
    stages = [
        "",
     "________        ",
     "|               ", 
     "|        |      ",
     "|        0      ",
     "|       /|\     ",
     "|       / \     ",
     "|               "
     ]
    
     rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman, My life depends on you...\N")   # displaying the message to the user 
    guesses = []
    