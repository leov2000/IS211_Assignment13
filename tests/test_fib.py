import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from recursion import fibonacci

class TestFib(unittest.TestCase):
    def setUp(self):
        self.fib_results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    def test_fibonacci_list(self):
        fib_list = [fibonacci(num) for num in range(14)]
        
        self.assertEqual(fib_list, self.fib_results)