---
title: indices
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/values-swift.struct/indices-swift.property
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/indices-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct/indices-swift.property.json'
content_hash: 'sha256:9e0baf735600c98e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Values](../values-swift.struct.md)

# indices

<sub>Instance Property</sub>

The indices that are valid for subscripting the collection, in ascending order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var indices: DefaultIndices<Self> { get }
```

## Discussion

A collection’s `indices` property can hold a strong reference to the collection itself, causing the collection to be non-uniquely referenced. If you mutate the collection while iterating over its indices, a strong reference can cause an unexpected copy of the collection. To avoid the unexpected copy, use the `index(after:)` method starting with `startIndex` to produce indices instead.

```swift
var c = MyFancyCollection([10, 20, 30, 40, 50])
var i = c.startIndex
while i != c.endIndex {
    c[i] /= 5
    i = c.index(after: i)
}
// c == MyFancyCollection([2, 4, 6, 8, 10])
```
