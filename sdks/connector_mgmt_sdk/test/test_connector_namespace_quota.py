"""
    Connector Management API

    Connector Management API is a REST API to manage connectors.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.model.cpu_quota import CpuQuota
from rhoas_connector_mgmt_sdk.model.memory_quota import MemoryQuota
globals()['CpuQuota'] = CpuQuota
globals()['MemoryQuota'] = MemoryQuota
from rhoas_connector_mgmt_sdk.model.connector_namespace_quota import ConnectorNamespaceQuota


class TestConnectorNamespaceQuota(unittest.TestCase):
    """ConnectorNamespaceQuota unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnectorNamespaceQuota(self):
        """Test ConnectorNamespaceQuota"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConnectorNamespaceQuota()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()