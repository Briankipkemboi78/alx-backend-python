#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map
"""

import unittest
from parameterized import expand
from utils import access_nested_map



class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function
    """

    @expand([
        ("Test case 1", {"a": 1}, ("a",), 1),
        ("Test case 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Test case 3", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, _, nested_map, path, expected ):
        """
        Tesst access_nested_map with various inputs
        """
        self.assertEqual(access_nested_map(nested_map), expected)

if __name__ == "__main__":
    unittest.main()