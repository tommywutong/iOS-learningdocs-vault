---
title: deletedModelsArray
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/deletedmodelsarray
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/deletedmodelsarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/deletedmodelsarray.json'
content_hash: 'sha256:09145aba70bc7137'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# deletedModelsArray

<sub>Instance Property</sub>

The array of registered models that the context will remove from the persistent storage during the next save operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deletedModelsArray: [any PersistentModel] { get }
```

## See Also

### Deleting models

- [delete(_:)](<delete(__).md>) — Removes the specified model from the persistent storage during the next save operation.
- [delete(model:where:includeSubclasses:)](<delete(model_where_includesubclasses_).md>) — Removes each model satisfying the given predicate from the persistent storage during the next save operation.
