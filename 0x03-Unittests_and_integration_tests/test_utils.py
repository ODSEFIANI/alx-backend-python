#!/usr/bin/env python3
"""py module
"""
import unittest
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)  # Replace with your actual module name


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_exception_message
            ):
        """function
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check if the exception message matches the expected message
        self.assertEqual(str(context.exception), expected_exception_message)


if __name__ == "__main__":
    unittest.main()
