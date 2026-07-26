---
title: CFXMLElementInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlelementinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlelementinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlelementinfo.json'
content_hash: 'sha256:fcfb820f3118b1b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLElementInfo

<sub>Structure</sub>

Contains a list of element attributes packaged as CFDictionary key/value pairs.

<sub>macOS</sub>

```swift
struct CFXMLElementInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an element containing attributes. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlelementinfo/init().md>)

### Instance Properties

- [attributeOrder](cfxmlelementinfo/attributeorder.md) — An array specifying the order in which the attributes appeared in the XML document.
- [attributes](cfxmlelementinfo/attributes.md) — The dictionary of attribute values.
- [isEmpty](cfxmlelementinfo/isempty.md) — A flag indicating whether the element was expressed in closed form.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
