---
title: CFXMLEntityTypeCode
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlentitytypecode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlentitytypecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlentitytypecode.json'
content_hash: 'sha256:ae353d65d5f8b295'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLEntityTypeCode

<sub>Enumeration</sub>

The entity type identification codes that the parser uses to describe XML entities.

<sub>macOS</sub>

```swift
enum CFXMLEntityTypeCode
```

## Overview

These codes are used with the [CFXMLEntityInfo](cfxmlentityinfo.md) and [CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md) structures.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFXMLEntityTypeParameter](cfxmlentitytypecode/parameter.md) — Implies a parsed, internal entity.
- [kCFXMLEntityTypeParsedInternal](cfxmlentitytypecode/parsedinternal.md) — Indicates a parsed, internal entity.
- [kCFXMLEntityTypeParsedExternal](cfxmlentitytypecode/parsedexternal.md) — Indicates a parsed, external entity.
- [kCFXMLEntityTypeUnparsed](cfxmlentitytypecode/unparsed.md) — Indicates an unparsed entity.
- [kCFXMLEntityTypeCharacter](cfxmlentitytypecode/character.md) — Indicates a character entity type.

### Initializers

- [init(rawValue:)](<cfxmlentitytypecode/init(rawvalue_).md>)

## See Also

### Constants

- [Node Current Version](1443311-node-current-version.md) — The version of a CFXMLNode object.
- [CFXMLNodeTypeCode](cfxmlnodetypecode.md) — The various XML data type identification codes that the parser uses to describe XML structures.
