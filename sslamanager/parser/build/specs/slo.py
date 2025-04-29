from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

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


@dataclass
class SloexpressionType:
    class Meta:
        name = "SLOexpressionType"

    one_op_expression: Optional["SloexpressionType.OneOpExpression"] = field(
        default=None,
        metadata={
            "name": "oneOpExpression",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    two_op_expression: Optional["SloexpressionType.TwoOpExpression"] = field(
        default=None,
        metadata={
            "name": "twoOpExpression",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )

    @dataclass
    class OneOpExpression:
        operator: Optional[OneOpOperator] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "required": True,
            },
        )
        operand: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )

    @dataclass
    class TwoOpExpression:
        operator: Optional[TwoOpOperator] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "required": True,
            },
        )
        operand1: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )
        operand2: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )


@dataclass
class Slotype:
    class Meta:
        name = "SLOType"

    metric_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetricREF",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    sloexpression: Optional[SloexpressionType] = field(
        default=None,
        metadata={
            "name": "SLOexpression",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    importance_weight: Optional[SlotypeImportanceWeight] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    slo_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SLO_ID",
            "type": "Attribute",
            "required": True,
        },
    )
