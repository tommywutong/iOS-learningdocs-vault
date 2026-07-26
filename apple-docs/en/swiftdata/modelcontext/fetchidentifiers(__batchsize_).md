---
title: 'fetchIdentifiers(_:batchSize:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/fetchidentifiers(_:batchsize:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/fetchidentifiers(_:batchsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/fetchidentifiers%28_%3Abatchsize%3A%29.json'
content_hash: 'sha256:41d0e6315b32d5a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# fetchIdentifiers(_:batchSize:)

<sub>Instance Method</sub>

Returns a collection of persistent identifiers, in batches, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchIdentifiers<T>(_ descriptor: FetchDescriptor<T>, batchSize: Int) throws -> FetchResultsCollection<PersistentIdentifier> where T : PersistentModel
```

## Parameters

- `descriptor` — A fetch descriptor that provides the configuration for the fetch.

- `batchSize` — The maximum number of identifiers to include in each batch.

## Return Value

The collection of persistent identifiers. If no models match the descriptor’s criteria, the array is empty.

## Discussion

The collection automatically fetches subsequent batches as you iterate over the identifiers, or access one at a specific index.

## See Also

### Fetching only persistent identifiers

- [fetchIdentifiers(_:)](<fetchidentifiers(__).md>) — Returns an array of persistent identifiers, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.
