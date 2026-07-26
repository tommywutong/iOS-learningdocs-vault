---
title: fetchLimit
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydescriptor/fetchlimit
source_url: 'https://developer.apple.com/documentation/swiftdata/historydescriptor/fetchlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydescriptor/fetchlimit.json'
content_hash: 'sha256:613e470681a5993a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDescriptor](../historydescriptor.md)

# fetchLimit

<sub>Instance Property</sub>

The maximum number of transactions to retrieve from the model store’s history.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchLimit: UInt64
```

## Discussion

> [!important] Important
> Use `nil` to tell the fetch to return all transactions of the associated type, not `0`.

The default value is `nil`.

## See Also

### Getting the descriptor configuration

- [predicate](predicate.md) — The predicate used to initialize the history descriptor.
- [sortBy](sortby.md) — The sort descriptor to use to sort the returned history data.
