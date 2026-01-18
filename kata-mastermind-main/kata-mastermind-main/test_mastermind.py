import unittest
from mastermind import compare_codes

class MasterMind(unittest.TestCase):
    def testing(self):
        self.assertEqual(compare_codes('1233', '1234'), (3, 0))
        self.assertEqual(compare_codes('1233', '1233'), (4, 0))
        self.assertEqual(compare_codes('1233', '1333'), (3, 0))

if __name__ == '__main__':
    unittest.main()