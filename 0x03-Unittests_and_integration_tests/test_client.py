#!/usr/bin/env python3
"""A py mddule
"""
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
import unittest
from typing import Dict
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    def test_org(self, org_name):
        with patch('client.get_json') as mock_get_json:
            # Mock the expected result of get_json
            mock_get_json.return_value = {"organization": org_name}

            # Create an instance of GithubOrgClient
            github_org_client = GithubOrgClient(org_name)

            # Call the org method
            result = github_org_client.org()

            # Assert that get_json was called once with the expected argument
            mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))

            # Assert that the result is the expected organization dictionary
            self.assertEqual(result, {"organization": org_name})

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        # Mock the payload returned by org
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

        # Create an instance of GithubOrgClient
        github_org_client = GithubOrgClient("testorg")

        # Call the _public_repos_url property
        result = github_org_client._public_repos_url

        # Assert that the result is the expected repos_url
        self.assertEqual(result, "https://api.github.com/orgs/testorg/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', return_value="https://api.github.com/orgs/testorg/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        # Mock the payload returned by get_json
        mock_get_json.return_value = [{"name": "repo1", "license": {"key": "my_license"}},
                                      {"name": "repo2", "license": {"key": "other_license"}}]

        # Create an instance of GithubOrgClient
        github_org_client = GithubOrgClient("testorg")

        # Call the public_repos method
        result = github_org_client.public_repos(license="my_license")

        # Assert that get_json was called once
        mock_get_json.assert_called_once()

        # Assert that the mocked property was called once
        mock_public_repos_url.assert_called_once()

        # Assert that the result is the expected list of repos
        self.assertEqual(result, ["repo1"])

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        # Create an instance of GithubOrgClient (it's a static method, so you can call it directly)
        result = GithubOrgClient.has_license(repo, license_key)

        # Assert that the result is as expected
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
