---
title: CFXMLExternalID
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlexternalid
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlexternalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlexternalid.json'
content_hash: 'sha256:340da58a4ac03ac8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLExternalID

<sub>Structure</sub>

Contains the system and public IDs for an external entity reference.

<sub>macOS</sub>

```swift
struct CFXMLExternalID
```

## Overview

This structure is part of the definition of the [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md), [CFXMLNotationInfo](cfxmlnotationinfo.md), and [CFXMLEntityInfo](cfxmlentityinfo.md) structures.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlexternalid/init().md>)
- [init(systemID:publicID:)](<cfxmlexternalid/init(systemid_publicid_).md>)

### Instance Properties

- [publicID](cfxmlexternalid/publicid.md) — The publicID string.
- [systemID](cfxmlexternalid/systemid.md) — The systemID URL.

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
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
