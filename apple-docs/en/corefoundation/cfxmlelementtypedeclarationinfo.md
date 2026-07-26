---
title: CFXMLElementTypeDeclarationInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlelementtypedeclarationinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlelementtypedeclarationinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlelementtypedeclarationinfo.json'
content_hash: 'sha256:2445e2b43851dd1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLElementTypeDeclarationInfo

<sub>Structure</sub>

Contains a description of the element type.

<sub>macOS</sub>

```swift
struct CFXMLElementTypeDeclarationInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode passed to your application when the parser encounters and element type declaration. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain a pointer to this structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlelementtypedeclarationinfo/init().md>)
- [init(contentDescription:)](<cfxmlelementtypedeclarationinfo/init(contentdescription_).md>)

### Instance Properties

- [contentDescription](cfxmlelementtypedeclarationinfo/contentdescription.md) — A textual description of the element type.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
