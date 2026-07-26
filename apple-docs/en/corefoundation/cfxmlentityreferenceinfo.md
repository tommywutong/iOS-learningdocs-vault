---
title: CFXMLEntityReferenceInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlentityreferenceinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlentityreferenceinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlentityreferenceinfo.json'
content_hash: 'sha256:6ce5ac16d997a95b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLEntityReferenceInfo

<sub>Structure</sub>

Contains information describing an XML entity reference.

<sub>macOS</sub>

```swift
struct CFXMLEntityReferenceInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an entity reference. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfxmlentityreferenceinfo/init().md>)
- [init(entityType:)](<cfxmlentityreferenceinfo/init(entitytype_).md>)

### Instance Properties

- [entityType](cfxmlentityreferenceinfo/entitytype.md) — The entity type code.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
