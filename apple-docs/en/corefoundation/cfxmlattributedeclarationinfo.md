---
title: CFXMLAttributeDeclarationInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlattributedeclarationinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlattributedeclarationinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlattributedeclarationinfo.json'
content_hash: 'sha256:6f8bce5baaa39332'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLAttributeDeclarationInfo

<sub>Structure</sub>

Contains information about an element attribute definition.

<sub>macOS</sub>

```swift
struct CFXMLAttributeDeclarationInfo
```

## Overview

This structure is part of the definition of the [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlattributedeclarationinfo/init().md>)
- [init(attributeName:typeString:defaultString:)](<cfxmlattributedeclarationinfo/init(attributename_typestring_defaultstring_).md>)

### Instance Properties

- [attributeName](cfxmlattributedeclarationinfo/attributename.md) — The name of the attribute.
- [defaultString](cfxmlattributedeclarationinfo/defaultstring.md) — The attribute’s default value.
- [typeString](cfxmlattributedeclarationinfo/typestring.md) — Describes the declaration of a single attribute.

## See Also

### Data Types

- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityInfo](cfxmlentityinfo.md) — Contains information describing an XML entity.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
