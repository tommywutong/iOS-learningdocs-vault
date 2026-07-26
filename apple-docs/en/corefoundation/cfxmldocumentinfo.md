---
title: CFXMLDocumentInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmldocumentinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmldocumentinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmldocumentinfo.json'
content_hash: 'sha256:be4bd87d99b7c244'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLDocumentInfo

<sub>Structure</sub>

Contains the source URL and text encoding information for the XML document.

<sub>macOS</sub>

```swift
struct CFXMLDocumentInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters the XML declaration. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmldocumentinfo/init().md>)
- [init(sourceURL:encoding:)](<cfxmldocumentinfo/init(sourceurl_encoding_).md>)

### Instance Properties

- [encoding](cfxmldocumentinfo/encoding.md) — The text encoding of the XML document.
- [sourceURL](cfxmldocumentinfo/sourceurl.md) — The source URL of the XML document.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
