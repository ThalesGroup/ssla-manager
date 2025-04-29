from dataclasses import dataclass, field

from sslamanager.parser.build.specs.sdt import ServiceDescriptionType
from sslamanager.parser.build.specs.slo import Slotype

__NAMESPACE__ = "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"


@dataclass
class Endpoint:
    class Meta:
        name = "endpoint"
        namespace = (
            "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ObjectiveList:
    class Meta:
        name = "objectiveList"
        namespace = (
            "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"
        )

    slo: list[Slotype] = field(
        default_factory=list,
        metadata={
            "name": "SLO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ServiceDescription(ServiceDescriptionType):
    class Meta:
        name = "serviceDescription"
        namespace = (
            "http://www.specs-project.eu/resources/schemas/xml/SLAtemplate"
        )
