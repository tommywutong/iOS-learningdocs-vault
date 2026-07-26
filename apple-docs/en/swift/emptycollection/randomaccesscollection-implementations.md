---
title: RandomAccessCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/emptycollection/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/emptycollection/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/emptycollection/randomaccesscollection-implementations.json'
content_hash: 'sha256:a3aeec64ef176bef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [EmptyCollection](../emptycollection.md)

# RandomAccessCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — Always zero, just like `startIndex`.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](startindex.md) — Always zero, just like `endIndex`.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — The distance between two indexes (always zero).
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Always traps.
- [index(before:)](<index(before_).md>) — Always traps.

### Subscripts

- [subscript(_:)](<subscript(__)-1wkfh.md>) — Accesses the element at the given position.
- [subscript(_:)](<subscript(__)-5fxf8.md>) — Accesses a contiguous subrange of the collection’s elements.

### Type Aliases

- [Index](index.md) — A type that represents a valid position in the collection.
