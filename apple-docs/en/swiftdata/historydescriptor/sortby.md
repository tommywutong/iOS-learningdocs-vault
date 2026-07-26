---
title: sortBy
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydescriptor/sortby
source_url: 'https://developer.apple.com/documentation/swiftdata/historydescriptor/sortby'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydescriptor/sortby.json'
content_hash: 'sha256:235c62b95bd977d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDescriptor](../historydescriptor.md)

# sortBy

<sub>Instance Property</sub>

The sort descriptor to use to sort the returned history data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sortBy: [SortDescriptor<TransactionType>]
```

## See Also

### Getting the descriptor configuration

- [fetchLimit](fetchlimit.md) — The maximum number of transactions to retrieve from the model store’s history.
- [predicate](predicate.md) — The predicate used to initialize the history descriptor.
