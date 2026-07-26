---
title: CFXMLNodeTypeCode
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlnodetypecode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodetypecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodetypecode.json'
content_hash: 'sha256:cb95f67c2ea323cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNodeTypeCode

<sub>Enumeration</sub>

The various XML data type identification codes that the parser uses to describe XML structures.

<sub>macOS</sub>

```swift
enum CFXMLNodeTypeCode
```

## Overview

When the parser encounters a new XML structure, its data type and contents are placed in a CFXMLNode object.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFXMLNodeTypeDocument](cfxmlnodetypecode/document.md) — Indicates a document where the data string is `NULL` and the additional information is a pointer to a [CFXMLDocumentInfo](cfxmldocumentinfo.md) structure.
- [kCFXMLNodeTypeElement](cfxmlnodetypecode/element.md) — Indicates an element where the data string is the name of the tag and the additional information is a pointer to a [CFXMLElementInfo](cfxmlelementinfo.md) structure.
- [kCFXMLNodeTypeAttribute](cfxmlnodetypecode/attribute.md) — Currently not used.
- [kCFXMLNodeTypeProcessingInstruction](cfxmlnodetypecode/processinginstruction.md) — Indicates a processing instruction where the data string is the name of the target and the additional information is a pointer to a [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) structure.
- [kCFXMLNodeTypeComment](cfxmlnodetypecode/comment.md) — Indicates a comment section where the data string is the text of the comment and the additional information is `NULL`.
- [kCFXMLNodeTypeText](cfxmlnodetypecode/text.md) — Indicates a text section where the data string is the text’s contents and the additional information is `NULL`.
- [kCFXMLNodeTypeCDATASection](cfxmlnodetypecode/cdatasection.md) — Indicates a CDATA section where the data string is the text of the CDATA and the additional information is `NULL`.
- [kCFXMLNodeTypeDocumentFragment](cfxmlnodetypecode/documentfragment.md) — Currently not used.
- [kCFXMLNodeTypeEntity](cfxmlnodetypecode/entity.md) — Indicates an entity where the data string is the name of the entity and the additional information is a pointer to a [CFXMLEntityInfo](cfxmlentityinfo.md) structure.
- [kCFXMLNodeTypeEntityReference](cfxmlnodetypecode/entityreference.md) — Indicates an entity reference where the data string is the name of the referenced entity and the additional information is a pointer to a [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) structure.
- [kCFXMLNodeTypeDocumentType](cfxmlnodetypecode/documenttype.md) — Indicates a document type where the data string is the name given to the top-level element and the additional information is a pointer to a [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) structure.
- [kCFXMLNodeTypeWhitespace](cfxmlnodetypecode/whitespace.md) — Indicates white space where the data string is the text of the white space and the additional information is `NULL`.
- [kCFXMLNodeTypeNotation](cfxmlnodetypecode/notation.md) — Indicates a notation where the data string is the notation name and the additional information is a pointer to a [CFXMLNotationInfo](cfxmlnotationinfo.md) structure.
- [kCFXMLNodeTypeElementTypeDeclaration](cfxmlnodetypecode/elementtypedeclaration.md) — Indicates an element type declaration where the data string is the tag name and the additional information is a pointer to a [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) structure.
- [kCFXMLNodeTypeAttributeListDeclaration](cfxmlnodetypecode/attributelistdeclaration.md) — Indicates an attribute list declaration where the data string is the tag name and the additional information is a pointer to a [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) structure.

### Initializers

- [init(rawValue:)](<cfxmlnodetypecode/init(rawvalue_).md>)

## See Also

### Constants

- [CFXMLEntityTypeCode](cfxmlentitytypecode.md) — The entity type identification codes that the parser uses to describe XML entities.
- [Node Current Version](1443311-node-current-version.md) — The version of a CFXMLNode object.
