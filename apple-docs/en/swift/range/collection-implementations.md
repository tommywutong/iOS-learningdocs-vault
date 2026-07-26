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
doc_path: /documentation/swift/range/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/range/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/collection-implementations.json'
content_hash: 'sha256:ca212923b1803364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Range](../range.md)

# Collection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the range, in ascending order.
- [startIndex](startindex.md) — The position of the first element in a nonempty collection.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.

### Subscripts

- [subscript(_:)](<subscript(__)-358vm.md>) — Accesses the subsequence bounded by the given range.
- [subscript(_:)](<subscript(__)-84ykx.md>) — Accesses the element at specified position.

### Type Aliases

- [Index](index.md) — A type that represents a position in the range.
- [Indices](indices-swift.typealias.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [SubSequence](subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
