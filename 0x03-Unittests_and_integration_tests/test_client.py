#!/usr/bin/env python3
"""
Testing Module for client.py
"""
from client import GithubOrgClient

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Suite for GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """
        Tests that GithubOrgClient.org returns the correct value
        """
        api_url = f'https://api.github.com/orgs/{org_name}'
        mocked_inst = GithubOrgClient(org_name)
        mocked_inst.org()
        mock_json.assert_called_once_with(api_url)
