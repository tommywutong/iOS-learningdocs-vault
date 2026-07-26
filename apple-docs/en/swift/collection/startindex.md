---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collection/startindex
source_url: 'https://developer.apple.com/documentation/swift/collection/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/startindex.json'
content_hash: 'sha256:4364dd795fb6513a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: Self.Index { get }
```

## Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

## See Also

### Manipulating Indices

- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-9kkbf.md) — The indices that are valid for subscripting the collection, in ascending order.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_)-393pr.md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_)-6jwra.md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
