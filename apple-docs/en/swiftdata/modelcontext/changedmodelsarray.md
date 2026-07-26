---
title: changedModelsArray
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/changedmodelsarray
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/changedmodelsarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/changedmodelsarray.json'
content_hash: 'sha256:3d6c230c33651b03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# changedModelsArray

<sub>Instance Property</sub>

The array of registered models that have unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var changedModelsArray: [any PersistentModel] { get }
```

## See Also

### Modifying models

- [hasChanges](haschanges.md) — A Boolean value that indicates whether the context has unsaved changes.
