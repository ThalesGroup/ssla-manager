from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = (
    "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/nist"
)


class NistcontrolTypeImportanceWeight(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(kw_only=True)
class NistcontrolType:
    class Meta:
        name = "NISTcontrolType"

    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/nist",
        }
    )
    importance_weight: NistcontrolTypeImportanceWeight = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/control_frameworks/nist",
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    control_enhancement: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    security_control: str = field(
        metadata={
            "name": "securityControl",
            "type": "Attribute",
        }
    )
    control_family: str = field(
        metadata={
            "type": "Attribute",
        }
    )
