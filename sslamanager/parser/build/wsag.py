from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime, XmlDuration

from sslamanager.parser.build.bf_2 import BaseFaultType
from sslamanager.parser.build.pkg_2001.xmlschema import (
    All as XmlschemaAll,
)
from sslamanager.parser.build.pkg_2001.xmlschema import (
    Choice,
    Enumeration,
    FractionDigits,
    GroupRef,
    Length,
    LocalSimpleType,
    MaxExclusive,
    MaxInclusive,
    MaxLength,
    MinExclusive,
    MinInclusive,
    MinLength,
    Pattern,
    Sequence,
    TotalDigits,
    WhiteSpace,
)

__NAMESPACE__ = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class AgreementId:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    value: str = field(default="")


@dataclass(kw_only=True)
class AgreementInitiatorIdentifierType:
    reference: None | object = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class AgreementResponderIdentifierType:
    reference: None | object = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


class AgreementRoleType(Enum):
    AGREEMENT_INITIATOR = "AgreementInitiator"
    AGREEMENT_RESPONDER = "AgreementResponder"


@dataclass(kw_only=True)
class CompensationType:
    assessment_interval: CompensationType.AssessmentInterval = field(
        metadata={
            "name": "AssessmentInterval",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    value_unit: None | str = field(
        default=None,
        metadata={
            "name": "ValueUnit",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    value_expression: None | object = field(
        default=None,
        metadata={
            "name": "ValueExpression",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )

    @dataclass(kw_only=True)
    class AssessmentInterval:
        time_interval: None | XmlDuration = field(
            default=None,
            metadata={
                "name": "TimeInterval",
                "type": "Element",
                "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            },
        )
        count: None | int = field(
            default=None,
            metadata={
                "name": "Count",
                "type": "Element",
                "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            },
        )


@dataclass(kw_only=True)
class Constraint:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class KpitargetType:
    class Meta:
        name = "KPITargetType"

    kpiname: str = field(
        metadata={
            "name": "KPIName",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    custom_service_level: None | object = field(
        default=None,
        metadata={
            "name": "CustomServiceLevel",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class Location:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    value: str = field(default="")


@dataclass(kw_only=True)
class Name:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    value: str = field(default="")


@dataclass(kw_only=True)
class NoncriticalExtensionType:
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class PreferenceType:
    service_term_reference: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceTermReference",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    utility: list[float] = field(
        default_factory=list,
        metadata={
            "name": "Utility",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "min_occurs": 1,
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class QualifyingCondition:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ServiceNameSet:
    service_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceName",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


class ServiceRoleType(Enum):
    SERVICE_CONSUMER = "ServiceConsumer"
    SERVICE_PROVIDER = "ServiceProvider"


@dataclass(kw_only=True)
class ServiceSelectorType:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    service_name: None | str = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class TermType:
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )


@dataclass(kw_only=True)
class AgreementContextType:
    agreement_initiator: None | object = field(
        default=None,
        metadata={
            "name": "AgreementInitiator",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    agreement_responder: None | object = field(
        default=None,
        metadata={
            "name": "AgreementResponder",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_provider: AgreementRoleType = field(
        metadata={
            "name": "ServiceProvider",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    expiration_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ExpirationTime",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    template_id: None | str = field(
        default=None,
        metadata={
            "name": "TemplateId",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    template_name: None | str = field(
        default=None,
        metadata={
            "name": "TemplateName",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
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
class BusinessValueListType:
    importance: None | int = field(
        default=None,
        metadata={
            "name": "Importance",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    penalty: list[CompensationType] = field(
        default_factory=list,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    reward: list[CompensationType] = field(
        default_factory=list,
        metadata={
            "name": "Reward",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    preference: None | PreferenceType = field(
        default=None,
        metadata={
            "name": "Preference",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    custom_business_value: list[object] = field(
        default_factory=list,
        metadata={
            "name": "CustomBusinessValue",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class ContinuingFaultType(BaseFaultType):
    pass


@dataclass(kw_only=True)
class NoncriticalExtensions(NoncriticalExtensionType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class OfferItemType:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    item_constraint: OfferItemType.ItemConstraint = field(
        metadata={
            "name": "ItemConstraint",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )

    @dataclass(kw_only=True)
    class ItemConstraint:
        simple_type: None | LocalSimpleType = field(
            default=None,
            metadata={
                "name": "simpleType",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        min_exclusive: list[MinExclusive] = field(
            default_factory=list,
            metadata={
                "name": "minExclusive",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        min_inclusive: list[MinInclusive] = field(
            default_factory=list,
            metadata={
                "name": "minInclusive",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        max_exclusive: list[MaxExclusive] = field(
            default_factory=list,
            metadata={
                "name": "maxExclusive",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        max_inclusive: list[MaxInclusive] = field(
            default_factory=list,
            metadata={
                "name": "maxInclusive",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        total_digits: list[TotalDigits] = field(
            default_factory=list,
            metadata={
                "name": "totalDigits",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        fraction_digits: list[FractionDigits] = field(
            default_factory=list,
            metadata={
                "name": "fractionDigits",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        length: list[Length] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        min_length: list[MinLength] = field(
            default_factory=list,
            metadata={
                "name": "minLength",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        max_length: list[MaxLength] = field(
            default_factory=list,
            metadata={
                "name": "maxLength",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        enumeration: list[Enumeration] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        white_space: list[WhiteSpace] = field(
            default_factory=list,
            metadata={
                "name": "whiteSpace",
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        pattern: list[Pattern] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        group: None | GroupRef = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        all: None | XmlschemaAll = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        choice: None | Choice = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        sequence: None | Sequence = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )


@dataclass(kw_only=True)
class ServiceLevelObjectiveType:
    kpitarget: None | KpitargetType = field(
        default=None,
        metadata={
            "name": "KPITarget",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    custom_service_level: None | object = field(
        default=None,
        metadata={
            "name": "CustomServiceLevel",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class ServiceTermType(TermType):
    service_name: str = field(
        metadata={
            "name": "ServiceName",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )


@dataclass(kw_only=True)
class VariableType:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    metric: None | str = field(
        default=None,
        metadata={
            "name": "Metric",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class ConstraintSectionType:
    item: list[OfferItemType] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    constraint: list[Constraint] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class Context(AgreementContextType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class ContinuingFault(ContinuingFaultType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class ServiceDescriptionTermType(ServiceTermType):
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class ServiceLevelObjective(ServiceLevelObjectiveType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class ServiceReferenceType(ServiceTermType):
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class VariableSetType:
    variable: list[VariableType] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class GuaranteeTermType(TermType):
    service_scope: list[ServiceSelectorType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceScope",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    qualifying_condition: None | QualifyingCondition = field(
        default=None,
        metadata={
            "name": "QualifyingCondition",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_level_objective: ServiceLevelObjective = field(
        metadata={
            "name": "ServiceLevelObjective",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    business_value_list: BusinessValueListType = field(
        metadata={
            "name": "BusinessValueList",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    obligated: None | ServiceRoleType = field(
        default=None,
        metadata={
            "name": "Obligated",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class ServicePropertiesType(ServiceTermType):
    variable_set: VariableSetType = field(
        metadata={
            "name": "VariableSet",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )


@dataclass(kw_only=True)
class TermCompositorType:
    exactly_one: list[TermCompositorType] = field(
        default_factory=list,
        metadata={
            "name": "ExactlyOne",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    one_or_more: list[TermCompositorType] = field(
        default_factory=list,
        metadata={
            "name": "OneOrMore",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    all: list[All] = field(
        default_factory=list,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_description_term: list[ServiceDescriptionTermType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceDescriptionTerm",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_reference: list[ServiceReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceReference",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_properties: list[ServicePropertiesType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceProperties",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    guarantee_term: list[GuaranteeTermType] = field(
        default_factory=list,
        metadata={
            "name": "GuaranteeTerm",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class All(TermCompositorType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class TermTreeType:
    all: None | All = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class Terms(TermTreeType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class AgreementType:
    name: None | Name = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    context: Context = field(
        metadata={
            "name": "Context",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    terms: Terms = field(
        metadata={
            "name": "Terms",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    agreement_id: None | str = field(
        default=None,
        metadata={
            "name": "AgreementId",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class AgreementOffer(AgreementType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass(kw_only=True)
class AgreementTemplateType(AgreementType):
    creation_constraints: ConstraintSectionType = field(
        metadata={
            "name": "CreationConstraints",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        }
    )
    template_id: None | str = field(
        default=None,
        metadata={
            "name": "TemplateId",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass(kw_only=True)
class Template(AgreementTemplateType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"
