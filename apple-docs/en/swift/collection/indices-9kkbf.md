---
title: indices
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collection/indices-9kkbf
source_url: 'https://developer.apple.com/documentation/swift/collection/indices-9kkbf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/indices-9kkbf.json'
content_hash: 'sha256:0d74637301b04964'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# indices

<sub>Instance Property</sub>

The indices that are valid for subscripting the collection, in ascending order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var indices: Self.Indices { get }
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

## Default Implementations

### BidirectionalCollection Implementations

- [indices](../bidirectionalcollection/indices-4jyvu.md) — The indices that are valid for subscripting the collection, in ascending order.

### Collection Implementations

- [indices](indices-wkbb.md) — The indices that are valid for subscripting the collection, in ascending order.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty collection.
- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_)-393pr.md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_)-6jwra.md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
