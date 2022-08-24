"""
    Service Registry Management API

    Service Registry Management API is a REST API for managing Service Registry instances. Service Registry is a datastore for event schemas and API designs, which is based on the open source Apicurio Registry project.  # noqa: E501

    The version of the OpenAPI document: 0.0.6
    Contact: rhosak-eval-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import rhoas_service_registry_mgmt_sdk
from rhoas_service_registry_mgmt_sdk.api.errors_api import ErrorsApi  # noqa: E501


class TestErrorsApi(unittest.TestCase):
    """ErrorsApi unit test stubs"""

    def setUp(self):
        self.api = ErrorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_error(self):
        """Test case for get_error

        """
        pass

    def test_get_errors(self):
        """Test case for get_errors

        """
        pass


if __name__ == '__main__':
    unittest.main()