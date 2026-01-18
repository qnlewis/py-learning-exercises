# This where you implement the following test cases: Decimal = 2 decimal places
import unittest
from simple_interest import calculate_simple_interest

class TestSimpleInterest(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(calculate_simple_interest(5000, 5, 2), 500.00)

    def test_zero_values(self):
        self.assertEqual(calculate_simple_interest(0, 0, 0), 0.00)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest(-5000, -5, -2)

    def test_large_values(self):
        result = calculate_simple_interest(5000000000, 5000000000, 5000000000)
        self.assertIsInstance(result, float)
        self.assertEqual(round(result, 2), result)

    def test_decimal_values(self):
        self.assertEqual(calculate_simple_interest(5000.50, 5.50, 2.50), 687.57)

    def test_string_values(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest("R 5000", "5%", "2 yrs")

    def test_invalid_interest(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest(5000, "five%", 2)

    def test_invalid_principle(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest("Four thousands", 6, 2)

    def test_invalid_time(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest(4000, 6, "two")

    def test_mixed_values(self):
        self.assertEqual(calculate_simple_interest(5000, 5.50, 2), 550.00)

if __name__ == "__main__":
    unittest.main()