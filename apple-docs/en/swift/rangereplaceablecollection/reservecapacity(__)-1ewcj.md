---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/reservecapacity(_:)-1ewcj'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/reservecapacity(_:)-1ewcj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/reservecapacity%28_%3A%29-1ewcj.json'
content_hash: 'sha256:b8d811bde53559b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ n: Int)
```

## Parameters

- `n` — The requested number of elements to store.

## Discussion

If you will be adding a known number of elements to a collection, use this method to avoid multiple reallocations. A type that conforms to `RangeReplaceableCollection` can choose how to respond when this method is called. Depending on the type, it may make sense to allocate more or less storage than requested or to take no action at all.
