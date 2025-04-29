from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = (
    "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/ccm"
)


class CcmcontrolTypeImportanceWeight(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class CcmcontrolType:
    class Meta:
        name = "CCMcontrolType"

    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/ccm",
            "required": True,
        },
    )
    importance_weight: Optional[CcmcontrolTypeImportanceWeight] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/ccm",
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    control_domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
