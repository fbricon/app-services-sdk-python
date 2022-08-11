"""
    Kafka Management API

    Kafka Management API is a REST API to manage Kafka instances  # noqa: E501

    The version of the OpenAPI document: 1.11.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kafka_mgmt_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from kafka_mgmt_client.exceptions import ApiAttributeError


def lazy_import():
    from kafka_mgmt_client.model.supported_kafka_size_bytes_value_item import SupportedKafkaSizeBytesValueItem
    globals()['SupportedKafkaSizeBytesValueItem'] = SupportedKafkaSizeBytesValueItem


class KafkaRequestAllOf(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'multi_az': (bool,),  # noqa: E501
            'reauthentication_enabled': (bool,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'cloud_provider': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'bootstrap_server_host': (str,),  # noqa: E501
            'admin_api_server_url': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'expires_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'failed_reason': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'instance_type': (str,),  # noqa: E501
            'instance_type_name': (str,),  # noqa: E501
            'kafka_storage_size': (str,),  # noqa: E501
            'max_data_retention_size': (SupportedKafkaSizeBytesValueItem,),  # noqa: E501
            'browser_url': (str,),  # noqa: E501
            'size_id': (str,),  # noqa: E501
            'ingress_throughput_per_sec': (str,),  # noqa: E501
            'egress_throughput_per_sec': (str,),  # noqa: E501
            'total_max_connections': (int,),  # noqa: E501
            'max_partitions': (int,),  # noqa: E501
            'max_data_retention_period': (str,),  # noqa: E501
            'max_connection_attempts_per_sec': (int,),  # noqa: E501
            'billing_cloud_account_id': (str,),  # noqa: E501
            'marketplace': (str,),  # noqa: E501
            'billing_model': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'multi_az': 'multi_az',  # noqa: E501
        'reauthentication_enabled': 'reauthentication_enabled',  # noqa: E501
        'status': 'status',  # noqa: E501
        'cloud_provider': 'cloud_provider',  # noqa: E501
        'region': 'region',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'name': 'name',  # noqa: E501
        'bootstrap_server_host': 'bootstrap_server_host',  # noqa: E501
        'admin_api_server_url': 'admin_api_server_url',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'expires_at': 'expires_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'failed_reason': 'failed_reason',  # noqa: E501
        'version': 'version',  # noqa: E501
        'instance_type': 'instance_type',  # noqa: E501
        'instance_type_name': 'instance_type_name',  # noqa: E501
        'kafka_storage_size': 'kafka_storage_size',  # noqa: E501
        'max_data_retention_size': 'max_data_retention_size',  # noqa: E501
        'browser_url': 'browser_url',  # noqa: E501
        'size_id': 'size_id',  # noqa: E501
        'ingress_throughput_per_sec': 'ingress_throughput_per_sec',  # noqa: E501
        'egress_throughput_per_sec': 'egress_throughput_per_sec',  # noqa: E501
        'total_max_connections': 'total_max_connections',  # noqa: E501
        'max_partitions': 'max_partitions',  # noqa: E501
        'max_data_retention_period': 'max_data_retention_period',  # noqa: E501
        'max_connection_attempts_per_sec': 'max_connection_attempts_per_sec',  # noqa: E501
        'billing_cloud_account_id': 'billing_cloud_account_id',  # noqa: E501
        'marketplace': 'marketplace',  # noqa: E501
        'billing_model': 'billing_model',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, multi_az, reauthentication_enabled, *args, **kwargs):  # noqa: E501
        """KafkaRequestAllOf - a model defined in OpenAPI

        Args:
            multi_az (bool):
            reauthentication_enabled (bool):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            status (str): Values: [accepted, preparing, provisioning, ready, failed, deprovision, deleting] . [optional]  # noqa: E501
            cloud_provider (str): Name of Cloud used to deploy. For example AWS. [optional]  # noqa: E501
            region (str): Values will be regions of specific cloud provider. For example: us-east-1 for AWS. [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            bootstrap_server_host (str): [optional]  # noqa: E501
            admin_api_server_url (str): The kafka admin server url to perform kafka admin operations e.g acl management etc. The value will be available when the Kafka has been fully provisioned i.e it reaches a 'ready' state. [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            expires_at (datetime, none_type): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            failed_reason (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            instance_type (str): [optional]  # noqa: E501
            instance_type_name (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            kafka_storage_size (str): Maximum data storage available to this Kafka. This is now deprecated, please use max_data_retention_size instead.. [optional]  # noqa: E501
            max_data_retention_size (SupportedKafkaSizeBytesValueItem): [optional]  # noqa: E501
            browser_url (str): [optional]  # noqa: E501
            size_id (str): [optional]  # noqa: E501
            ingress_throughput_per_sec (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            egress_throughput_per_sec (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            total_max_connections (int): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            max_partitions (int): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            max_data_retention_period (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            max_connection_attempts_per_sec (int): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            billing_cloud_account_id (str): [optional]  # noqa: E501
            marketplace (str): [optional]  # noqa: E501
            billing_model (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.multi_az = multi_az
        self.reauthentication_enabled = reauthentication_enabled
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, multi_az, reauthentication_enabled, *args, **kwargs):  # noqa: E501
        """KafkaRequestAllOf - a model defined in OpenAPI

        Args:
            multi_az (bool):
            reauthentication_enabled (bool):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            status (str): Values: [accepted, preparing, provisioning, ready, failed, deprovision, deleting] . [optional]  # noqa: E501
            cloud_provider (str): Name of Cloud used to deploy. For example AWS. [optional]  # noqa: E501
            region (str): Values will be regions of specific cloud provider. For example: us-east-1 for AWS. [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            bootstrap_server_host (str): [optional]  # noqa: E501
            admin_api_server_url (str): The kafka admin server url to perform kafka admin operations e.g acl management etc. The value will be available when the Kafka has been fully provisioned i.e it reaches a 'ready' state. [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            expires_at (datetime, none_type): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            failed_reason (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            instance_type (str): [optional]  # noqa: E501
            instance_type_name (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            kafka_storage_size (str): Maximum data storage available to this Kafka. This is now deprecated, please use max_data_retention_size instead.. [optional]  # noqa: E501
            max_data_retention_size (SupportedKafkaSizeBytesValueItem): [optional]  # noqa: E501
            browser_url (str): [optional]  # noqa: E501
            size_id (str): [optional]  # noqa: E501
            ingress_throughput_per_sec (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            egress_throughput_per_sec (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            total_max_connections (int): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            max_partitions (int): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            max_data_retention_period (str): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            max_connection_attempts_per_sec (int): This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead.. [optional]  # noqa: E501
            billing_cloud_account_id (str): [optional]  # noqa: E501
            marketplace (str): [optional]  # noqa: E501
            billing_model (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.multi_az = multi_az
        self.reauthentication_enabled = reauthentication_enabled
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
