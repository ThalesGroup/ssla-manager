import os.path
from pathlib import Path
from typing import List

import pytest

from sslamanager.parser.build import ServicePropertiesType, VariableType
from sslamanager.parser.build.specs.capability import CapabilityType
from sslamanager.parser.build.specs.security_metric import MetricType
from sslamanager.parser.build.specs.slo import Slotype
from sslamanager.parser.build.wsag import ServiceDescriptionTermType
from sslamanager.parser.ssla_parser import SSLAParser, SSLA, SLO, Metric, EnumUnit, EnumUnitItem, \
    IntervalUnit, ServiceProperties, ServiceProperty

SERVICE_NAME = "Secure Web Server"

SCHEMA_PATH = "../parser/templates/ssla/ssla_schema.xsd"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

ssla_test_path = Path(os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid.xml"))
ssla_invalid_path = Path(os.path.join(CURRENT_DIR, "../static/ssla_tls_server_invalid.xml"))


def test_ssla():
    ssla_data = ssla_test_path.read_bytes()

    # test parser
    ssla_parser = SSLAParser()
    assert ssla_parser is not None
    assert ssla_parser.parser is not None

    # test model
    ssla_model = ssla_parser.parse_from_content(ssla_data)
    assert ssla_model is not None
    assert ssla_model.ssla is not None

    # test ssla content
    services_test(ssla_model)
    capabilities_test(ssla_model)
    metrics_test(ssla_model)
    slo_test(ssla_model)
    properties_test(ssla_model)

    # test invalid
    expectedError: Exception
    ssla_invalid_data = ssla_invalid_path.read_bytes()
    with pytest.raises(Exception) as e:
        ssla_parser.parse_from_content(ssla_invalid_data)

    assert "invalid SSLA content" in str(e.value)


def services_test(ssla: "SSLA"):
    # test all services
    services: List["ServiceDescriptionTermType"] = ssla.get_services()
    assert len(services) == 1

    # test one service
    service: "ServiceDescriptionTermType" = ssla.get_service(SERVICE_NAME)
    assert service is not None
    assert service.service_name == SERVICE_NAME


def capabilities_test(ssla: "SSLA"):
    capabilities: List["CapabilityType"] = ssla.get_capabilities(SERVICE_NAME)
    assert capabilities is not None
    assert len(capabilities) == 2

    capabilities_ids = [capability.id for capability in capabilities]
    assert "TLS" in capabilities_ids
    assert "AAA" in capabilities_ids


def metrics_test(ssla: "SSLA"):
    metrics = ssla.get_metrics(SERVICE_NAME)
    assert metrics is not None
    assert len(metrics) == 11

    metric_id = "tls_crypto_strength"
    crypto_strength_metric: "MetricType" = metrics[0]
    assert crypto_strength_metric is not None
    assert crypto_strength_metric.reference_id == metric_id

    # test to request only one metric
    m = ssla.get_metric(service_name=SERVICE_NAME, metric_id=metric_id)
    assert crypto_strength_metric == m


def slo_test(ssla: "SSLA"):
    slos = ssla.get_slos()
    assert slos is not None
    assert len(slos) == 9

    crypto_strength_slo: "Slotype" = slos[0]
    assert crypto_strength_slo.metric_ref == "tls_crypto_strength"


def properties_test(ssla: "SSLA"):
    properties = ssla.get_service_properties(SERVICE_NAME)
    assert properties is not None
    assert len(properties) == 1

    p: "ServicePropertiesType" = properties[0]
    assert "TLS" in p.name
    assert SERVICE_NAME == p.service_name
    assert p.variable_set is not None

    variables: List["VariableType"] = p.variable_set.variable
    assert variables is not None
    assert len(variables) == 6

    variable1: VariableType = variables[0]
    assert variable1 is not None
    assert variable1.location is not None
    assert "CCM" in variable1.location.value
    assert "tls_crypto_strength" in variable1.metric


def test_slo_serialization():
    ssla_test_path = Path(os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid.xml"))
    ssla_data = ssla_test_path.read_bytes()
    ssla_parser = SSLAParser()

    # test SLO parser
    ssla_model = ssla_parser.parse_from_content(ssla_data)
    parsed_slos: List["SLO"] = ssla_model.get_slos_json()
    for slo_json_model in parsed_slos:
        assert slo_json_model is not None
        assert slo_json_model.id is not None
        assert slo_json_model.operator is not None
        assert slo_json_model.metricREF is not None
        assert slo_json_model.operands is not None

    assert len(parsed_slos) == 9
    slo1: "SLO" = parsed_slos[0]
    assert slo1.id == "tls_slo1"
    assert slo1.metricREF == "tls_crypto_strength"
    assert slo1.operands == ['7']
    assert slo1.operator == "eq"
    assert slo1.priority == "HIGH"

    slo2: "SLO" = parsed_slos[8]
    assert slo2.id == "aaa_slo3"
    assert slo2.metricREF == "aaa_log_completeness"
    assert slo2.operands == ['LOW', 'HIGH']
    assert slo2.operator == "in_included"
    assert slo2.priority == "LOW"


def test_metrics_serialization():
    ssla_test_path = Path(os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid.xml"))
    ssla_data = ssla_test_path.read_bytes()
    ssla_parser = SSLAParser()

    # test metrics parser
    ssla_model = ssla_parser.parse_from_content(ssla_data)
    parsed_metrics: List["Metric"] = ssla_model.get_metrics_json(SERVICE_NAME)
    for metric in parsed_metrics:
        assert metric.id is not None
        assert metric.definition is not None
        assert metric.unit_name is not None
        assert (metric.enum_unit is not None or metric.interval_unit is not None)
        if metric.enum_unit is not None:
            assert metric.interval_unit is None
            items: List["EnumUnitItem"] = metric.enum_unit.items
            assert items is not None
            for item in items:
                assert item.description is not None
                assert item.value is not None
        else:
            assert metric.enum_unit is None
            unit: "IntervalUnit" = metric.interval_unit
            assert unit.start is not None
            assert unit.stop is not None
            assert unit.step is not None

    assert len(parsed_metrics) == 11

    metric_id = 'tls_crypto_strength'
    metric1: Metric = parsed_metrics[0]
    assert metric1.id == metric_id
    unit: "IntervalUnit" = metric1.interval_unit
    assert unit.start == 0
    assert unit.stop == 8
    assert unit.step == 1
    assert unit.name == "hours"

    metric2: Metric = parsed_metrics[1]
    assert metric2.id == 'forward_secrecy'
    unit: "EnumUnit" = metric2.enum_unit
    assert unit.name == 'activation'
    assert len(unit.items) == 2
    assert unit.items[0].value == 'yes'
    assert unit.items[1].value == 'no'

    # test request only one
    m = ssla_model.get_metric_json(SERVICE_NAME, metric_id)
    assert m == metric1


def test_properties_serialization():
    ssla_test_path = Path(os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid.xml"))
    ssla_data = ssla_test_path.read_bytes()
    ssla_parser = SSLAParser()

    # test properties parser
    ssla_model = ssla_parser.parse_from_content(ssla_data)
    parsed_properties = ssla_model.get_service_properties_json(SERVICE_NAME)
    for props in parsed_properties:
        assert props.capability_id is not None
        assert props.service_name == SERVICE_NAME
        assert props.properties is not None
        for prop in props.properties:
            assert prop.name is not None
            assert prop.location is not None
            assert prop.metric is not None

    props1: "ServiceProperties" = parsed_properties[0]
    assert props1.capability_id == "TLS"

    prop1: "ServiceProperty" = props1.properties[0]
    assert prop1.name == "specs_TLS_M3"
    assert prop1.metric == "tls_crypto_strength"
    assert prop1.location == "//specs:CCMsecurityControl[@id='EKM-01']"
