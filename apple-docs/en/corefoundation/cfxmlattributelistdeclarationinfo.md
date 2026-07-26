---
title: CFXMLAttributeListDeclarationInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlattributelistdeclarationinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlattributelistdeclarationinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlattributelistdeclarationinfo.json'
content_hash: 'sha256:eafa97e510d1377d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLAttributeListDeclarationInfo

<sub>Structure</sub>

Contains a list of the attributes associated with an element.

<sub>macOS</sub>

```swift
struct CFXMLAttributeListDeclarationInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an attribute declaration in the DTD. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain the pointer to this structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlattributelistdeclarationinfo/init().md>)
- [init(numberOfAttributes:attributes:)](<cfxmlattributelistdeclarationinfo/init(numberofattributes_attributes_).md>)

### Instance Properties

- [attributes](cfxmlattributelistdeclarationinfo/attributes.md) — A C array of attributes.
- [numberOfAttributes](cfxmlattributelistdeclarationinfo/numberofattributes.md) — The number of attributes in the array.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
