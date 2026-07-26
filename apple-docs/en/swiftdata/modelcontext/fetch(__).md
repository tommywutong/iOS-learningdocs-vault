---
title: 'fetch(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/fetch(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/fetch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/fetch%28_%3A%29.json'
content_hash: 'sha256:ef2c65e814b9fbc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# fetch(_:)

<sub>Instance Method</sub>

Returns an array of typed models that match the criteria of the specified fetch descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetch<T>(_ descriptor: FetchDescriptor<T>) throws -> [T] where T : PersistentModel
```

## Parameters

- `descriptor` — A fetch descriptor that provides the configuration for the fetch.

## Return Value

The array of typed models that satisfy the criteria of the fetch descriptor. If no models match the criteria, the array is empty.

## See Also

### Fetching models

- [fetch(_:batchSize:)](<fetch(__batchsize_).md>) — Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [fetchCount(_:)](<fetchcount(__).md>) — Returns the number of models that match the criteria of the specified fetch descriptor.
- [FetchDescriptor](../fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [FetchResultsCollection](../fetchresultscollection.md) — A collection that efficiently provides the results of a completed fetch.
- [enumerate(_:batchSize:allowEscapingMutations:block:)](<enumerate(__batchsize_allowescapingmutations_block_).md>) — Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [model(for:)](<model(for_).md>) — Returns the persistent model for the specified identifier.
- [registeredModel(for:)](<registeredmodel(for_).md>) — Returns the typed model for the specified identifier.
