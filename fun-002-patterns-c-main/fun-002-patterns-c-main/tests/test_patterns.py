# tests/test_patterns.py

import unittest
import patterns

class PatternsTestCases(unittest.TestCase):

    def test_square_height_7(self):
        expected = """*******
*******
*******
*******
*******
*******
*******"""
        self.assertEqual(patterns.draw_square(7), expected)

    def test_pyramid_height_3(self):
        expected = "  *\n ***\n*****"
        self.assertEqual(patterns.draw_pyramid(3), expected)

    def test_triangle_height_6(self):
        expected = "\n".join([
            "1",
            "12",
            "123",
            "1234",
            "12345",
            "123456"
        ])
        self.assertEqual(patterns.draw_triangle(6), expected)

    def test_triangle_reversed_9(self):
        expected = "\n".join([
            "987654321",
            "87654321",
            "7654321",
            "654321",
            "54321",
            "4321",
            "321",
            "21",
            "1"
        ])
        self.assertEqual(patterns.draw_triangle_reversed(9), expected)

    def test_triangle_prime_4(self):
        expected = "2\n3 5\n7 11 13\n17 19 23 29"
        self.assertEqual(patterns.draw_triangle_prime(4), expected)

    def test_is_prime_5(self):
        self.assertTrue(patterns.is_prime(5))

    def test_triangle_prime_7(self):
        result = patterns.draw_triangle_prime(7)
        lines = result.split('\n')
        self.assertEqual(len(lines), 7)
        self.assertEqual(lines[0], "2")
        self.assertEqual(lines[1], "3 5")
        self.assertEqual(lines[2], "7 11 13")

if __name__ == "__main__":
    unittest.main()