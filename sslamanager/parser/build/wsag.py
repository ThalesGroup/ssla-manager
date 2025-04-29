from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

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


@dataclass
class AgreementId:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AgreementInitiatorIdentifierType:
    reference: Optional[object] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class AgreementResponderIdentifierType:
    reference: Optional[object] = field(
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


@dataclass
class CompensationType:
    assessment_interval: Optional["CompensationType.AssessmentInterval"] = (
        field(
            default=None,
            metadata={
                "name": "AssessmentInterval",
                "type": "Element",
                "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
                "required": True,
            },
        )
    )
    value_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueUnit",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    value_expression: Optional[object] = field(
        default=None,
        metadata={
            "name": "ValueExpression",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )

    @dataclass
    class AssessmentInterval:
        time_interval: Optional[XmlDuration] = field(
            default=None,
            metadata={
                "name": "TimeInterval",
                "type": "Element",
                "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            },
        )
        count: Optional[int] = field(
            default=None,
            metadata={
                "name": "Count",
                "type": "Element",
                "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            },
        )


@dataclass
class Constraint:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class KpitargetType:
    class Meta:
        name = "KPITargetType"

    kpiname: Optional[str] = field(
        default=None,
        metadata={
            "name": "KPIName",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    custom_service_level: Optional[object] = field(
        default=None,
        metadata={
            "name": "CustomServiceLevel",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class Location:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Name:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class NoncriticalExtensionType:
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
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


@dataclass
class QualifyingCondition:
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
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


@dataclass
class ServiceSelectorType:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class TermType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )


@dataclass
class AgreementContextType:
    agreement_initiator: Optional[object] = field(
        default=None,
        metadata={
            "name": "AgreementInitiator",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    agreement_responder: Optional[object] = field(
        default=None,
        metadata={
            "name": "AgreementResponder",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_provider: Optional[AgreementRoleType] = field(
        default=None,
        metadata={
            "name": "ServiceProvider",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    expiration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpirationTime",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    template_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TemplateId",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    template_name: Optional[str] = field(
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


@dataclass
class BusinessValueListType:
    importance: Optional[int] = field(
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
    preference: Optional[PreferenceType] = field(
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


@dataclass
class ContinuingFaultType(BaseFaultType):
    pass


@dataclass
class NoncriticalExtensions(NoncriticalExtensionType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class OfferItemType:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    item_constraint: Optional["OfferItemType.ItemConstraint"] = field(
        default=None,
        metadata={
            "name": "ItemConstraint",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )

    @dataclass
    class ItemConstraint:
        simple_type: Optional[LocalSimpleType] = field(
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
        group: Optional[GroupRef] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        all: Optional[XmlschemaAll] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        choice: Optional[Choice] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )
        sequence: Optional[Sequence] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
            },
        )


@dataclass
class ServiceLevelObjectiveType:
    kpitarget: Optional[KpitargetType] = field(
        default=None,
        metadata={
            "name": "KPITarget",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    custom_service_level: Optional[object] = field(
        default=None,
        metadata={
            "name": "CustomServiceLevel",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class ServiceTermType(TermType):
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )


@dataclass
class VariableType:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    metric: Optional[str] = field(
        default=None,
        metadata={
            "name": "Metric",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
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


@dataclass
class Context(AgreementContextType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class ContinuingFault(ContinuingFaultType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class ServiceDescriptionTermType(ServiceTermType):
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class ServiceLevelObjective(ServiceLevelObjectiveType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class ServiceReferenceType(ServiceTermType):
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
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


@dataclass
class GuaranteeTermType(TermType):
    service_scope: list[ServiceSelectorType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceScope",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    qualifying_condition: Optional[QualifyingCondition] = field(
        default=None,
        metadata={
            "name": "QualifyingCondition",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    service_level_objective: Optional[ServiceLevelObjective] = field(
        default=None,
        metadata={
            "name": "ServiceLevelObjective",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    business_value_list: Optional[BusinessValueListType] = field(
        default=None,
        metadata={
            "name": "BusinessValueList",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    obligated: Optional[ServiceRoleType] = field(
        default=None,
        metadata={
            "name": "Obligated",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class ServicePropertiesType(ServiceTermType):
    variable_set: Optional[VariableSetType] = field(
        default=None,
        metadata={
            "name": "VariableSet",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )


@dataclass
class TermCompositorType:
    exactly_one: list["TermCompositorType"] = field(
        default_factory=list,
        metadata={
            "name": "ExactlyOne",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    one_or_more: list["TermCompositorType"] = field(
        default_factory=list,
        metadata={
            "name": "OneOrMore",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    all: list["All"] = field(
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


@dataclass
class All(TermCompositorType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class TermTreeType:
    all: Optional[All] = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class Terms(TermTreeType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class AgreementType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )
    context: Optional[Context] = field(
        default=None,
        metadata={
            "name": "Context",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    terms: Optional[Terms] = field(
        default=None,
        metadata={
            "name": "Terms",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    agreement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgreementId",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class AgreementOffer(AgreementType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"


@dataclass
class AgreementTemplateType(AgreementType):
    creation_constraints: Optional[ConstraintSectionType] = field(
        default=None,
        metadata={
            "name": "CreationConstraints",
            "type": "Element",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
            "required": True,
        },
    )
    template_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TemplateId",
            "type": "Attribute",
            "namespace": "http://schemas.ggf.org/graap/2007/03/ws-agreement",
        },
    )


@dataclass
class Template(AgreementTemplateType):
    class Meta:
        namespace = "http://schemas.ggf.org/graap/2007/03/ws-agreement"
