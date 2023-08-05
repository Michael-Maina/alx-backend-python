#!/usr/bin/env python3
"""
Testing Module for test_utils.py
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Suite for access_tested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Asserts if the return value of access_nested_map matches
        the expected result
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(expected_result, result)
