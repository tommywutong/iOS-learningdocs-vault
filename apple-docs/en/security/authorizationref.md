---
title: AuthorizationRef
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationref
source_url: 'https://developer.apple.com/documentation/security/authorizationref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationref.json'
content_hash: 'sha256:f2d0c952526976d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationRef

<sub>Type Alias</sub>

A pointer to an opaque authorization reference structure.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias AuthorizationRef = OpaquePointer
```

## Discussion

This data type points to a structure the Security Server uses to store information about the authorization session. Use the functions described in [Authorization Services](authorization-services.md) to create, access, and free the authorization reference.
