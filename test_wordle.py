import unittest
import sys
from wordle import get_current_game_word

class TestGameWordLength(unittest.TestCase):
    '''Tests that the word read into the program and selected randomly
    is the same length as the user's wordlength argument in the CLI'''
    
    def test_five_letter_word(self):
        five_letter = len(get_current_game_word(5))
        self.assertEqual(five_letter, 5, "Length of word is incorrect")

    def test_six_letter_word(self):
        six_letter = len(get_current_game_word(6))
        self.assertEqual(six_letter, 6)


if __name__ == '__main__':
    unittest.main()