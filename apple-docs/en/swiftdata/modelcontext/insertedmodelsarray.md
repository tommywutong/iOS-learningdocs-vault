---
title: insertedModelsArray
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/insertedmodelsarray
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/insertedmodelsarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/insertedmodelsarray.json'
content_hash: 'sha256:b46eef9517a61307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# insertedModelsArray

<sub>Instance Property</sub>

The array of inserted models that the context is yet to persist.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var insertedModelsArray: [any PersistentModel] { get }
```

## See Also

### Inserting models

- [insert(_:)](<insert(__).md>) — Registers the specified model with the context so it can include the model in the next save operation.
