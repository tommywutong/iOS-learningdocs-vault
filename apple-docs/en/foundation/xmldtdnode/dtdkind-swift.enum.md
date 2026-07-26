---
title: XMLDTDNode.DTDKind
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtdnode/dtdkind-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode/dtdkind-swift.enum.json'
content_hash: 'sha256:38523a3690795a86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTDNode](../xmldtdnode.md)

# XMLDTDNode.DTDKind

<sub>Enumeration</sub>

The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.

<sub>Mac Catalyst, macOS</sub>

```swift
enum DTDKind
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NSXMLAttributeCDATAKind](dtdkind-swift.enum/cdataattribute.md) — Identifies an attribute-list declaration with a `CDATA` (character data) value type.
- [NSXMLAttributeEntitiesKind](dtdkind-swift.enum/entitiesattribute.md) — Identifies an attribute-list declaration with an `ENTITIES` value type (refers to multiple unparsed entities declared elsewhere in document).
- [NSXMLAttributeEntityKind](dtdkind-swift.enum/entityattribute.md) — Identifies an attribute-list declaration with an `ENTITY` value type (refers to unparsed entity declared in document).
- [NSXMLAttributeEnumerationKind](dtdkind-swift.enum/enumerationattribute.md) — Identifies an attribute-list declaration with an enumeration value type (list of all possible values).
- [NSXMLAttributeIDKind](dtdkind-swift.enum/idattribute.md) — Identifies an attribute-list declaration with an `ID` value type (per-document unique element name).
- [NSXMLAttributeIDRefKind](dtdkind-swift.enum/idrefattribute.md) — Identifies an attribute-list declaration with an `IDREF` value type (refers to element `ID` type).
- [NSXMLAttributeIDRefsKind](dtdkind-swift.enum/idrefsattribute.md) — Identifies an attribute-list declaration with an `IDREFS` value type (refers to multiple elements of `ID` type).
- [NSXMLAttributeNMTokenKind](dtdkind-swift.enum/nmtokenattribute.md) — Identifies an attribute-list declaration with a `NMTOKEN` value type (name token).
- [NSXMLAttributeNMTokensKind](dtdkind-swift.enum/nmtokensattribute.md) — Identifies an attribute-list declaration with a `NMTOKENS` value type (multiple name tokens)
- [NSXMLAttributeNotationKind](dtdkind-swift.enum/notationattribute.md) — Identifies an attribute-list declaration with a `NOTATION` value type (name of declared notation).
- [NSXMLElementDeclarationAnyKind](dtdkind-swift.enum/anydeclaration.md) — Identifies an `ANY` element declaration.
- [NSXMLElementDeclarationElementKind](dtdkind-swift.enum/elementdeclaration.md) — Identifies a declaration of an element with child elements.
- [NSXMLElementDeclarationEmptyKind](dtdkind-swift.enum/emptydeclaration.md) — Identifies a declaration (`EMPTY`) of an empty element.
- [NSXMLElementDeclarationMixedKind](dtdkind-swift.enum/mixeddeclaration.md) — Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).
- [NSXMLElementDeclarationUndefinedKind](dtdkind-swift.enum/undefineddeclaration.md) — Identifies an undefined element declaration.
- [NSXMLEntityGeneralKind](dtdkind-swift.enum/general.md) — Identifies a general entity declaration.
- [NSXMLEntityParameterKind](dtdkind-swift.enum/parameter.md) — Identifies a parameter entity declaration.
- [NSXMLEntityParsedKind](dtdkind-swift.enum/parsed.md) — Identifies a parsed entity declaration.
- [NSXMLEntityPredefined](dtdkind-swift.enum/predefined.md) — Identifies a predefined entity declaration.
- [NSXMLEntityUnparsedKind](dtdkind-swift.enum/unparsed.md) — Identifies an unparsed entity declaration.

### Initializers

- [init(rawValue:)](<dtdkind-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [DTD Node Kind Constants](../dtd_node_kind_constants.md) — Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
