from __future__ import annotations

from dataclasses import dataclass, field

from sslamanager.parser.build.specs.capability import CapabilityType
from sslamanager.parser.build.specs.security_metric import MetricType

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


@dataclass(kw_only=True)
class ServiceDescriptionType:
    class Meta:
        name = "serviceDescriptionType"

    service_resources: list[ServiceDescriptionType.ServiceResources] = field(
        default_factory=list,
        metadata={
            "name": "serviceResources",
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )
    capabilities: ServiceDescriptionType.Capabilities = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        }
    )
    security_metrics: None | ServiceDescriptionType.SecurityMetrics = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
        },
    )

    @dataclass(kw_only=True)
    class ServiceResources:
        resources_provider: list[
            ServiceDescriptionType.ServiceResources.ResourcesProvider
        ] = field(
            default_factory=list,
            metadata={
                "name": "resourcesProvider",
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class ResourcesProvider:
            vm: list[
                ServiceDescriptionType.ServiceResources.ResourcesProvider.Vm
            ] = field(
                default_factory=list,
                metadata={
                    "name": "VM",
                    "type": "Element",
                    "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                },
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
            zone: str = field(
                metadata={
                    "type": "Attribute",
                }
            )
            description: str = field(
                metadata={
                    "type": "Attribute",
                }
            )
            max_allowed_vms: None | int = field(
                default=None,
                metadata={
                    "name": "maxAllowedVMs",
                    "type": "Attribute",
                },
            )
            min_required_vms: None | int = field(
                default=None,
                metadata={
                    "name": "minRequiredVMs",
                    "type": "Attribute",
                },
            )
            label: str = field(
                metadata={
                    "type": "Attribute",
                }
            )

            @dataclass(kw_only=True)
            class Vm:
                appliance: None | str = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                hardware: None | str = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                description: None | str = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

    @dataclass(kw_only=True)
    class Capabilities:
        capability: list[CapabilityType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
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
