---
title: CFXMLProcessingInstructionInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlprocessinginstructioninfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlprocessinginstructioninfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlprocessinginstructioninfo.json'
content_hash: 'sha256:0e0ef5b369e78373'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLProcessingInstructionInfo

<sub>Structure</sub>

Contains the text of the processing instruction.

<sub>macOS</sub>

```swift
struct CFXMLProcessingInstructionInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters a processing instruction. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlprocessinginstructioninfo/init().md>)
- [init(dataString:)](<cfxmlprocessinginstructioninfo/init(datastring_).md>)

### Instance Properties

- [dataString](cfxmlprocessinginstructioninfo/datastring.md) — The text of the processing instruction.

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
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
