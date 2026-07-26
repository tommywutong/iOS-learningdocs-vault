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
doc_path: /documentation/swift/repeated/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/repeated/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/repeated/randomaccesscollection-implementations.json'
content_hash: 'sha256:a76fc3050a610077'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [Repeated](../repeated.md)

# RandomAccessCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](startindex.md) — The position of the first element in a nonempty collection.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately after the given index.

### Subscripts

- [subscript(_:)](<subscript(__).md>) — Accesses the element at the specified position.

### Type Aliases

- [Index](index.md) — A type that represents a valid position in the collection.
