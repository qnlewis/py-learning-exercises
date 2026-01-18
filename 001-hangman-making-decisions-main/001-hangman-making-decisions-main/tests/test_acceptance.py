import unittest
import sys
sys.path.append('/home/wtc6/001-hangman-making-decisions')
from unittest.mock import patch
from io import StringIO
from hangman import *

class mockobj(object):
    @classmethod
    def choice(cls,li):
        return 'python'
    
class TestHangmanGame(unittest.TestCase):

    # Test get_guess function
    @patch('builtins.input', return_value='a')
    def test_get_guess(self, mock_input):
        guess = get_guess()
        self.assertEqual(guess, 'a')

    # Test is_correct_guess function
    def test_is_correct_guess(self):
        self.assertTrue(is_correct_guess("python", 'p'))
        self.assertFalse(is_correct_guess("python", 'z'))

    # Test update_display function
    def test_update_display(self):
        word = "python"
        display = ["_"] * len(word)
        updated_display = update_display(word, 'p', display)
        self.assertEqual(updated_display, ['p', '_', '_', '_', '_', '_'])

        updated_display = update_display(word, 'y', updated_display)
        self.assertEqual(updated_display, ['p', 'y', '_', '_', '_', '_'])

    # Test is_not_correct_guess function
    @patch('sys.stdout', new_callable=StringIO)
    def test_is_not_correct_guess(self, mock_stdout):
        attempts = is_not_correct_guess(6)
        self.assertEqual(attempts, 5)
        self.assertEqual(mock_stdout.getvalue().strip(), "Incorrect! You have 5 attempts left.")

    # Test fully_guessed function
    def test_fully_guessed(self):
        self.assertTrue(fully_guessed(['p', 'y', 't', 'h', 'o', 'n']))
        self.assertFalse(fully_guessed(['p', '_', '_', '_', '_', '_']))

    # Test is_winner function
    def test_is_winner(self):
        self.assertEqual(is_winner(['p', 'y', 't', 'h', 'o', 'n'], "python"), "You won!")
        self.assertEqual(is_winner(['p', '_', '_', '_', '_', '_'], "python"), "You lost! The word was: python")

    # Test play_game function (integration test)
    @patch('builtins.input', side_effect=['p', 'y', 't', 'h', 'o', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_win(self, mock_stdout, mock_input):
        with patch('random.choice',mockobj.choice):
            play_game()
            output = mock_stdout.getvalue().strip()
            self.assertIn("You won!", output)

    @patch('builtins.input', side_effect=['a', 'b', 'c', 'd', 'e', 'f'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_lose(self, mock_stdout, mock_input):
        with patch('random.choice',mockobj.choice):
            play_game()
            output = mock_stdout.getvalue().strip()
            self.assertIn("You lost! The word was: python", output)

if __name__ == '__main__':
    unittest.main()