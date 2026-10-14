from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


class EnumTypeEnumItemsType(Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"


class IntervalTypeIntervalItemsType(Enum):
    INTEGER = "integer"
    FLOAT = "float"


@dataclass(kw_only=True)
class MetricParameterType:
    class Meta:
        name = "metricParameterType"

    parameter_definition_id: str = field(
        metadata={
            "name": "parameterDefinitionId",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    value: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    note: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )


@dataclass(kw_only=True)
class MetricRuleType:
    class Meta:
        name = "metricRuleType"

    rule_definition_id: str = field(
        metadata={
            "name": "ruleDefinitionId",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    value: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    note: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
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


@dataclass(kw_only=True)
class ReferenceType:
    class Meta:
        name = "referenceType"

    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    reference_id: str = field(
        metadata={
            "name": "referenceId",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class EnumType:
    class Meta:
        name = "enumType"

    enum_items_type: EnumTypeEnumItemsType = field(
        metadata={
            "name": "enumItemsType",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    enum_items: EnumType.EnumItems = field(
        metadata={
            "name": "enumItems",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )

    @dataclass(kw_only=True)
    class EnumItems:
        enum_item: list[EnumType.EnumItems.EnumItem] = field(
            default_factory=list,
            metadata={
                "name": "enumItem",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class EnumItem:
            value: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                }
            )
            description: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                }
            )


@dataclass(kw_only=True)
class IntervalType:
    class Meta:
        name = "intervalType"

    interval_items_type: IntervalTypeIntervalItemsType = field(
        metadata={
            "name": "intervalItemsType",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    interval_item_start: None | object = field(
        default=None,
        metadata={
            "name": "intervalItemStart",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    interval_item_stop: None | object = field(
        default=None,
        metadata={
            "name": "intervalItemStop",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    interval_item_step: None | object = field(
        default=None,
        metadata={
            "name": "intervalItemStep",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )


@dataclass(kw_only=True)
class ParameterDefinitionType(ReferenceType):
    class Meta:
        name = "parameterDefinitionType"

    definition: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    parameter_type: ParameterTypeType = field(
        metadata={
            "name": "parameterType",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    note: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )


@dataclass(kw_only=True)
class RuleDefinitionType(ReferenceType):
    class Meta:
        name = "ruleDefinitionType"

    definition: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    note: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )


@dataclass(kw_only=True)
class ScaleType:
    class Meta:
        name = "scaleType"

    qualitative: None | QualitativeValueType = field(
        default=None,
        metadata={
            "name": "Qualitative",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    quantitative: None | QuantitativeValueType = field(
        default=None,
        metadata={
            "name": "Quantitative",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )


@dataclass(kw_only=True)
class UnitType:
    class Meta:
        name = "unitType"

    enum_unit: None | EnumType = field(
        default=None,
        metadata={
            "name": "enumUnit",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    interval_unit: None | IntervalType = field(
        default=None,
        metadata={
            "name": "intervalUnit",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class MetricDefinitionType:
    unit: UnitType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    scale: ScaleType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    expression: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    definition: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    note: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )


@dataclass(kw_only=True)
class AbstractMetricType(ReferenceType):
    metric_definition: MetricDefinitionType = field(
        metadata={
            "name": "MetricDefinition",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    abstract_metric_rule_definition: (
        None | AbstractMetricType.AbstractMetricRuleDefinition
    ) = field(
        default=None,
        metadata={
            "name": "AbstractMetricRuleDefinition",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    abstract_metric_parameter_definition: (
        None | AbstractMetricType.AbstractMetricParameterDefinition
    ) = field(
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

    @dataclass(kw_only=True)
    class AbstractMetricRuleDefinition:
        rule_definition: list[RuleDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "RuleDefinition",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )

    @dataclass(kw_only=True)
    class AbstractMetricParameterDefinition:
        parameter_definition: list[ParameterDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "ParameterDefinition",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )


@dataclass(kw_only=True)
class MetricType(AbstractMetricType):
    primary_abstract_metric: None | str = field(
        default=None,
        metadata={
            "name": "PrimaryAbstractMetric",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    metric_rules: list[MetricType.MetricRules] = field(
        default_factory=list,
        metadata={
            "name": "MetricRules",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    metric_parameters: list[MetricType.MetricParameters] = field(
        default_factory=list,
        metadata={
            "name": "MetricParameters",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    note: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )

    @dataclass(kw_only=True)
    class MetricRules:
        metric_rule: MetricRuleType = field(
            metadata={
                "name": "MetricRule",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            }
        )

    @dataclass(kw_only=True)
    class MetricParameters:
        metric_parameter: MetricParameterType = field(
            metadata={
                "name": "MetricParameter",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            }
        )


@dataclass(kw_only=True)
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
