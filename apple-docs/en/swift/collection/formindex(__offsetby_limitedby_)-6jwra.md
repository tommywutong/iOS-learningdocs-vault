---
title: 'formIndex(_:offsetBy:limitedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/formindex(_:offsetby:limitedby:)-6jwra'
source_url: 'https://developer.apple.com/documentation/swift/collection/formindex(_:offsetby:limitedby:)-6jwra'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/formindex%28_%3Aoffsetby%3Alimitedby%3A%29-6jwra.json'
content_hash: 'sha256:aefe0e2d968f573a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# formIndex(_:offsetBy:limitedBy:)

<sub>Instance Method</sub>

Offsets the given index by the specified distance, or so that it equals the given limiting index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Bool
```

## Parameters

- `i` — A valid index of the collection.

- `distance` — The distance to offset `i`. `distance` must not be negative unless the collection conforms to the `BidirectionalCollection` protocol.

- `limit` — A valid index of the collection to use as a limit. If `distance > 0`, a limit that is less than `i` has no effect. Likewise, if `distance < 0`, a limit that is greater than `i` has no effect.

## Return Value

`true` if `i` has been offset by exactly `distance` steps without going beyond `limit`; otherwise, `false`. When the return value is `false`, the value of `i` is equal to `limit`.

## Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the absolute value of `distance`.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty collection.
- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-9kkbf.md) — The indices that are valid for subscripting the collection, in ascending order.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_)-393pr.md>) — Offsets the given index by the specified distance.
