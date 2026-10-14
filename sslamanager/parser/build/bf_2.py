from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from sslamanager.parser.build.pkg_2005.pkg_08.addressing.ws_addr import (
    EndpointReferenceType,
)
from sslamanager.parser.build.xml import LangValue

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass(kw_only=True)
class BaseFaultType:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    timestamp: XmlDateTime = field(
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        }
    )
    originator: None | EndpointReferenceType = field(
        default=None,
        metadata={
            "name": "Originator",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    error_code: None | BaseFaultType.ErrorCode = field(
        default=None,
        metadata={
            "name": "ErrorCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    description: list[BaseFaultType.Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    fault_cause: None | BaseFaultType.FaultCause = field(
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

    @dataclass(kw_only=True)
    class ErrorCode:
        dialect: str = field(
            metadata={
                "type": "Attribute",
            }
        )
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )

    @dataclass(kw_only=True)
    class Description:
        value: str = field(default="")
        lang: None | str | LangValue = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

    @dataclass(kw_only=True)
    class FaultCause:
        other_element: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            },
        )


@dataclass(kw_only=True)
class BaseFault(BaseFaultType):
    class Meta:
        namespace = "http://docs.oasis-open.org/wsrf/bf-2"
