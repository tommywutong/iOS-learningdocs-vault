---
title: 'delete(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/delete(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/delete(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/delete%28_%3A%29.json'
content_hash: 'sha256:14877a279c8f3efa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# delete(_:)

<sub>Instance Method</sub>

Removes the specified model from the persistent storage during the next save operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func delete<T>(_ model: T) where T : PersistentModel
```

## Parameters

- `model` — The persistent model to delete.

## Discussion

When the context nexts commits its changes, SwiftData removes the model from the persistent storage. If the model is new and in an unsaved state, the context simply discards it.

## See Also

### Deleting models

- [deletedModelsArray](deletedmodelsarray.md) — The array of registered models that the context will remove from the persistent storage during the next save operation.
- [delete(model:where:includeSubclasses:)](<delete(model_where_includesubclasses_).md>) — Removes each model satisfying the given predicate from the persistent storage during the next save operation.
