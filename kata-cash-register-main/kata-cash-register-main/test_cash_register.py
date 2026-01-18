import unittest
from cash_register import change

class TestChange(unittest.TestCase):
    def test_change(self):
        self.assertEqual(change(100, 100), {})
        self.assertEqual(change(10000, 20000), {10000: 1})
        
if __name__ == '__main__':
    unittest.main()