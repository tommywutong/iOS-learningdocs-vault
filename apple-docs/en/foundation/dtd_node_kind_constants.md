---
title: DTD Node Kind Constants
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dtd_node_kind_constants
source_url: 'https://developer.apple.com/documentation/foundation/dtd_node_kind_constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dtd_node_kind_constants.json'
content_hash: 'sha256:7f6352c4f5b5e68f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Archives and Serialization](archives-and-serialization.md) · [XML Processing and Modeling](xml-processing-and-modeling.md) · [XMLDTDNode](xmldtdnode.md)

# DTD Node Kind Constants

<sub>API Collection</sub>

Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.

## Topics

### Constants

- [NSXMLEntityGeneralKind](xmldtdnode/dtdkind-swift.enum/general.md) — Identifies a general entity declaration.
- [NSXMLEntityParsedKind](xmldtdnode/dtdkind-swift.enum/parsed.md) — Identifies a parsed entity declaration.
- [NSXMLEntityUnparsedKind](xmldtdnode/dtdkind-swift.enum/unparsed.md) — Identifies an unparsed entity declaration.
- [NSXMLEntityParameterKind](xmldtdnode/dtdkind-swift.enum/parameter.md) — Identifies a parameter entity declaration.
- [NSXMLEntityPredefined](xmldtdnode/dtdkind-swift.enum/predefined.md) — Identifies a predefined entity declaration.
- [NSXMLAttributeCDATAKind](xmldtdnode/dtdkind-swift.enum/cdataattribute.md) — Identifies an attribute-list declaration with a `CDATA` (character data) value type.
- [NSXMLAttributeIDKind](xmldtdnode/dtdkind-swift.enum/idattribute.md) — Identifies an attribute-list declaration with an `ID` value type (per-document unique element name).
- [NSXMLAttributeIDRefKind](xmldtdnode/dtdkind-swift.enum/idrefattribute.md) — Identifies an attribute-list declaration with an `IDREF` value type (refers to element `ID` type).
- [NSXMLAttributeIDRefsKind](xmldtdnode/dtdkind-swift.enum/idrefsattribute.md) — Identifies an attribute-list declaration with an `IDREFS` value type (refers to multiple elements of `ID` type).
- [NSXMLAttributeEntityKind](xmldtdnode/dtdkind-swift.enum/entityattribute.md) — Identifies an attribute-list declaration with an `ENTITY` value type (refers to unparsed entity declared in document).
- [NSXMLAttributeEntitiesKind](xmldtdnode/dtdkind-swift.enum/entitiesattribute.md) — Identifies an attribute-list declaration with an `ENTITIES` value type (refers to multiple unparsed entities declared elsewhere in document).
- [NSXMLAttributeNMTokenKind](xmldtdnode/dtdkind-swift.enum/nmtokenattribute.md) — Identifies an attribute-list declaration with a `NMTOKEN` value type (name token).
- [NSXMLAttributeNMTokensKind](xmldtdnode/dtdkind-swift.enum/nmtokensattribute.md) — Identifies an attribute-list declaration with a `NMTOKENS` value type (multiple name tokens)
- [NSXMLAttributeEnumerationKind](xmldtdnode/dtdkind-swift.enum/enumerationattribute.md) — Identifies an attribute-list declaration with an enumeration value type (list of all possible values).
- [NSXMLAttributeNotationKind](xmldtdnode/dtdkind-swift.enum/notationattribute.md) — Identifies an attribute-list declaration with a `NOTATION` value type (name of declared notation).
- [NSXMLElementDeclarationUndefinedKind](xmldtdnode/dtdkind-swift.enum/undefineddeclaration.md) — Identifies an undefined element declaration.
- [NSXMLElementDeclarationEmptyKind](xmldtdnode/dtdkind-swift.enum/emptydeclaration.md) — Identifies a declaration (`EMPTY`) of an empty element.
- [NSXMLElementDeclarationAnyKind](xmldtdnode/dtdkind-swift.enum/anydeclaration.md) — Identifies an `ANY` element declaration.
- [NSXMLElementDeclarationMixedKind](xmldtdnode/dtdkind-swift.enum/mixeddeclaration.md) — Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).
- [NSXMLElementDeclarationElementKind](xmldtdnode/dtdkind-swift.enum/elementdeclaration.md) — Identifies a declaration of an element with child elements.

## See Also

### Constants

- [DTDKind](xmldtdnode/dtdkind-swift.enum.md) — The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
