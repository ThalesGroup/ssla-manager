from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional, Union
from xml.etree.ElementTree import QName

from sslamanager.parser.build.xml import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class AllNniValue(Enum):
    UNBOUNDED = "unbounded"


class AllMaxOccurs(Enum):
    VALUE_1 = 1


class AllMinOccurs(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


@dataclass
class AnyType:
    """
    Not the real urType, but as close an approximation as we can get in the XML
    representation.
    """

    class Meta:
        name = "anyType"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
class Appinfo:
    class Meta:
        name = "appinfo"
        namespace = "http://www.w3.org/2001/XMLSchema"

    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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


class AttributeUse(Enum):
    PROHIBITED = "prohibited"
    OPTIONAL = "optional"
    REQUIRED = "required"


class BlockSet(Enum):
    """
    A utility type, not for public use #all or (possibly empty) subset of
    {substitution, extension, restriction}
    """

    ALL = "#all"
    EXTENSION = "extension"
    RESTRICTION = "restriction"
    SUBSTITUTION = "substitution"


class DerivationSet(Enum):
    """
    A utility type, not for public use #all or (possibly empty) subset of
    {extension, restriction}
    """

    EXTENSION = "extension"
    RESTRICTION = "restriction"
    ALL = "#all"


class FormChoice(Enum):
    """
    A utility type, not for public use.
    """

    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"


class FullDerivationSet(Enum):
    """
    A utility type, not for public use #all or (possibly empty) subset of
    {extension, restriction, list, union}
    """

    EXTENSION = "extension"
    RESTRICTION = "restriction"
    LIST = "list"
    UNION = "union"
    ALL = "#all"


class NamespaceList(Enum):
    """
    A utility type, not for public use.
    """

    ANY = "##any"
    OTHER = "##other"
    TARGET_NAMESPACE = "##targetNamespace"
    LOCAL = "##local"


class NarrowMaxMinMaxOccurs(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


class NarrowMaxMinMinOccurs(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


@dataclass
class OpenAttrs:
    """
    This type is extended by almost all schema types to allow attributes from other
    namespaces to be added to user schemas.
    """

    class Meta:
        name = "openAttrs"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


class SimpleDerivationSet(Enum):
    """
    #all or (possibly empty) subset of {restriction, union, list} A utility type,
    not for public use
    """

    ALL = "#all"
    LIST = "list"
    UNION = "union"
    RESTRICTION = "restriction"


class WhiteSpaceValue(Enum):
    PRESERVE = "preserve"
    REPLACE = "replace"
    COLLAPSE = "collapse"


class WildcardProcessContents(Enum):
    SKIP = "skip"
    LAX = "lax"
    STRICT = "strict"


@dataclass
class Documentation:
    class Meta:
        name = "documentation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
class Annotation(OpenAttrs):
    class Meta:
        name = "annotation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    appinfo: list[Appinfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    documentation: list[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Annotated(OpenAttrs):
    """
    This type is extended by all types which allow annotation other than
    &lt;schema&gt; itself.
    """

    class Meta:
        name = "annotated"

    annotation: Optional[Annotation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Facet(Annotated):
    class Meta:
        name = "facet"

    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FieldType(Annotated):
    class Meta:
        name = "field"
        namespace = "http://www.w3.org/2001/XMLSchema"

    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(\.//)?((((child::)?((\i\c*:)?(\i\c*|\*)))|\.)/)*((((child::)?((\i\c*:)?(\i\c*|\*)))|\.)|((attribute::|@)((\i\c*:)?(\i\c*|\*))))(\|(\.//)?((((child::)?((\i\c*:)?(\i\c*|\*)))|\.)/)*((((child::)?((\i\c*:)?(\i\c*|\*)))|\.)|((attribute::|@)((\i\c*:)?(\i\c*|\*)))))*",
        },
    )


@dataclass
class Import(Annotated):
    class Meta:
        name = "import"
        namespace = "http://www.w3.org/2001/XMLSchema"

    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
        },
    )


@dataclass
class Include(Annotated):
    class Meta:
        name = "include"
        namespace = "http://www.w3.org/2001/XMLSchema"

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Notation(Annotated):
    class Meta:
        name = "notation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    public: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Selector(Annotated):
    class Meta:
        name = "selector"
        namespace = "http://www.w3.org/2001/XMLSchema"

    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(\.//)?(((child::)?((\i\c*:)?(\i\c*|\*)))|\.)(/(((child::)?((\i\c*:)?(\i\c*|\*)))|\.))*(\|(\.//)?(((child::)?((\i\c*:)?(\i\c*|\*)))|\.)(/(((child::)?((\i\c*:)?(\i\c*|\*)))|\.))*)*",
        },
    )


@dataclass
class SimpleTypeAbstract(Annotated):
    """
    :ivar restriction:
    :ivar list_value:
    :ivar union:
    :ivar final:
    :ivar name: Can be restricted to required or forbidden
    """

    class Meta:
        name = "simpleType"

    restriction: Optional["Restriction"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    list_value: Optional["List"] = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    union: Optional["UnionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    final: Optional[SimpleDerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Wildcard(Annotated):
    class Meta:
        name = "wildcard"

    namespace: NamespaceList = field(
        default=NamespaceList.ANY,
        metadata={
            "type": "Attribute",
        },
    )
    process_contents: WildcardProcessContents = field(
        default=WildcardProcessContents.STRICT,
        metadata={
            "name": "processContents",
            "type": "Attribute",
        },
    )


@dataclass
class AnyType(Wildcard):
    class Meta:
        name = "any"
        namespace = "http://www.w3.org/2001/XMLSchema"

    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )


@dataclass
class AnyAttribute(Wildcard):
    class Meta:
        name = "anyAttribute"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Keybase(Annotated):
    class Meta:
        name = "keybase"

    selector: Optional[Selector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "required": True,
        },
    )
    field_value: list[FieldType] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "min_occurs": 1,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LocalSimpleType(SimpleTypeAbstract):
    """
    :ivar any_element:
    :ivar name: Forbidden when nested
    :ivar final:
    """

    class Meta:
        name = "localSimpleType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    final: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class MaxExclusive(Facet):
    class Meta:
        name = "maxExclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MaxInclusive(Facet):
    class Meta:
        name = "maxInclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MinExclusive(Facet):
    class Meta:
        name = "minExclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MinInclusive(Facet):
    class Meta:
        name = "minInclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NoFixedFacet(Facet):
    class Meta:
        name = "noFixedFacet"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    fixed: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class NumFacet(Facet):
    class Meta:
        name = "numFacet"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TopLevelSimpleType(SimpleTypeAbstract):
    """
    :ivar any_element:
    :ivar name: Required at the top level
    """

    class Meta:
        name = "topLevelSimpleType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WhiteSpace(Facet):
    class Meta:
        name = "whiteSpace"
        namespace = "http://www.w3.org/2001/XMLSchema"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[WhiteSpaceValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Attribute1(Annotated):
    class Meta:
        name = "attribute"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    use: AttributeUse = field(
        default=AttributeUse.OPTIONAL,
        metadata={
            "type": "Attribute",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fixed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: Optional[FormChoice] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Enumeration(NoFixedFacet):
    class Meta:
        name = "enumeration"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class FractionDigits(NumFacet):
    class Meta:
        name = "fractionDigits"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Key(Keybase):
    class Meta:
        name = "key"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Keyref(Keybase):
    class Meta:
        name = "keyref"
        namespace = "http://www.w3.org/2001/XMLSchema"

    refer: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Length(NumFacet):
    class Meta:
        name = "length"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class List(Annotated):
    class Meta:
        name = "list"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    item_type: Optional[QName] = field(
        default=None,
        metadata={
            "name": "itemType",
            "type": "Attribute",
        },
    )


@dataclass
class MaxLength(NumFacet):
    class Meta:
        name = "maxLength"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MinLength(NumFacet):
    class Meta:
        name = "minLength"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Pattern(NoFixedFacet):
    class Meta:
        name = "pattern"
        namespace = "http://www.w3.org/2001/XMLSchema"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SimpleType(TopLevelSimpleType):
    class Meta:
        name = "simpleType"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TotalDigits(NumFacet):
    class Meta:
        name = "totalDigits"
        namespace = "http://www.w3.org/2001/XMLSchema"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class UnionType(Annotated):
    class Meta:
        name = "union"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: list[LocalSimpleType] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    member_types: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "memberTypes",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class Unique(Keybase):
    class Meta:
        name = "unique"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AttributeGroupAbstract(Annotated):
    class Meta:
        name = "attributeGroup"

    attribute: list[Attribute1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list["AttributeGroupRef"] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Restriction(Annotated):
    class Meta:
        name = "restriction"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    min_exclusive: list[MinExclusive] = field(
        default_factory=list,
        metadata={
            "name": "minExclusive",
            "type": "Element",
        },
    )
    min_inclusive: list[MinInclusive] = field(
        default_factory=list,
        metadata={
            "name": "minInclusive",
            "type": "Element",
        },
    )
    max_exclusive: list[MaxExclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxExclusive",
            "type": "Element",
        },
    )
    max_inclusive: list[MaxInclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxInclusive",
            "type": "Element",
        },
    )
    total_digits: list[TotalDigits] = field(
        default_factory=list,
        metadata={
            "name": "totalDigits",
            "type": "Element",
        },
    )
    fraction_digits: list[FractionDigits] = field(
        default_factory=list,
        metadata={
            "name": "fractionDigits",
            "type": "Element",
        },
    )
    length: list[Length] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    min_length: list[MinLength] = field(
        default_factory=list,
        metadata={
            "name": "minLength",
            "type": "Element",
        },
    )
    max_length: list[MaxLength] = field(
        default_factory=list,
        metadata={
            "name": "maxLength",
            "type": "Element",
        },
    )
    enumeration: list[Enumeration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    white_space: list[WhiteSpace] = field(
        default_factory=list,
        metadata={
            "name": "whiteSpace",
            "type": "Element",
        },
    )
    pattern: list[Pattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TopLevelAttribute(Attribute1):
    class Meta:
        name = "topLevelAttribute"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    form: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    use: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Attribute(TopLevelAttribute):
    class Meta:
        name = "attribute"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AttributeGroupRef(AttributeGroupAbstract):
    class Meta:
        name = "attributeGroupRef"

    attribute: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    attribute_group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_attribute: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class NamedAttributeGroup(AttributeGroupAbstract):
    class Meta:
        name = "namedAttributeGroup"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class AttributeGroup(NamedAttributeGroup):
    class Meta:
        name = "attributeGroup"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ComplexTypeAbstract(Annotated):
    """
    :ivar simple_content:
    :ivar complex_content:
    :ivar group:
    :ivar all:
    :ivar choice:
    :ivar sequence:
    :ivar attribute:
    :ivar attribute_group:
    :ivar any_attribute:
    :ivar name: Will be restricted to required or forbidden
    :ivar mixed: Not allowed if simpleContent child is chosen. May be
        overriden by setting on complexContent child.
    :ivar abstract:
    :ivar final:
    :ivar block:
    """

    class Meta:
        name = "complexType"

    simple_content: Optional["SimpleContent"] = field(
        default=None,
        metadata={
            "name": "simpleContent",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    complex_content: Optional["ComplexContent"] = field(
        default=None,
        metadata={
            "name": "complexContent",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    group: Optional["GroupRef"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: Optional["All"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: Optional["Choice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: Optional["Sequence"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute: list[Attribute1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    final: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    block: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LocalComplexType(ComplexTypeAbstract):
    class Meta:
        name = "localComplexType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    abstract: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    final: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    block: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class TopLevelComplexType(ComplexTypeAbstract):
    class Meta:
        name = "topLevelComplexType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ComplexType(TopLevelComplexType):
    class Meta:
        name = "complexType"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ElementAbstract(Annotated):
    """The element element can be used either at the top level to define an
    element-type binding globally, or within a content model to either reference a
    globally-defined element or type or declare an element-type binding locally.

    The ref form is not allowed at the top level.
    """

    class Meta:
        name = "element"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    complex_type: Optional[LocalComplexType] = field(
        default=None,
        metadata={
            "name": "complexType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    unique: list[Unique] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    key: list[Key] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    keyref: list[Keyref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    substitution_group: Optional[QName] = field(
        default=None,
        metadata={
            "name": "substitutionGroup",
            "type": "Attribute",
        },
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fixed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nillable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    final: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    block: Optional[BlockSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: Optional[FormChoice] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LocalElement(ElementAbstract):
    class Meta:
        name = "localElement"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    substitution_group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    final: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    abstract: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class TopLevelElement(ElementAbstract):
    class Meta:
        name = "topLevelElement"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    form: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Element(TopLevelElement):
    class Meta:
        name = "element"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class GroupAbstract(Annotated):
    """
    Group type for explicit groups, named top-level groups and group references.
    """

    class Meta:
        name = "group"

    element: list[LocalElement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    group: list["GroupRef"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: list["All"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: list["Choice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: list["Sequence"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any: list[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )


@dataclass
class NarrowMaxMin(LocalElement):
    """
    Restricted max/min.
    """

    class Meta:
        name = "narrowMaxMin"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: NarrowMaxMinMinOccurs = field(
        default=NarrowMaxMinMinOccurs.VALUE_1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: NarrowMaxMinMaxOccurs = field(
        default=NarrowMaxMinMaxOccurs.VALUE_1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )


@dataclass
class ExplicitGroup(GroupAbstract):
    """
    Group type for the three kinds of group.
    """

    class Meta:
        name = "explicitGroup"

    all: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class RealGroup(GroupAbstract):
    class Meta:
        name = "realGroup"

    element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Redefine(OpenAttrs):
    class Meta:
        name = "redefine"
        namespace = "http://www.w3.org/2001/XMLSchema"

    annotation: list[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    simple_type: list[SimpleTypeAbstract] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    complex_type: list[ComplexTypeAbstract] = field(
        default_factory=list,
        metadata={
            "name": "complexType",
            "type": "Element",
        },
    )
    group: list[GroupAbstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attribute_group: list[AttributeGroupAbstract] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
        },
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class All(ExplicitGroup):
    """
    Only elements allowed inside.
    """

    class Meta:
        name = "all"
        namespace = "http://www.w3.org/2001/XMLSchema"

    all: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: AllMinOccurs = field(
        default=AllMinOccurs.VALUE_1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: AllMaxOccurs = field(
        default=AllMaxOccurs.VALUE_1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )


@dataclass
class Choice(ExplicitGroup):
    class Meta:
        name = "choice"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class GroupRef(RealGroup):
    class Meta:
        name = "groupRef"

    element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    all: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Schema(OpenAttrs):
    class Meta:
        name = "schema"
        namespace = "http://www.w3.org/2001/XMLSchema"

    include: list[Include] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    import_value: list[Import] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
        },
    )
    redefine: list[Redefine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    annotation: list[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    simple_type: list[SimpleTypeAbstract] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    complex_type: list[ComplexTypeAbstract] = field(
        default_factory=list,
        metadata={
            "name": "complexType",
            "type": "Element",
        },
    )
    group: list[GroupAbstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attribute_group: list[AttributeGroupAbstract] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
        },
    )
    element: list[ElementAbstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attribute: list[Attribute1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notation: list[Notation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetNamespace",
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    final_default: str = field(
        default="",
        metadata={
            "name": "finalDefault",
            "type": "Attribute",
        },
    )
    block_default: str = field(
        default="",
        metadata={
            "name": "blockDefault",
            "type": "Attribute",
        },
    )
    attribute_form_default: FormChoice = field(
        default=FormChoice.UNQUALIFIED,
        metadata={
            "name": "attributeFormDefault",
            "type": "Attribute",
        },
    )
    element_form_default: FormChoice = field(
        default=FormChoice.UNQUALIFIED,
        metadata={
            "name": "elementFormDefault",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class Sequence(ExplicitGroup):
    class Meta:
        name = "sequence"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class SimpleExplicitGroup(ExplicitGroup):
    class Meta:
        name = "simpleExplicitGroup"

    all: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ExtensionType(Annotated):
    class Meta:
        name = "extensionType"

    group: Optional[GroupRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: Optional[All] = field(
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
    attribute: list[Attribute1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NamedGroup(RealGroup):
    class Meta:
        name = "namedGroup"

    element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    all: list["NamedGroup.All"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: list[SimpleExplicitGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: list[SimpleExplicitGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )

    @dataclass
    class All(All):
        all: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        any_element: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        group: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        choice: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        sequence: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        any: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        min_occurs: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        max_occurs: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )


@dataclass
class RestrictionType(Annotated):
    class Meta:
        name = "restrictionType"

    group: Optional[GroupRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: Optional[All] = field(
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
    attribute: list[Attribute1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ComplexRestrictionType(RestrictionType):
    class Meta:
        name = "complexRestrictionType"

    simple_type: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_exclusive: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_inclusive: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_exclusive: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_inclusive: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    total_digits: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    fraction_digits: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    length: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_length: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_length: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    enumeration: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    white_space: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    pattern: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Group(NamedGroup):
    class Meta:
        name = "group"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class SimpleExtensionType(ExtensionType):
    class Meta:
        name = "simpleExtensionType"

    group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    all: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class SimpleRestrictionType(RestrictionType):
    class Meta:
        name = "simpleRestrictionType"

    group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    all: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ComplexContent(Annotated):
    """
    :ivar restriction:
    :ivar extension:
    :ivar mixed: Overrides any setting on complexType parent.
    """

    class Meta:
        name = "complexContent"
        namespace = "http://www.w3.org/2001/XMLSchema"

    restriction: Optional[ComplexRestrictionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mixed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SimpleContent(Annotated):
    class Meta:
        name = "simpleContent"
        namespace = "http://www.w3.org/2001/XMLSchema"

    restriction: Optional[SimpleRestrictionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    extension: Optional[SimpleExtensionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
