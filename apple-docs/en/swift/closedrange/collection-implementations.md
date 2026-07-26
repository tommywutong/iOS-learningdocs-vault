---
title: Collection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/closedrange/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/closedrange/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/collection-implementations.json'
content_hash: 'sha256:8249dbe9e868a521'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [ClosedRange](../closedrange.md)

# Collection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The range’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [isEmpty](isempty.md) — A Boolean value indicating whether the range contains no elements.
- [startIndex](startindex.md) — The position of the first element in the range.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.

### Subscripts

- [subscript(_:)](<subscript(__)-60m0l.md>) — Accesses the element at specified position.
- [subscript(_:)](<subscript(__)-vph6.md>) — Accesses a contiguous subrange of the collection’s elements.

### Type Aliases

- [Indices](indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [SubSequence](subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

### Enumerations

- [Index](index.md) — A type that represents a position in the collection.
