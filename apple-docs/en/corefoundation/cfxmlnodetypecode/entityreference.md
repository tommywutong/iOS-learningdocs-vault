---
title: CFXMLNodeTypeCode.entityReference
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlnodetypecode/entityreference
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodetypecode/entityreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodetypecode/entityreference.json'
content_hash: 'sha256:3dcfc5eb6af28bf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLNodeTypeCode](../cfxmlnodetypecode.md)

# CFXMLNodeTypeCode.entityReference

<sub>Case</sub>

Indicates an entity reference where the data string is the name of the referenced entity and the additional information is a pointer to a [CFXMLEntityReferenceInfo](../cfxmlentityreferenceinfo.md) structure.

<sub>macOS</sub>

```swift
case entityReference
```

## See Also

### Constants

- [kCFXMLNodeTypeDocument](document.md) — Indicates a document where the data string is `NULL` and the additional information is a pointer to a [CFXMLDocumentInfo](../cfxmldocumentinfo.md) structure.
- [kCFXMLNodeTypeElement](element.md) — Indicates an element where the data string is the name of the tag and the additional information is a pointer to a [CFXMLElementInfo](../cfxmlelementinfo.md) structure.
- [kCFXMLNodeTypeAttribute](attribute.md) — Currently not used.
- [kCFXMLNodeTypeProcessingInstruction](processinginstruction.md) — Indicates a processing instruction where the data string is the name of the target and the additional information is a pointer to a [CFXMLProcessingInstructionInfo](../cfxmlprocessinginstructioninfo.md) structure.
- [kCFXMLNodeTypeComment](comment.md) — Indicates a comment section where the data string is the text of the comment and the additional information is `NULL`.
- [kCFXMLNodeTypeText](text.md) — Indicates a text section where the data string is the text’s contents and the additional information is `NULL`.
- [kCFXMLNodeTypeCDATASection](cdatasection.md) — Indicates a CDATA section where the data string is the text of the CDATA and the additional information is `NULL`.
- [kCFXMLNodeTypeDocumentFragment](documentfragment.md) — Currently not used.
- [kCFXMLNodeTypeEntity](entity.md) — Indicates an entity where the data string is the name of the entity and the additional information is a pointer to a [CFXMLEntityInfo](../cfxmlentityinfo.md) structure.
- [kCFXMLNodeTypeDocumentType](documenttype.md) — Indicates a document type where the data string is the name given to the top-level element and the additional information is a pointer to a [CFXMLDocumentTypeInfo](../cfxmldocumenttypeinfo.md) structure.
- [kCFXMLNodeTypeWhitespace](whitespace.md) — Indicates white space where the data string is the text of the white space and the additional information is `NULL`.
- [kCFXMLNodeTypeNotation](notation.md) — Indicates a notation where the data string is the notation name and the additional information is a pointer to a [CFXMLNotationInfo](../cfxmlnotationinfo.md) structure.
- [kCFXMLNodeTypeElementTypeDeclaration](elementtypedeclaration.md) — Indicates an element type declaration where the data string is the tag name and the additional information is a pointer to a [CFXMLElementTypeDeclarationInfo](../cfxmlelementtypedeclarationinfo.md) structure.
- [kCFXMLNodeTypeAttributeListDeclaration](attributelistdeclaration.md) — Indicates an attribute list declaration where the data string is the tag name and the additional information is a pointer to a [CFXMLAttributeListDeclarationInfo](../cfxmlattributelistdeclarationinfo.md) structure.
