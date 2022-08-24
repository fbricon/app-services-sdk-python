# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from dimakis_test_connector_mgmt_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dimakis_test_connector_mgmt_sdk.model.addon_parameter import AddonParameter
from dimakis_test_connector_mgmt_sdk.model.addon_parameter_list import AddonParameterList
from dimakis_test_connector_mgmt_sdk.model.channel import Channel
from dimakis_test_connector_mgmt_sdk.model.connector import Connector
from dimakis_test_connector_mgmt_sdk.model.connector_cluster import ConnectorCluster
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_list import ConnectorClusterList
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_list_all_of import ConnectorClusterListAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_meta import ConnectorClusterMeta
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_request import ConnectorClusterRequest
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_request_meta import ConnectorClusterRequestMeta
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_state import ConnectorClusterState
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_status import ConnectorClusterStatus
from dimakis_test_connector_mgmt_sdk.model.connector_cluster_status_status import ConnectorClusterStatusStatus
from dimakis_test_connector_mgmt_sdk.model.connector_configuration import ConnectorConfiguration
from dimakis_test_connector_mgmt_sdk.model.connector_desired_state import ConnectorDesiredState
from dimakis_test_connector_mgmt_sdk.model.connector_list import ConnectorList
from dimakis_test_connector_mgmt_sdk.model.connector_list_all_of import ConnectorListAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_meta import ConnectorMeta
from dimakis_test_connector_mgmt_sdk.model.connector_meta_all_of import ConnectorMetaAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_namespace import ConnectorNamespace
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_all_of import ConnectorNamespaceAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_eval_request import ConnectorNamespaceEvalRequest
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_list import ConnectorNamespaceList
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_list_all_of import ConnectorNamespaceListAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_meta import ConnectorNamespaceMeta
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_meta_all_of import ConnectorNamespaceMetaAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_patch_request import ConnectorNamespacePatchRequest
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_quota import ConnectorNamespaceQuota
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_request import ConnectorNamespaceRequest
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_request_all_of import ConnectorNamespaceRequestAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_request_meta import ConnectorNamespaceRequestMeta
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_state import ConnectorNamespaceState
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_status import ConnectorNamespaceStatus
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_tenant import ConnectorNamespaceTenant
from dimakis_test_connector_mgmt_sdk.model.connector_namespace_tenant_kind import ConnectorNamespaceTenantKind
from dimakis_test_connector_mgmt_sdk.model.connector_request import ConnectorRequest
from dimakis_test_connector_mgmt_sdk.model.connector_request_meta import ConnectorRequestMeta
from dimakis_test_connector_mgmt_sdk.model.connector_state import ConnectorState
from dimakis_test_connector_mgmt_sdk.model.connector_status import ConnectorStatus
from dimakis_test_connector_mgmt_sdk.model.connector_status_status import ConnectorStatusStatus
from dimakis_test_connector_mgmt_sdk.model.connector_type import ConnectorType
from dimakis_test_connector_mgmt_sdk.model.connector_type_all_of import ConnectorTypeAllOf
from dimakis_test_connector_mgmt_sdk.model.connector_type_list import ConnectorTypeList
from dimakis_test_connector_mgmt_sdk.model.connector_type_list_all_of import ConnectorTypeListAllOf
from dimakis_test_connector_mgmt_sdk.model.cpu_quota import CpuQuota
from dimakis_test_connector_mgmt_sdk.model.error import Error
from dimakis_test_connector_mgmt_sdk.model.kafka_connection_settings import KafkaConnectionSettings
from dimakis_test_connector_mgmt_sdk.model.list import List
from dimakis_test_connector_mgmt_sdk.model.memory_quota import MemoryQuota
from dimakis_test_connector_mgmt_sdk.model.object_meta import ObjectMeta
from dimakis_test_connector_mgmt_sdk.model.object_reference import ObjectReference
from dimakis_test_connector_mgmt_sdk.model.schema_registry_connection_settings import SchemaRegistryConnectionSettings
from dimakis_test_connector_mgmt_sdk.model.service_account import ServiceAccount
from dimakis_test_connector_mgmt_sdk.model.service_connection_settings import ServiceConnectionSettings
from dimakis_test_connector_mgmt_sdk.model.version_metadata import VersionMetadata
from dimakis_test_connector_mgmt_sdk.model.version_metadata_all_of import VersionMetadataAllOf
