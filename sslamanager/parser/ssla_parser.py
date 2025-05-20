import logging
import os.path
import re
from pathlib import Path
from typing import List, Optional

from lxml import etree
from pydantic import BaseModel
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from sslamanager.exceptions import SSLASLOException, SSLAFormatException, SSLAValidationException, SSLAMetricsException
from sslamanager.parser.build import ServicePropertiesType
from sslamanager.parser.build.specs import TwoOpOperator, UnitType
from sslamanager.parser.build.specs.security_metric import MetricType
from sslamanager.parser.build.specs.slo import SloexpressionType, Slotype, OneOpOperator
from sslamanager.parser.build.wsag import AgreementOffer, ServiceDescriptionTermType

logger = logging.getLogger("uvicorn.default")


class ServiceDescription(BaseModel):
    service_name: str
    capabilities: List[str]


class ServiceProperty(BaseModel):
    name: str
    metric: str
    # location is the reference of the metric in Security Framework provided by the SSLA
    # example: //specs:CCMsecurityControl[@id='EKM-01']
    location: str


class ServiceProperties(BaseModel):
    capability_id: str
    service_name: str
    properties: List["ServiceProperty"]


class ServicePropertiesParser(object):

    @staticmethod
    def parse_capability_id(service_property_name: str) -> str:
        match = re.search(r"@id='([^']+)'", service_property_name)
        return match.group(1) if match else None

    @staticmethod
    def to_json_model(service_property: "ServicePropertiesType") -> "ServiceProperties":
        parsed_properties: List["ServiceProperty"] = []
        for variable in service_property.variable_set.variable:
            parsed_properties.append(ServiceProperty(name=variable.name,
                                                     metric=variable.metric,
                                                     location=variable.location.value))

        return ServiceProperties(capability_id=ServicePropertiesParser.parse_capability_id(service_property.name),
                                 service_name=service_property.service_name,
                                 properties=parsed_properties)


class MetricUnit(BaseModel):
    name: str


class IntervalUnit(MetricUnit):
    start: int
    stop: int
    step: int


class EnumUnitItem(BaseModel):
    value: str
    description: str


class EnumUnit(MetricUnit):
    items: List["EnumUnitItem"]


class Metric(BaseModel):
    id: str  # referenceId in SSLA
    definition: str
    enum_unit: Optional["EnumUnit"]
    interval_unit: Optional["IntervalUnit"]
    unit_name: str


class MetricParser:

    @staticmethod
    def to_json_model(metric: "MetricType"):
        """
        This function helps to parse the MetricType into a pydantic model being jsonable
        """
        unit: "UnitType" = metric.metric_definition.unit
        # a unit is 'enum' or 'interval' type
        # both can be null
        enum_unit: Optional["EnumUnit"]
        interval_unit: Optional["IntervalUnit"]
        if unit.enum_unit is not None:
            items: List["EnumUnitItem"] = []
            for item in unit.enum_unit.enum_items.enum_item:
                items.append(EnumUnitItem(value=item.value,
                                          description=item.description))
            enum_unit = EnumUnit(name=unit.name,
                                 items=items)
            interval_unit = None
        elif unit.interval_unit is not None:
            interval_unit = IntervalUnit(name=unit.name,
                                         start=unit.interval_unit.interval_item_start,
                                         stop=unit.interval_unit.interval_item_stop,
                                         step=unit.interval_unit.interval_item_step)
            enum_unit = None
        else:
            raise SSLAMetricsException(f"metric unit type unknown for metric '{metric.reference_id}'")

        return Metric(id=metric.reference_id,
                      definition=metric.metric_definition.definition,
                      enum_unit=enum_unit,
                      interval_unit=interval_unit,
                      unit_name=unit.name)


class SLO(BaseModel):
    id: str
    metricREF: str
    priority: Optional[str]
    operator: str
    operands: List[str]


class SLOParser:
    """
    Parser that helps to handle the SLO data in an SSLA
    It is useful for json parsing for example
    """

    def __init__(self, slo_from_xml):
        self.slo_xml = slo_from_xml

    def get_slo_id(self) -> str:
        return self.slo_xml.attributes['SLO_ID']

    def get_slo_priority(self) -> Optional[str]:
        ret = self.slo_xml.children[2].text
        if not ret:
            raise SSLASLOException("Unable to parse priority")
        return ret

    def get_slo_operator(self) -> str:
        ret = str(self.slo_xml.children[1].children[0].children[0].text)
        if not ret:
            raise SSLASLOException("Unable to parse operator")
        return ret

    def get_slo_operands(self) -> List[str]:
        # the number of operands is equal to the list of slo's operator childrens list - 1
        # because the first index references the operator
        num_operands = len(self.slo_xml.children[1].children[0].children) - 1
        ret: List[str] = []
        for i in range(1, num_operands + 1):
            ret.append(self.slo_xml.children[1].children[0].children[i].text)
        if not ret:
            raise SSLASLOException("Unable to parse operand")
        return ret

    def get_slo_metric_ref(self) -> str:
        ret = self.slo_xml.children[0].text
        if not ret:
            raise SSLASLOException("Unable to parse metricRef")
        return ret

    def is_one_op_expression(self) -> bool:
        qname = self.slo_xml.children[1].children[0].qname
        # if the qname string contains the substring "OneOpExpression"
        return "oneOpExpression" in qname

    def is_two_op_expression(self) -> bool:
        qname = self.slo_xml.children[1].children[0].qname
        # if the qname string contains the substring "OneOpExpression"
        return "twoOpExpression" in qname

    def parse(self) -> "Slotype":
        """
        This function helps to parse the xml element in SSLA into a Slotype of the compiled class from the xsd files.
        It is needed because the actual parsing returns them as "AnyElement" type instead of Slotype.
        """
        expression: Optional["SloexpressionType"] = None
        if self.is_one_op_expression():
            operator = OneOpOperator(self.get_slo_operator())
            operands = self.get_slo_operands()
            one_op_expression = SloexpressionType.OneOpExpression(operator=operator, operand=operands[0])
            expression = SloexpressionType(one_op_expression=one_op_expression)
        elif self.is_two_op_expression():
            operator = TwoOpOperator(self.get_slo_operator())
            operands = self.get_slo_operands()
            two_op_expression = SloexpressionType.TwoOpExpression(operator=operator, operand1=operands[0],
                                                                  operand2=operands[1])
            expression = SloexpressionType(two_op_expression=two_op_expression)

        return Slotype(metric_ref=self.get_slo_metric_ref(),
                       sloexpression=expression,
                       importance_weight=self.get_slo_priority(),
                       slo_id=self.get_slo_id())

    @staticmethod
    def to_json_model(slo_type: "Slotype") -> "SLO":
        """
        This function helps to parse the Slotype into a pydantic model being jsonable
        """
        if slo_type.sloexpression.one_op_expression is not None:
            exp = slo_type.sloexpression.one_op_expression
            operands = [exp.operand]
            operator = exp.operator.value
        elif slo_type.sloexpression.two_op_expression is not None:
            exp = slo_type.sloexpression.two_op_expression
            operands = [exp.operand1, exp.operand2]
            operator = exp.operator.value
        else:
            raise Exception(f"unknown operand type in SLO: {slo_type.slo_id}")

        return SLO(id=slo_type.slo_id,
                   metricREF=slo_type.metric_ref,
                   operator=operator,
                   operands=operands,
                   priority=slo_type.importance_weight)


class SSLA:
    """
    This class has two goals :
      - wrap the SSLA XML schema entry point's model class
      - define methods to look for useful fields in the SSLA (and not the entire model)
    """
    ssla: AgreementOffer

    def __init__(self, entry_point: AgreementOffer):
        self.ssla = entry_point

    def get_services(self) -> List["ServiceDescriptionTermType"]:
        return self.ssla.terms.all.service_description_term

    def get_services_names(self) -> List[str]:
        return [service.service_name for service in self.get_services()]

    def get_service(self, service_name: str) -> "ServiceDescriptionTermType":
        service_descriptions = [desc for desc in self.ssla.terms.all.service_description_term
                                if desc.service_name == service_name]
        return service_descriptions[0]

    def get_first_service(self) -> "ServiceDescriptionTermType":
        return self.get_services()[0]

    def get_first_service_name(self) -> str:
        return self.get_services_names()[0]

    def get_capabilities(self, service_name: str) -> Optional[list["CapabilityType"]]:
        service = self.get_service(service_name)
        return service.other_element.capabilities.capability

    def get_metrics(self, service_name: str) -> List["MetricType"]:
        """
        Get the metrics per service name from the SSLA
        """
        service_description_terms = self.get_service(service_name)
        return service_description_terms.other_element.security_metrics.metric

    def get_metric(self, service_name: str, metric_id: str) -> "MetricType":
        service_description_terms = self.get_service(service_name)
        test: MetricType
        singleton = [m for m in service_description_terms.other_element.security_metrics.metric if
                     m.reference_id == metric_id]
        if len(singleton) == 1:
            return singleton[0]
        elif len(singleton) > 1:
            raise SSLAMetricsException(f"too many metrics found for id {metric_id}")
        else:
            raise SSLAMetricsException(f"metric {metric_id} not found in SSLA")

    def get_metrics_json(self, service_name: str) -> List["Metric"]:
        """
        Get a pydantic data model of the metrics that can be serialized in json
        """
        ssla_metrics = self.get_metrics(service_name)
        return [MetricParser.to_json_model(metric) for metric in ssla_metrics]

    def get_metric_json(self, service_name: str, metric_id: str) -> "Metric":
        m = self.get_metric(service_name, metric_id)
        return MetricParser.to_json_model(m)

    def get_slos(self) -> List["Slotype"]:
        """
        Get the SLOs from the SSLA
        """
        slos: List["Slotype"] = []
        for guaranteeTerm in self.ssla.terms.all.guarantee_term:
            custom_service_level = guaranteeTerm.service_level_objective.custom_service_level
            for slo in custom_service_level.children[0].children:
                slo_parser = SLOParser(slo)
                slos.append(slo_parser.parse())
        if not slos:
            raise SSLASLOException("No SLO description in SSLA")
        return slos

    def get_slos_json(self) -> List["SLO"]:
        """
        Get a pydantic data model of the SLOs that can be serialized in json
        """
        ssla_slos = self.get_slos()
        return [SLOParser.to_json_model(slo) for slo in ssla_slos]

    def get_service_properties(self, service_name: str) -> List["ServicePropertiesType"]:
        """
        Provides a list of properties, because one service can have multiple set of properties.
        A service may have on set of properties per capability for example.
        :param service_name: name of the service concerned by the properties
        """
        return [p for p in self.ssla.terms.all.service_properties if p.service_name == service_name]

    def get_service_properties_json(self, service_name: str) -> List["ServiceProperties"]:
        """
        Get a pydantic data model of the propoerties of a service that can be serialized in json
        """
        ssla_service_properties = self.get_service_properties(service_name)
        return [ServicePropertiesParser.to_json_model(p) for p in ssla_service_properties]


class SSLAParser(object):
    """
    Parser to generate and validate the SSLA object model from various inputs
    """

    def __init__(self):
        self.self_path = Path.cwd()
        self.parser = XmlParser(context=XmlContext())
        self.schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates/ssla/ssla_schema.xsd")

    def validate_schema_from_content(self, ssla_content: bytes) -> bool:
        """
        Returns True if the given XML file is validated by the SSLA XML Schema
        """
        template = etree.parse(self.schema_path)
        schema = etree.XMLSchema(template)
        ssla = etree.XML(ssla_content)
        result = schema.validate(ssla)
        if len(schema.error_log) > 0:
            raise SSLAValidationException(f"invalid SSLA content: {schema.error_log.last_error.message}")
        return result

    def parse_from_content(self, content: bytes) -> "SSLA":
        """
        Returns a list of xsdata model from content
        """

        if not self.validate_schema_from_content(content):
            raise SSLAValidationException("SSLA not valid according to xsd schema")
        try:
            model = self.parser.from_bytes(content, AgreementOffer)
        except ParserError as e:
            raise SSLAFormatException("SSLA schema validation from content failed", e.args)

        return SSLA(model)
