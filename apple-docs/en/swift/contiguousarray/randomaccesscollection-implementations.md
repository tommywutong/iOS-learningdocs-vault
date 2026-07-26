---
title: RandomAccessCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/contiguousarray/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/randomaccesscollection-implementations.json'
content_hash: 'sha256:87918f96d4f78833'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md) · [ContiguousArray](../contiguousarray.md)

# RandomAccessCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](startindex.md) — The position of the first element in a nonempty array.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.

### Subscripts

- [subscript(_:)](<subscript(__)-41wt7.md>) — Accesses a contiguous subrange of the array’s elements.
- [subscript(_:)](<subscript(__)-899p6.md>) — Accesses the element at the specified position.

### Type Aliases

- [Index](index.md) — The index type for arrays, `Int`.
- [Indices](indices.md) — The type that represents the indices that are valid for subscripting an array, in ascending order.
