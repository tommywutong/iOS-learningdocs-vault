---
title: CFXMLEntityInfo
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlentityinfo
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlentityinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlentityinfo.json'
content_hash: 'sha256:ab9a5929e3036b9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLEntityInfo

<sub>Structure</sub>

Contains information describing an XML entity.

<sub>macOS</sub>

```swift
struct CFXMLEntityInfo
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an entity declaration. Use the [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) function to obtain a pointer to this structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlentityinfo/init().md>)
- [init(entityType:replacementText:entityID:notationName:)](<cfxmlentityinfo/init(entitytype_replacementtext_entityid_notationname_).md>)

### Instance Properties

- [entityID](cfxmlentityinfo/entityid.md) — `entityID.systemID` will be `NULL` if `entityType` is internal.
- [entityType](cfxmlentityinfo/entitytype.md) — The entity type code.
- [notationName](cfxmlentityinfo/notationname.md) — `NULL` if `entityType` is parsed.
- [replacementText](cfxmlentityinfo/replacementtext.md) — `NULL` if `entityType` is external or unparsed, otherwise the text that the entity should be replaced with.

## See Also

### Data Types

- [CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md) — Contains information about an element attribute definition.
- [CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md) — Contains a list of the attributes associated with an element.
- [CFXMLDocumentInfo](cfxmldocumentinfo.md) — Contains the source URL and text encoding information for the XML document.
- [CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md) — Contains the external ID of the DTD.
- [CFXMLElementInfo](cfxmlelementinfo.md) — Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md) — Contains a description of the element type.
- [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) — Contains information describing an XML entity reference.
- [CFXMLExternalID](cfxmlexternalid.md) — Contains the system and public IDs for an external entity reference.
- [CFXMLNotationInfo](cfxmlnotationinfo.md) — Contains the external ID of the notation.
- [CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md) — Contains the text of the processing instruction.
