"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.reserved_resource import ReservedResource
globals()['ReservedResource'] = ReservedResource
from account_management_sdk.model.cluster_authorization_request import ClusterAuthorizationRequest


class TestClusterAuthorizationRequest(unittest.TestCase):
    """ClusterAuthorizationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterAuthorizationRequest(self):
        """Test ClusterAuthorizationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterAuthorizationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()