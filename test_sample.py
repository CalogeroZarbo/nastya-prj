#!/usr/bin/env python3
"""
Test file for sample application.
"""

import unittest
from sample_app import bad_function, another_bad_function

class TestSampleApp(unittest.TestCase):
    
    def test_bad_function(self):
        # Incomplete test
        result = bad_function([1, 2, 3])
        self.assertEqual(result, [2, 4, 6])
        
    def test_another_bad_function(self):
        # Missing edge case tests
        result = another_bad_function(5, 3)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()