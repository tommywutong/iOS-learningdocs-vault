---
title: predicate
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydescriptor/predicate
source_url: 'https://developer.apple.com/documentation/swiftdata/historydescriptor/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydescriptor/predicate.json'
content_hash: 'sha256:2f58cb5c6db6e460'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDescriptor](../historydescriptor.md)

# predicate

<sub>Instance Property</sub>

The predicate used to initialize the history descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var predicate: Predicate<TransactionType>?
```

## See Also

### Getting the descriptor configuration

- [fetchLimit](fetchlimit.md) — The maximum number of transactions to retrieve from the model store’s history.
- [sortBy](sortby.md) — The sort descriptor to use to sort the returned history data.
