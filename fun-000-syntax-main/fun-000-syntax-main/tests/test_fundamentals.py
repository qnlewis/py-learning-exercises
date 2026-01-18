from unittest import TestCase
from io import StringIO
import fundamentals as fun
import sys
import test_my_tests
import inspect

class TestFunctions(TestCase):
    def test_get_date_of_birth(self):
        self.assertEqual(fun.get_date_of_birth('0004185035083'), '18/04/00')
        self.assertEqual(fun.get_date_of_birth('0111224903088'), '22/11/01')
        self.assertEqual(fun.get_date_of_birth('9809126723080'), '12/09/98')

    def test_get_gender(self):
        self.assertEqual(fun.get_gender('9106236034082'), 'Male')
        self.assertEqual(fun.get_gender('9402030894089'), 'Female')
        self.assertEqual(fun.get_gender('0312264983083'), 'Female')

    def test_get_citizenship(self):
        self.assertEqual(fun.get_citizenship('9407076583088'), 'South African')
        self.assertEqual(fun.get_citizenship('9210304503182'), 'Non-South African')
        self.assertEqual(fun.get_citizenship('0312264983083'), 'South African')
    
    def test_fizzbuzz_attribute_exists(self):
        self.assertTrue(hasattr(fun,"fizzbuzz"))

    def test_fizzbuzz(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        fun.fizzbuzz(20)
        expected_output = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\n"
        self.assertEqual(expected_output,text_capture.getvalue())
        
    def test_check_number_attributes_exists(self):
        obj = test_my_tests.MyTestCases()
        self.assertTrue(hasattr(obj,"test_check_number_odd_number"))
        self.assertTrue(hasattr(obj,"test_check_number_even_number"))
        self.assertTrue(hasattr(obj,"test_check_number_negative_even_number"))
        self.assertTrue(hasattr(obj,"test_check_number_negative_odd_number"))
        self.assertTrue(hasattr(obj,"test_check_number_neutral"))
        
    def test_methods_are_not_empty(self):
        test_methods = [method for method in dir(test_my_tests.MyTestCases) if method.startswith('test_')]
        for method in test_methods:
            method_obj = getattr(test_my_tests.MyTestCases, method)
            source = inspect.getsource(method_obj)

            if 'pass' in source and len(source.strip().split('\n')) <= 2:
                self.fail(f"Method {method} is empty or contains only 'pass'")