"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_instance_sdk
from kafka_instance_sdk.model.node import Node
from kafka_instance_sdk.model.partition_leader import PartitionLeader
globals()['Node'] = Node
globals()['PartitionLeader'] = PartitionLeader
from kafka_instance_sdk.model.partition import Partition


class TestPartition(unittest.TestCase):
    """Partition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPartition(self):
        """Test Partition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Partition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()