---
title: 'distance(from:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/distance(from:to:)'
source_url: 'https://developer.apple.com/documentation/swift/string/distance(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/distance%28from%3Ato%3A%29.json'
content_hash: 'sha256:8335befde27ad40a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# distance(from:to:)

<sub>Instance Method</sub>

Returns the distance between two indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from start: String.Index, to end: String.Index) -> Int
```

## Parameters

- `start` — A valid index of the collection.

- `end` — Another valid index of the collection. If `end` is equal to `start`, the result is zero.

## Return Value

The distance between `start` and `end`.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the resulting distance.

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
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
