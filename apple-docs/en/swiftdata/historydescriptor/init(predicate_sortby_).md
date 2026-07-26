---
title: 'init(predicate:sortBy:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/historydescriptor/init(predicate:sortby:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/historydescriptor/init(predicate:sortby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydescriptor/init%28predicate%3Asortby%3A%29.json'
content_hash: 'sha256:9ab5c39a1c11d3d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryDescriptor](../historydescriptor.md)

# init(predicate:sortBy:)

<sub>Initializer</sub>

Initializes a new history descriptor with the provided predicate and sort descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(predicate: Predicate<TransactionType>? = nil, sortBy: [SortDescriptor<TransactionType>] = [])
```

## Parameters

- `predicate` — The logical condition that determines whether the history includes a specific model in its results. The default value is `nil`.

- `sortBy` — The array of sort descriptors that tell the history how to order its results. The default value is an empty array.

## Discussion

If you don’t specify a predicate, any fetch using this descriptor will return all models of the associated type. If you expect the number of fetched transactions to be high, use [fetchLimit](fetchlimit.md) to limit the number of transactions returned.

## See Also

### Creating a descriptor

- [init(predicate:)](<init(predicate_).md>) — Initializes a new history descriptor with the provided predicate.
