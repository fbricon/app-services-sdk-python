"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.object_reference import ObjectReference
from account_management_sdk.model.registry_all_of import RegistryAllOf
globals()['ObjectReference'] = ObjectReference
globals()['RegistryAllOf'] = RegistryAllOf
from account_management_sdk.model.registry import Registry


class TestRegistry(unittest.TestCase):
    """Registry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegistry(self):
        """Test Registry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Registry()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()