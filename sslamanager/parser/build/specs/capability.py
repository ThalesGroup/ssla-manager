from __future__ import annotations

from dataclasses import dataclass, field

from sslamanager.parser.build.specs.controls.ccm import CcmcontrolType
from sslamanager.parser.build.specs.controls.nist import NistcontrolType

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


@dataclass(kw_only=True)
class CapabilityType:
    class Meta:
        name = "capabilityType"

    control_framework: CapabilityType.ControlFramework = field(
        metadata={
            "name": "controlFramework",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
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
    description: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    mandatory: str = field(
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass(kw_only=True)
    class ControlFramework:
        nistsecurity_control: list[NistcontrolType] = field(
            default_factory=list,
            metadata={
                "name": "NISTsecurityControl",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )
        ccmsecurity_control: list[CcmcontrolType] = field(
            default_factory=list,
            metadata={
                "name": "CCMsecurityControl",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )
        id: str = field(
            metadata={
                "type": "Attribute",
            }
        )
        framework_name: str = field(
            metadata={
                "name": "frameworkName",
                "type": "Attribute",
            }
        )
