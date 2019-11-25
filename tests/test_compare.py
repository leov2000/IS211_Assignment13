import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from recursion import compareTo

class TestCompareTo(unittest.TestCase):
    def setUp(self):
        self.compare_results = [-1, 0, 1, 1, 1, 0]

    def test_fibonacci_list(self):
        compare_list = [
            compareTo('hi', 'ih'),
            compareTo('hello', 'hello'),
            compareTo('goodbye', 'byegood'),
            compareTo('goodbye', 'bye'),
            compareTo('hi', 'hello'),
            compareTo('world', 'world')
        ]
        
        self.assertEqual(compare_list, self.compare_results)

    