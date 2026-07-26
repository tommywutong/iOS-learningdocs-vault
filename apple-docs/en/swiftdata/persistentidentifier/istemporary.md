---
title: isTemporary
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/persistentidentifier/istemporary
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentidentifier/istemporary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentidentifier/istemporary.json'
content_hash: 'sha256:37588b8970d99a74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [PersistentIdentifier](../persistentidentifier.md)

# isTemporary

<sub>Instance Property</sub>

A Boolean value that indicates whether the identifier is temporary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isTemporary: Bool { get }
```

## Discussion

A temporary identifier is assigned to a model when it is first initialized. Once you call [save()](<../modelcontext/save().md>), the model receives a permanent identifier.

Temporary identifiers should not be persisted or used to create durable maps to a model. Temporary identifiers are only valid until an object is persisted, and must be remapped to the permanent identifier once a model is saved.

```swift
if model.persistentModelID.isTemporary {
    try modelContext.save()
}
let data = try JSONEncoder().encode(model.persistentModelID)
```
