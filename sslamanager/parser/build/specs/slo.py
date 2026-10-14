from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


class SlotypeImportanceWeight(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class OneOpOperator(Enum):
    EQ = "eq"
    GT = "gt"
    LT = "lt"
    GEQ = "geq"
    LEQ = "leq"


class TwoOpOperator(Enum):
    IN_EXCLUDED = "in_excluded"
    IN_INCLUDED = "in_included"


@dataclass(kw_only=True)
class SloexpressionType:
    class Meta:
        name = "SLOexpressionType"

    one_op_expression: None | SloexpressionType.OneOpExpression = field(
        default=None,
        metadata={
            "name": "oneOpExpression",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    two_op_expression: None | SloexpressionType.TwoOpExpression = field(
        default=None,
        metadata={
            "name": "twoOpExpression",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )

    @dataclass(kw_only=True)
    class OneOpExpression:
        operator: OneOpOperator = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            }
        )
        operand: None | object = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )

    @dataclass(kw_only=True)
    class TwoOpExpression:
        operator: TwoOpOperator = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            }
        )
        operand1: None | object = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )
        operand2: None | object = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )


@dataclass(kw_only=True)
class Slotype:
    class Meta:
        name = "SLOType"

    metric_ref: str = field(
        metadata={
            "name": "MetricREF",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    sloexpression: SloexpressionType = field(
        metadata={
            "name": "SLOexpression",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    importance_weight: SlotypeImportanceWeight = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    slo_id: str = field(
        metadata={
            "name": "SLO_ID",
            "type": "Attribute",
        }
    )
