---
title: SecRequirementType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secrequirementtype
source_url: 'https://developer.apple.com/documentation/security/secrequirementtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrequirementtype.json'
content_hash: 'sha256:8b96a1c240d5dad4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRequirementType

<sub>Enumeration</sub>

An enumeration indicating different types of internal requirements for code.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecRequirementType
```

## Overview

These constants are indexes into requirement sets and are not currently used in any public API.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecHostRequirementType](secrequirementtype/hostrequirementtype.md) — What hosts may run this code.
- [kSecGuestRequirementType](secrequirementtype/guestrequirementtype.md) — What guests this code may run.
- [kSecDesignatedRequirementType](secrequirementtype/designatedrequirementtype.md) — A designated requirement.
- [kSecLibraryRequirementType](secrequirementtype/libraryrequirementtype.md) — What libraries this code may link against.
- [kSecPluginRequirementType](secrequirementtype/pluginrequirementtype.md) — What plug-ins this code may load.
- [kSecInvalidRequirementType](secrequirementtype/invalidrequirementtype.md) — Invalid type of requirement.
- [kSecRequirementTypeCount](secrequirementtype/requirementtypecount.md) — The number of valid requirement types.

### Initializers

- [init(rawValue:)](<secrequirementtype/init(rawvalue_).md>)
