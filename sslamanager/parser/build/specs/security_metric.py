from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


class EnumTypeEnumItemsType(Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"


class IntervalTypeIntervalItemsType(Enum):
    INTEGER = "integer"
    FLOAT = "float"


@dataclass
class MetricParameterType:
    class Meta:
        name = "metricParameterType"

    parameter_definition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterDefinitionId",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )


@dataclass
class MetricRuleType:
    class Meta:
        name = "metricRuleType"

    rule_definition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ruleDefinitionId",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )


class ParameterTypeType(Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    LIST = "list"


class QualitativeValueType(Enum):
    NOMINAL = "Nominal"
    ORDINAL = "Ordinal"


class QuantitativeValueType(Enum):
    INTERVAL = "Interval"
    RATIO = "Ratio"


@dataclass
class ReferenceType:
    class Meta:
        name = "referenceType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceId",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EnumType:
    class Meta:
        name = "enumType"

    enum_items_type: Optional[EnumTypeEnumItemsType] = field(
        default=None,
        metadata={
            "name": "enumItemsType",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    enum_items: Optional["EnumType.EnumItems"] = field(
        default=None,
        metadata={
            "name": "enumItems",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )

    @dataclass
    class EnumItems:
        enum_item: list["EnumType.EnumItems.EnumItem"] = field(
            default_factory=list,
            metadata={
                "name": "enumItem",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )

        @dataclass
        class EnumItem:
            value: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                    "required": True,
                },
            )
            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                    "required": True,
                },
            )


@dataclass
class IntervalType:
    class Meta:
        name = "intervalType"

    interval_items_type: Optional[IntervalTypeIntervalItemsType] = field(
        default=None,
        metadata={
            "name": "intervalItemsType",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    interval_item_start: Optional[object] = field(
        default=None,
        metadata={
            "name": "intervalItemStart",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    interval_item_stop: Optional[object] = field(
        default=None,
        metadata={
            "name": "intervalItemStop",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    interval_item_step: Optional[object] = field(
        default=None,
        metadata={
            "name": "intervalItemStep",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )


@dataclass
class ParameterDefinitionType(ReferenceType):
    class Meta:
        name = "parameterDefinitionType"

    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    parameter_type: Optional[ParameterTypeType] = field(
        default=None,
        metadata={
            "name": "parameterType",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )


@dataclass
class RuleDefinitionType(ReferenceType):
    class Meta:
        name = "ruleDefinitionType"

    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )


@dataclass
class ScaleType:
    class Meta:
        name = "scaleType"

    qualitative: Optional[QualitativeValueType] = field(
        default=None,
        metadata={
            "name": "Qualitative",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    quantitative: Optional[QuantitativeValueType] = field(
        default=None,
        metadata={
            "name": "Quantitative",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )


@dataclass
class UnitType:
    class Meta:
        name = "unitType"

    enum_unit: Optional[EnumType] = field(
        default=None,
        metadata={
            "name": "enumUnit",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    interval_unit: Optional[IntervalType] = field(
        default=None,
        metadata={
            "name": "intervalUnit",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MetricDefinitionType:
    unit: Optional[UnitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    scale: Optional[ScaleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    expression: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )


@dataclass
class AbstractMetricType(ReferenceType):
    metric_definition: Optional[MetricDefinitionType] = field(
        default=None,
        metadata={
            "name": "MetricDefinition",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    abstract_metric_rule_definition: Optional[
        "AbstractMetricType.AbstractMetricRuleDefinition"
    ] = field(
        default=None,
        metadata={
            "name": "AbstractMetricRuleDefinition",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    abstract_metric_parameter_definition: Optional[
        "AbstractMetricType.AbstractMetricParameterDefinition"
    ] = field(
        default=None,
        metadata={
            "name": "AbstractMetricParameterDefinition",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    underlying_abstract_metric: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "UnderlyingAbstractMetric",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )

    @dataclass
    class AbstractMetricRuleDefinition:
        rule_definition: list[RuleDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "RuleDefinition",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )

    @dataclass
    class AbstractMetricParameterDefinition:
        parameter_definition: list[ParameterDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "ParameterDefinition",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )


@dataclass
class MetricType(AbstractMetricType):
    primary_abstract_metric: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryAbstractMetric",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    metric_rules: list["MetricType.MetricRules"] = field(
        default_factory=list,
        metadata={
            "name": "MetricRules",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    metric_parameters: list["MetricType.MetricParameters"] = field(
        default_factory=list,
        metadata={
            "name": "MetricParameters",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )

    @dataclass
    class MetricRules:
        metric_rule: Optional[MetricRuleType] = field(
            default=None,
            metadata={
                "name": "MetricRule",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "required": True,
            },
        )

    @dataclass
    class MetricParameters:
        metric_parameter: Optional[MetricParameterType] = field(
            default=None,
            metadata={
                "name": "MetricParameter",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "required": True,
            },
        )


@dataclass
class SecurityMetricsType:
    class Meta:
        name = "security_metricsType"

    abstract_metric: list[AbstractMetricType] = field(
        default_factory=list,
        metadata={
            "name": "AbstractMetric",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    metric: list[MetricType] = field(
        default_factory=list,
        metadata={
            "name": "Metric",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
