import unittest
from number_representations import to_roman_numeral

class TestToRomanNumeral(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(to_roman_numeral(1), 'I')
        self.assertEqual(to_roman_numeral(4), 'IV')
        self.assertEqual(to_roman_numeral(9), 'IX')
        self.assertEqual(to_roman_numeral(58), 'LVIII')
        self.assertEqual(to_roman_numeral(1994), 'MCMXCIV')
        self.assertEqual(to_roman_numeral(3999), 'MMMCMXCIX')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            to_roman_numeral(0)
        with self.assertRaises(ValueError):
            to_roman_numeral(-1)
        with self.assertRaises(ValueError):
            to_roman_numeral("1000")
        with self.assertRaises(ValueError):
            to_roman_numeral(3.14)

if __name__ == '__main__':
    unittest.main()