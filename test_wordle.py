import unittest
import sys
from wordle import get_current_game_word, check_correct_guess_format, letter_in_word, play_game
from unittest.mock import patch, Mock

class TestGameWordLength(unittest.TestCase):
    '''Tests that the word read into the program and selected randomly
    is the same length as the user's wordlength argument in the CLI'''
    
    def test_five_letter_word(self):
        five_letter = len(get_current_game_word(5))
        self.assertEqual(five_letter, 5, "Length of word is incorrect")

    def test_six_letter_word(self):
        six_letter = len(get_current_game_word(6))
        self.assertEqual(six_letter, 6)

class TestGuessFormatCorrectness(unittest.TestCase):
    '''Tests format of user provided input'''

    def test_incorrect_guess_format(self):
        guess_format = check_correct_guess_format("hel9p", 5)
        self.assertEqual(guess_format, False)

    def test_incorrect_guess_format_space(self):
        guess_format_space = check_correct_guess_format("app l", 5)
        self.assertEqual(guess_format_space, False)

    def test_incorrect_guess_len(self):
        guess_format_len = check_correct_guess_format("brandonismyname", 5)
        self.assertEqual(guess_format_len, False)

    def test_correct_guess_format(self):
        guess_format = check_correct_guess_format("abcde", 5)
        self.assertEqual(guess_format, True)

class TestLetterInWord(unittest.TestCase):

    def test_no_letters(self):
        no_letters = letter_in_word('b', "dream")
        self.assertEqual(no_letters, False)

    def test_one_letter(self):
        one_letter = letter_in_word('a', "brain")
        self.assertEqual(one_letter, True)

    def test_same_letter_more_than_once(self):
        same_letter_multiple = letter_in_word('p', "apple")
        self.assertEqual(same_letter_multiple, True)

if __name__ == '__main__':
    unittest.main()