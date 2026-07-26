---
title: 'insert(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/insert(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/insert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/insert%28_%3A%29.json'
content_hash: 'sha256:e2eba4553f961533'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# insert(_:)

<sub>Instance Method</sub>

Registers the specified model with the context so it can include the model in the next save operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insert<T>(_ model: T) where T : PersistentModel
```

## Parameters

- `model` — The model to include in the next save operation.

## Discussion

A model is given a temporary persistent identifier until the first time a context saves it, after which that context assigns a permanent identifier. If you call [rollback()](<rollback().md>) after inserting a model but before the next save operation, the context discards that model.

## See Also

### Inserting models

- [insertedModelsArray](insertedmodelsarray.md) — The array of inserted models that the context is yet to persist.
