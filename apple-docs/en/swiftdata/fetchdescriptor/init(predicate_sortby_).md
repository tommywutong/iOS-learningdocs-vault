---
title: 'init(predicate:sortBy:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/fetchdescriptor/init(predicate:sortby:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/init(predicate:sortby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/init%28predicate%3Asortby%3A%29.json'
content_hash: 'sha256:cd81658c41fe0829'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# init(predicate:sortBy:)

<sub>Initializer</sub>

Creates a fetch descriptor with the specified predicate that, optionally, arranges the fetched models in a particular order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(predicate: Predicate<T>? = nil, sortBy: [SortDescriptor<T>] = [])
```

## Parameters

- `predicate` — The logical condition that determines whether the fetch includes a specific model in its results. The default value is `nil`.

- `sortBy` — The array of sort descriptors that tell the fetch how to order its results. The default value is an empty array.

## Discussion

If you don’t specify a predicate, any fetch using this descriptor will return all models of the associated type. If you expect the number of fetched models to be high, use [fetchLimit](fetchlimit.md) and [fetchOffset](fetchoffset.md) to break those results into smaller, more efficient batches.

## See Also

### Creating a fetch descriptor

- [Predicate](../../foundation/predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [SortDescriptor](../../foundation/sortdescriptor.md) — A serializable description of how to sort numerics and strings.
