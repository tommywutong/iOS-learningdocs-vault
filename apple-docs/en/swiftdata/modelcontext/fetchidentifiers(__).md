---
title: 'fetchIdentifiers(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/fetchidentifiers(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/fetchidentifiers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/fetchidentifiers%28_%3A%29.json'
content_hash: 'sha256:ffc31e79c0b79e89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# fetchIdentifiers(_:)

<sub>Instance Method</sub>

Returns an array of persistent identifiers, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchIdentifiers<T>(_ descriptor: FetchDescriptor<T>) throws -> [PersistentIdentifier] where T : PersistentModel
```

## Parameters

- `descriptor` — A fetch descriptor that provides the configuration for the fetch.

## Return Value

The array of persistent identifiers. If no models match the descriptor’s criteria, the array is empty.

## See Also

### Fetching only persistent identifiers

- [fetchIdentifiers(_:batchSize:)](<fetchidentifiers(__batchsize_).md>) — Returns a collection of persistent identifiers, in batches, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.
