---
title: indices
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/words-swift.struct/indices-swift.property
source_url: 'https://developer.apple.com/documentation/swift/uint128/words-swift.struct/indices-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/words-swift.struct/indices-swift.property.json'
content_hash: 'sha256:d69fee4fde9c194b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt128](../../uint128.md) · [Words](../words-swift.struct.md)

# indices

<sub>Instance Property</sub>

The indices that are valid for subscripting the collection, in ascending order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var indices: UInt128.Words.Indices { get }
```

## Discussion

A collection’s `indices` property can hold a strong reference to the collection itself, causing the collection to be nonuniquely referenced. If you mutate the collection while iterating over its indices, a strong reference can result in an unexpected copy of the collection. To avoid the unexpected copy, use the `index(after:)` method starting with `startIndex` to produce indices instead.

```swift
var c = MyFancyCollection([10, 20, 30, 40, 50])
var i = c.startIndex
while i != c.endIndex {
    c[i] /= 5
    i = c.index(after: i)
}
// c == MyFancyCollection([2, 4, 6, 8, 10])
```
