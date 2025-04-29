from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from sslamanager.parser.build.pkg_2005.pkg_08.addressing.ws_addr import (
    EndpointReferenceType,
)
from sslamanager.parser.build.xml import LangValue

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass
class BaseFaultType:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
            "required": True,
        },
    )
    originator: Optional[EndpointReferenceType] = field(
        default=None,
        metadata={
            "name": "Originator",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    error_code: Optional["BaseFaultType.ErrorCode"] = field(
        default=None,
        metadata={
            "name": "ErrorCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    description: list["BaseFaultType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    fault_cause: Optional["BaseFaultType.FaultCause"] = field(
        default=None,
        metadata={
            "name": "FaultCause",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )

    @dataclass
    class ErrorCode:
        dialect: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )

    @dataclass
    class Description:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        lang: Optional[Union[str, LangValue]] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

    @dataclass
    class FaultCause:
        other_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            },
        )


@dataclass
class BaseFault(BaseFaultType):
    class Meta:
        namespace = "http://docs.oasis-open.org/wsrf/bf-2"
