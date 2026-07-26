---
title: 'formIndex(_:offsetBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/formindex(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/swift/string/formindex(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/formindex%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:9a8b67ea41c5a43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# formIndex(_:offsetBy:)

<sub>Instance Method</sub>

Offsets the given index by the specified distance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int)
```

## Parameters

- `i` — A valid index of the collection.

- `distance` — The distance to offset `i`. `distance` must not be negative unless the collection conforms to the `BidirectionalCollection` protocol.

## Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the absolute value of `distance`.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first character in a nonempty string.
- [endIndex](endindex.md) — A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
