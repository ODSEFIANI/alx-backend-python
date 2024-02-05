#!/usr/bin/env python3
"""py module
"""
from unittest.mock import patch, Mock
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)  # Replace with your actual module name


class TestAccessNestedMap(unittest.TestCase):
    """class
    """
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
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """checks ifts raise the same error"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Json TEST HTTTP"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """py function
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return the mock_response
        with patch('your_module_name.requests.get', return_value=mock_response) as mock_get:
            # Call the get_json function
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with the test_url
            mock_get.assert_called_once_with(test_url)

            # Assert that the result of get_json is equal to the test_payload
            self.assertEqual(result, test_payload)