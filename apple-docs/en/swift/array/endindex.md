---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/endindex
source_url: 'https://developer.apple.com/documentation/swift/array/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/endindex.json'
content_hash: 'sha256:b36573fa3d9b686b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# endIndex

<sub>Instance Property</sub>

The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: Int { get }
```

## Discussion

When you need a range that includes the last element of an array, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```swift
let numbers = [10, 20, 30, 40, 50]
if let i = numbers.firstIndex(of: 30) {
    print(numbers[i ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the array is empty, `endIndex` is equal to `startIndex`.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty array.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
