#!/usr/bin/python3
"""Unittests for max_integer function"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max(self):
        """Test function returns max value when elements are all positive"""
        self.assertEqual(max_integer([1, 2, 5, 4]), 5)

    def test_single_element(self):
        """Test function returns max value when only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_mixed_list(self):
        """Test function returns max value when elements are positive or negative"""
        self.assertEqual(max_integer([7, -7, 0]), 7)

    def test_all_negative(self):
        """Test function returns max value when elements are all negatives"""
        self.assertEqual(max_integer([-9, -7, -2]), -2)

    def test_empty_list(self):
        """Test function returns max value when list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_duplicate_values(self):
        """Test function returns max value when elements are all equal"""
        self.assertEqual(max_integer([7, 7, 7]), 7)


if __name__ == "__main__":
    unittest.main()
