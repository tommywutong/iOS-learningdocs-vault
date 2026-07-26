---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collection/endindex
source_url: 'https://developer.apple.com/documentation/swift/collection/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/endindex.json'
content_hash: 'sha256:ca9062558bc436c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# endIndex

<sub>Instance Property</sub>

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: Self.Index { get }
```

## Discussion

When you need a range that includes the last element of a collection, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```swift
let numbers = [10, 20, 30, 40, 50]
if let index = numbers.firstIndex(of: 30) {
    print(numbers[index ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the collection is empty, `endIndex` is equal to `startIndex`.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty collection.
- [indices](indices-9kkbf.md) — The indices that are valid for subscripting the collection, in ascending order.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_)-393pr.md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_)-6jwra.md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
