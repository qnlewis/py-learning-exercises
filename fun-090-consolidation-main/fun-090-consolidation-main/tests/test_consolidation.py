import unittest
import consolidation 

import sys
from io import StringIO


class TestConsolidation(unittest.TestCase):
    
    def test_fibonacci_basic(self):
        """Test basic fibonacci sequence generation"""

        self.assertEqual(consolidation.fibonacci(5), [0, 1, 1, 2, 3])
        
    def test_factorial_basic(self):
        """Test basic factorial calculation"""
        
        self.assertEqual(consolidation.factorial(5), 120)  
        
    def test_count_letters_and_punctuation_basic(self):
        """Test basic letter and punctuation counting"""
     
        result = consolidation.count_letters_and_punctuation("Hello, World!")
        expected = {'!': 1, ',': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
        self.assertEqual(len(result), len(expected))
        for key, value in expected.items():
            self.assertIn(key, result)
            self.assertEqual(result[key], value)
        
    def test_count_perfect_squares_basic(self):
        """Test basic perfect square counting"""

        self.assertEqual(consolidation.count_perfect_squares_in_list([4, 9, 16, 17]), 3)
        
    def test_draw_triangle_prime_basic(self):
        """Test basic prime triangle drawing"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        consolidation.draw_triangle_prime(3)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Should contain prime numbers in triangle format
        self.assertIn("2", output)
        self.assertIn("3 5", output)
        
    def test_matrix_multiply_basic(self):
        """Test basic matrix multiplication"""
        
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        
        result = consolidation.matrix_multiply(matrix1, matrix2)
        expected = [[58, 64], [139, 154]]
        
        self.assertEqual(result, expected)
        
    def test_is_palindrome_iterative_basic(self):
        """Test basic palindrome checking"""
        
        self.assertTrue(consolidation.is_palindrome_iterative("madam"))
        self.assertFalse(consolidation.is_palindrome_iterative("hello"))


if __name__ == '__main__':
    unittest.main()