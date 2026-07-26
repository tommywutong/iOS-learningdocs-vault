---
title: 'enumerate(_:batchSize:allowEscapingMutations:block:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/enumerate(_:batchsize:allowescapingmutations:block:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/enumerate(_:batchsize:allowescapingmutations:block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/enumerate%28_%3Abatchsize%3Aallowescapingmutations%3Ablock%3A%29.json'
content_hash: 'sha256:b7ce95002773ba48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# enumerate(_:batchSize:allowEscapingMutations:block:)

<sub>Instance Method</sub>

Runs a closure for each model that matches the criteria of the specified fetch descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerate<T>(_ fetch: FetchDescriptor<T>, batchSize: Int = 5000, allowEscapingMutations: Bool = false, block: (T) throws -> Void) throws where T : PersistentModel
```

## Parameters

- `fetch` — A fetch descriptor that provides the configuration for the fetch.

- `batchSize` — The maximum number of models to include in each batch. The default value is 5000.

- `allowEscapingMutations` — A Boolean value that determines whether the closure can leave the context in a modified state after it completes. The default value is `false`.

- `block` — The closure to run for each fetched model.

## See Also

### Fetching models

- [fetch(_:)](<fetch(__).md>) — Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [fetch(_:batchSize:)](<fetch(__batchsize_).md>) — Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [fetchCount(_:)](<fetchcount(__).md>) — Returns the number of models that match the criteria of the specified fetch descriptor.
- [FetchDescriptor](../fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [FetchResultsCollection](../fetchresultscollection.md) — A collection that efficiently provides the results of a completed fetch.
- [model(for:)](<model(for_).md>) — Returns the persistent model for the specified identifier.
- [registeredModel(for:)](<registeredmodel(for_).md>) — Returns the typed model for the specified identifier.
