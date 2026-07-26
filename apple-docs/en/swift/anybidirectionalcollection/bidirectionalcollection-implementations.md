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
doc_path: /documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations.json'
content_hash: 'sha256:83b874b2fc72bfd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# BidirectionalCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [last](last.md) — The last element of the collection.
- [startIndex](startindex.md) — The position of the first element in a non-empty collection.

### Instance Methods

- [difference(from:)](<difference(from_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](<difference(from_by_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [joined(separator:)](<joined(separator_)-6ag5z.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [last(where:)](<last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the given number of elements from the end of the collection.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.

### Subscripts

- [subscript(_:)](<subscript(__)-95c1r.md>) — Accesses the element indicated by `position`.
- [subscript(_:)](<subscript(__)-9b37e.md>) — Accesses a contiguous subrange of the collection’s elements.
