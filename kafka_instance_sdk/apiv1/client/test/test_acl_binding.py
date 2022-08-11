"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_instance_sdk
from kafka_instance_sdk.model.acl_binding_all_of import AclBindingAllOf
from kafka_instance_sdk.model.acl_operation import AclOperation
from kafka_instance_sdk.model.acl_pattern_type import AclPatternType
from kafka_instance_sdk.model.acl_permission_type import AclPermissionType
from kafka_instance_sdk.model.acl_resource_type import AclResourceType
from kafka_instance_sdk.model.object_reference import ObjectReference
globals()['AclBindingAllOf'] = AclBindingAllOf
globals()['AclOperation'] = AclOperation
globals()['AclPatternType'] = AclPatternType
globals()['AclPermissionType'] = AclPermissionType
globals()['AclResourceType'] = AclResourceType
globals()['ObjectReference'] = ObjectReference
from kafka_instance_sdk.model.acl_binding import AclBinding


class TestAclBinding(unittest.TestCase):
    """AclBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAclBinding(self):
        """Test AclBinding"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AclBinding()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()