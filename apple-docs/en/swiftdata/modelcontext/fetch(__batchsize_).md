---
title: 'fetch(_:batchSize:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/fetch(_:batchsize:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/fetch(_:batchsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/fetch%28_%3Abatchsize%3A%29.json'
content_hash: 'sha256:0c0502827dfd2954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# fetch(_:batchSize:)

<sub>Instance Method</sub>

Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetch<T>(_ descriptor: FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<T> where T : PersistentModel
```

## Parameters

- `descriptor` — A fetch descriptor that provides the configuration for the fetch.

- `batchSize` — The maximum number of models to include in each batch.

## Return Value

The collection of typed models that satisfy the criteria of the fetch descriptor. If no models match the criteria, the collection is empty.

## Discussion

As you access the models in the returned collection (either sequentially, or directly using subscripting), the context automatically fetches the necessary batches.

## See Also

### Fetching models

- [fetch(_:)](<fetch(__).md>) — Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [fetchCount(_:)](<fetchcount(__).md>) — Returns the number of models that match the criteria of the specified fetch descriptor.
- [FetchDescriptor](../fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [FetchResultsCollection](../fetchresultscollection.md) — A collection that efficiently provides the results of a completed fetch.
- [enumerate(_:batchSize:allowEscapingMutations:block:)](<enumerate(__batchsize_allowescapingmutations_block_).md>) — Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [model(for:)](<model(for_).md>) — Returns the persistent model for the specified identifier.
- [registeredModel(for:)](<registeredmodel(for_).md>) — Returns the typed model for the specified identifier.
