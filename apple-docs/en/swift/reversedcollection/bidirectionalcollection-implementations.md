---
title: BidirectionalCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/bidirectionalcollection-implementations.json'
content_hash: 'sha256:e4901aeafb5a4d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [ReversedCollection](../reversedcollection.md)

# BidirectionalCollection Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [Index](index.md) — An index that traverses the same positions as an underlying index, with inverted traversal direction.

### Instance Properties

- [last](last.md) — The last element of the collection.

### Instance Methods

- [difference(from:)](<difference(from_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](<difference(from_by_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [dropLast(_:)](<droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [joined(separator:)](<joined(separator_)-3e82c.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [last(where:)](<last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
