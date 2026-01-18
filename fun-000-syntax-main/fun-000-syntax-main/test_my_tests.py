import unittest
import fundamentals


class MyTestCases(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello, World!", "Hello, World!")
        
    def test_check_number_odd_number(self):
        result = fundamentals.check_number(3)
        assert result == 'Weird', f"Expected 'Weird', but got {result}"
    
    def test_check_number_even_number(self):
        result = fundamentals.check_number(4)
        assert result == 'Not Weird', f"Expected 'Not Weird', but got {result}"
    
    def test_check_number_negative_even_number(self):
        result = fundamentals.check_number(-2)
        assert result == 'Very weird', f"Expected 'Very weird', but got {result}"
        
    def test_check_number_negative_odd_number(self):
        result = fundamentals.check_number(-3)
        assert result == 'Extremely Weird', f"Expected 'Extremely Weird', but got {result}"    
        
    def test_check_number_neutral(self):
        result = fundamentals.check_number(0)
        assert result == 'Neutral', f"Expected 'Neutral', but got {result}"
    


if __name__ == "__main__":
    unittest.main()