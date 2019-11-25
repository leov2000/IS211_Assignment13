import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from recursion import gcd

class TestGcd(unittest.TestCase):
    def setUp(self):
        self.gcd_results = [17, 10, 2, 1, 1, 2, 10, 17]

    def test_fibonacci_list(self):
        gcd_list = [
            gcd(68,119),
            gcd(2110, 1130),
            gcd(206, 40),
            gcd(1, 5),
            gcd(5, 1),
            gcd(40, 206),
            gcd(1130, 2110),
            gcd(119, 68)
        ]
        
        self.assertEqual(gcd_list, self.gcd_results)