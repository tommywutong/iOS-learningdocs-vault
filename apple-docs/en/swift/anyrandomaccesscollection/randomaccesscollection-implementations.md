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
doc_path: /documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations.json'
content_hash: 'sha256:646418f613cf1682'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# RandomAccessCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [startIndex](startindex.md) — The position of the first element in a non-empty collection.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.

### Subscripts

- [subscript(_:)](<subscript(__)-37hui.md>) — Accesses the element indicated by `position`.
- [subscript(_:)](<subscript(__)-6jydx.md>) — Accesses a contiguous subrange of the collection’s elements.
