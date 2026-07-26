---
title: 'formIndex(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/formindex(after:)'
source_url: 'https://developer.apple.com/documentation/swift/array/formindex(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/formindex%28after%3A%29.json'
content_hash: 'sha256:94d0a2ed2ee10f0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# formIndex(after:)

<sub>Instance Method</sub>

Replaces the given index with its successor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(after i: inout Int)
```

## Parameters

- `i` — A valid index of the collection. `i` must be less than `endIndex`.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty array.
- [endIndex](endindex.md) — The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
