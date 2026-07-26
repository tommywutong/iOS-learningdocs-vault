---
title: CFXMLNotationInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlnotationinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnotationinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnotationinfo.json'
content_hash: 'sha256:932fc4926a8f633d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNotationInfo

<sub>Structure</sub>

Contains the external ID of the notation.

<sub>macOS</sub>

```swift
struct CFXMLNotationInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters a notation element. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain a pointer to this structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlnotationinfo/init().md>)
- [init(externalID:)](<cfxmlnotationinfo/init(externalid_).md>)

### Instance Properties

- [externalID](cfxmlnotationinfo/externalid.md) — The external ID of the notation.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
