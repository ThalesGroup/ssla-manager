from dataclasses import dataclass, field
from typing import Optional

from sslamanager.parser.build.specs.controls.ccm import CcmcontrolType
from sslamanager.parser.build.specs.controls.nist import NistcontrolType

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


@dataclass
class CapabilityType:
    class Meta:
        name = "capabilityType"

    control_framework: Optional["CapabilityType.ControlFramework"] = field(
        default=None,
        metadata={
            "name": "controlFramework",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    mandatory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
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
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        framework_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "frameworkName",
                "type": "Attribute",
                "required": True,
            },
        )
