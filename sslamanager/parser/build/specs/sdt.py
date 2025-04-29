from dataclasses import dataclass, field
from typing import Optional

from sslamanager.parser.build.specs.capability import CapabilityType
from sslamanager.parser.build.specs.security_metric import MetricType

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


@dataclass
class ServiceDescriptionType:
    class Meta:
        name = "serviceDescriptionType"

    service_resources: list["ServiceDescriptionType.ServiceResources"] = field(
        default_factory=list,
        metadata={
            "name": "serviceResources",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    capabilities: Optional["ServiceDescriptionType.Capabilities"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            "required": True,
        },
    )
    security_metrics: Optional["ServiceDescriptionType.SecurityMetrics"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
            },
        )
    )

    @dataclass
    class ServiceResources:
        resources_provider: list[
            "ServiceDescriptionType.ServiceResources.ResourcesProvider"
        ] = field(
            default_factory=list,
            metadata={
                "name": "resourcesProvider",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )

        @dataclass
        class ResourcesProvider:
            vm: list[
                "ServiceDescriptionType.ServiceResources.ResourcesProvider.Vm"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "VM",
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
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )
            zone: Optional[str] = field(
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
            max_allowed_vms: Optional[int] = field(
                default=None,
                metadata={
                    "name": "maxAllowedVMs",
                    "type": "Attribute",
                },
            )
            min_required_vms: Optional[int] = field(
                default=None,
                metadata={
                    "name": "minRequiredVMs",
                    "type": "Attribute",
                },
            )
            label: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )

            @dataclass
            class Vm:
                appliance: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                hardware: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                description: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

    @dataclass
    class Capabilities:
        capability: list[CapabilityType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )

    @dataclass
    class SecurityMetrics:
        metric: list[MetricType] = field(
            default_factory=list,
            metadata={
                "name": "Metric",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )
