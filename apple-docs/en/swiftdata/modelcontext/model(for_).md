---
title: 'model(for:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/model(for:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/model(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/model%28for%3A%29.json'
content_hash: 'sha256:c8fe2133c1c8639e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# model(for:)

<sub>Instance Method</sub>

Returns the persistent model for the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func model(for persistentModelID: PersistentIdentifier) -> any PersistentModel
```

## Parameters

- `persistentModelID` — The identifier of the model to fetch. For more information, see [PersistentIdentifier](../persistentidentifier.md).

## Return Value

The identified persistent model, if known to the context; otherwise, an unsaved model with its [persistentModelID](../persistentmodel/persistentmodelid.md) property set to `persistentModelID`.

## See Also

### Fetching models

- [fetch(_:)](<fetch(__).md>) — Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [fetch(_:batchSize:)](<fetch(__batchsize_).md>) — Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [fetchCount(_:)](<fetchcount(__).md>) — Returns the number of models that match the criteria of the specified fetch descriptor.
- [FetchDescriptor](../fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [FetchResultsCollection](../fetchresultscollection.md) — A collection that efficiently provides the results of a completed fetch.
- [enumerate(_:batchSize:allowEscapingMutations:block:)](<enumerate(__batchsize_allowescapingmutations_block_).md>) — Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [registeredModel(for:)](<registeredmodel(for_).md>) — Returns the typed model for the specified identifier.
