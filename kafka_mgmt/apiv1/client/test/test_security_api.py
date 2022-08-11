"""
    Kafka Management API

    Kafka Management API is a REST API to manage Kafka instances  # noqa: E501

    The version of the OpenAPI document: 1.11.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import kafka_mgmt_client
from kafka_mgmt_client.api.security_api import SecurityApi  # noqa: E501


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service_account(self):
        """Test case for create_service_account

        """
        pass

    def test_delete_service_account_by_id(self):
        """Test case for delete_service_account_by_id

        """
        pass

    def test_get_service_account_by_id(self):
        """Test case for get_service_account_by_id

        """
        pass

    def test_get_service_accounts(self):
        """Test case for get_service_accounts

        """
        pass

    def test_get_sso_providers(self):
        """Test case for get_sso_providers

        """
        pass

    def test_reset_service_account_creds(self):
        """Test case for reset_service_account_creds

        """
        pass


if __name__ == '__main__':
    unittest.main()
