from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = (
    "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/nist"
)


class NistcontrolTypeImportanceWeight(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class NistcontrolType:
    class Meta:
        name = "NISTcontrolType"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/nist",
            "required": True,
        },
    )
    importance_weight: Optional[NistcontrolTypeImportanceWeight] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/nist",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    control_enhancement: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    security_control: Optional[str] = field(
        default=None,
        metadata={
            "name": "securityControl",
            "type": "Attribute",
            "required": True,
        },
    )
    control_family: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
