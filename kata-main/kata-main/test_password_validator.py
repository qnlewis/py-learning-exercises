import unittest
from password_validator import is_password_secure

class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_password_secure("Valid123!"))

    def test_too_short_password(self):
        self.assertFalse(is_password_secure("Short1!"))

    def test_missing_uppercase(self):
        self.assertFalse(is_password_secure("missinguppercase1!"))

    def test_missing_number(self):
        self.assertFalse(is_password_secure("MissingNumber!"))

    def test_password_no_special_character(self):
        self.assertFalse(is_password_secure("10 I Want To Hold Your Hand"))

if __name__ == '__main__':
    unittest.main()