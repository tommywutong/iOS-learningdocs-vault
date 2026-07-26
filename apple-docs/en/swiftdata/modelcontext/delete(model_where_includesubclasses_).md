---
title: 'delete(model:where:includeSubclasses:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/delete(model:where:includesubclasses:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/delete(model:where:includesubclasses:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/delete%28model%3Awhere%3Aincludesubclasses%3A%29.json'
content_hash: 'sha256:975adba64be3ac5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# delete(model:where:includeSubclasses:)

<sub>Instance Method</sub>

Removes each model satisfying the given predicate from the persistent storage during the next save operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func delete<T>(model: T.Type, where predicate: Predicate<T>? = nil, includeSubclasses: Bool = true) throws where T : PersistentModel
```

## Parameters

- `model` — The type of the model to remove.

- `predicate` — The logical condition to use when determining if the context should remove a particular model. The default value is `nil`.

- `includeSubclasses` — A Boolean value that indicates whether the context includes subclasses of the specified model type when evaluating models to remove. The default value is `true`.

## Discussion

> [!warning] Warning
> If you don’t provide a predicate, the context will remove all models of the specified type from the persistent storage.

## See Also

### Deleting models

- [deletedModelsArray](deletedmodelsarray.md) — The array of registered models that the context will remove from the persistent storage during the next save operation.
- [delete(_:)](<delete(__).md>) — Removes the specified model from the persistent storage during the next save operation.
