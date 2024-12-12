#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map.

This module contains unit tests for the `access_nested_map` function
from the `utils` module. It uses parameterized inputs to test the
function with various cases.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function.

    This class contains unit tests to verify that the access_nested_map
    function works correctly for various nested dictionary structures.
    """

    @parameterized.expand([
        ("Test case 1", {"a": 1}, ("a",), 1),
        ("Test case 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Test case 3", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, _: str, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any
    ) -> None:
        """
        Test access_nested_map with various inputs.

        Args:
            _ (str): Test case description (ignored in assertions).
            nested_map (Dict[str, Any]): The nested dictionary to query.
            path (Tuple[str, ...]): The path to access in the dictionary.
            expected (Any): The expected value at the path.

        Asserts:
            The value at the specified path matches the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
