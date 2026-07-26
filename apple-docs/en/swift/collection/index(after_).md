---
title: 'index(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/index(after:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/index(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/index%28after%3A%29.json'
content_hash: 'sha256:14834ba78c5077d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# index(after:)

<sub>Instance Method</sub>

Returns the position immediately after the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(after i: Self.Index) -> Self.Index
```

## Parameters

- `i` — A valid index of the collection. `i` must be less than `endIndex`.

## Return Value

The index value immediately after `i`.

## Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Default Implementations

### BidirectionalCollection Implementations

- [index(after:)](<../bidirectionalcollection/index(after_)-4zlq6.md>) — Returns the position immediately after the given index.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty collection.
- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-9kkbf.md) — The indices that are valid for subscripting the collection, in ascending order.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_)-393pr.md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_)-6jwra.md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
