from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = (
    "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/ccm"
)


class CcmcontrolTypeImportanceWeight(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(kw_only=True)
class CcmcontrolType:
    class Meta:
        name = "CCMcontrolType"

    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/ccm",
        }
    )
    importance_weight: CcmcontrolTypeImportanceWeight = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/ccm",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    control_domain: str = field(
        metadata={
            "type": "Attribute",
        }
    )
