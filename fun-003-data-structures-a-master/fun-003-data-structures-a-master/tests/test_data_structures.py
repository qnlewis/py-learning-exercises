import unittest
import data_structures

class TestDataStructures(unittest.TestCase):
    def test_find_max(self):
        self.assertTrue(data_structures.find_max([1, 2, 3, 4, 5]), 5)
    
    
    def test_find_min(self):
        self.assertTrue(data_structures.find_min([1, 2, 3, 4, 5]), 1)
    
    
    def test_find_average(self):
        self.assertTrue(data_structures.find_average([1, 2, 3, 4, 5]), 3.0)
    
    
    def test_find_even_pairs(self):
        self.assertTrue(data_structures.find_even_pairs([1, 3, 5]), [(0, 1), (1, 2)])
    
    
    def test_find_odd_pairs(self):
        self.assertTrue(data_structures.find_odd_pairs([1, 2, 5]), [(0, 1), (1, 2)])
    
    
    def test_find_number_of_even_numbers(self):
        self.assertTrue(data_structures.find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
    
    
    def test_find_number_of_odd_numbers(self):
        self.assertTrue(data_structures.find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
    
    
    def test_find_even_numbers(self):
        self.assertTrue(data_structures.find_even_numbers([1, 2, 3, 4, 5]), (2, 4))
    
    
    def test_find_odd_numbers(self):
        self.assertTrue(data_structures.find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
    
    
    def test_return_list_stats(self):
        self.assertTrue(data_structures.return_list_stats([1, 2, 3, 4, 5]), 
                        {'unique_numbers': {1, 2, 3, 4, 5}, 'max': 5, 'min': 1, 'average': 3.0,
                         'even_pairs': [], 'odd_pairs': [(0, 1), (1, 2), (2, 3), (3, 4)],
                         'even_numbers': (2, 4), 'odd_numbers': (1, 3, 5),
                         'number_of_even_numbers': 2, 'number_of_odd_numbers': 3})
        
        
