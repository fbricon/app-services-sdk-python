"""
    Kafka Management API

    Kafka Management API is a REST API to manage Kafka instances  # noqa: E501

    The version of the OpenAPI document: 1.11.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_mgmt_client
from kafka_mgmt_client.model.supported_kafka_size_bytes_value_item import SupportedKafkaSizeBytesValueItem
globals()['SupportedKafkaSizeBytesValueItem'] = SupportedKafkaSizeBytesValueItem
from kafka_mgmt_client.model.supported_kafka_size import SupportedKafkaSize


class TestSupportedKafkaSize(unittest.TestCase):
    """SupportedKafkaSize unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSupportedKafkaSize(self):
        """Test SupportedKafkaSize"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SupportedKafkaSize()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
