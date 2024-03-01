# Wordle
import math
import random
import sys

## Add constants to modify color of terminal stdout
WRONG = "\033[31m"
CLOSE = "\033[103m"
CORRECT = "\033[32m"
RESET = "\033[39m"

def main():

    # Test usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: python3 wordle.py wordsize")

    wordsize = sys.argv[1]
    try:
        wordsize = int(sys.argv[1])
    except ValueError:
        sys.exit("Non-numeric argument provided")
    
    # Check this, need to be able to select from 5, 6 letter words
    if wordsize != 5 and wordsize != 6:
        sys.exit("Argument needs to be either the number 5 or 6")
    
    print(get_current_game_word(wordsize))

    print(get_user_guess(wordsize))

    print(WRONG+"BRAND"+RESET)

def get_current_game_word(wordsize):
    """Reads in list of 5 or 6 letter words based on user's wordsize argument
    and returns one word to be the current game word"""

    file = f"./input/{wordsize}.txt"
    word_bank = []
    with open(file, "r") as f:
        for line in f:
            word_bank.append(line.strip())
    random_index = math.floor(random.random() * 1000) 
    current_game_word = word_bank[random_index]

    return current_game_word

def get_user_guess(wordsize):

    user_guess = ""

    while len(user_guess) != wordsize or not check_correct_guess_format(user_guess):
        user_guess = input(f"Enter a {wordsize}-letter guess: ")

    return user_guess

def check_correct_guess_format(guess):

    for letter in guess:
        if not letter.isalpha():
            return False
        
    return True













if __name__ == "__main__":
    main()