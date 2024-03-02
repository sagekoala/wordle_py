# Wordle
import math
import random
import sys

## Add constants to modify color of terminal stdout
WRONG = "\033[31m"
CLOSE = "\033[33m"
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
    
    # Get words
    current_game_word = get_current_game_word(wordsize)

    # Send current words to play round function
    rounds = wordsize + 1
    result = play_game(current_game_word, rounds, wordsize)

    print(result)


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

def get_user_guess(wordsize, rounds):

    user_guess = ""

    while not check_correct_guess_format(user_guess, wordsize):
        user_guess = input(f"{rounds} guesses remaining - Enter a {wordsize}-letter guess: ").lower()

    return user_guess

def check_correct_guess_format(guess, wordsize):

    if len(guess) != wordsize:
        return False

    for letter in guess:
        if not letter.isalpha():
            return False
        
    return True

def display_guess_correctness(guess, current_game_word):

    if guess == current_game_word:
        print(CORRECT+guess+RESET)
        return True

    for i, letter in enumerate(guess):
        if letter == current_game_word[i]:
            print(CORRECT+letter+RESET, end="")
        elif letter_in_word(letter, current_game_word):
            print(CLOSE+letter+RESET, end="")
        else:
            print(WRONG+letter+RESET, end="")

    print()

    return False

def letter_in_word(guess_letter, current_game_word):

    for c in current_game_word:
        if c == guess_letter:
            return True
        
    return False

def play_game(current_game_word, rounds, wordsize):

    while rounds > 0:
        user_guess = get_user_guess(wordsize, rounds)
        correct = display_guess_correctness(user_guess, current_game_word)
        
        if correct:
            return f"You won! The correct guess was {current_game_word}"
        rounds -= 1

    return f"You ran out of guesses! The correct guess was {current_game_word}"

if __name__ == "__main__":
    main()