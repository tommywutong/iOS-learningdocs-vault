---
title: BidirectionalCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations.json'
content_hash: 'sha256:cff27d6688afc273'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# BidirectionalCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [endIndex](endindex.md) — The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [last](last.md) — The last element of the collection.
- [startIndex](startindex.md) — The position of the first Unicode scalar value if the string is nonempty.

### Instance Methods

- [difference(from:)](<difference(from_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](<difference(from_by_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [dropLast(_:)](<droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the next consecutive location after `i`.
- [index(before:)](<index(before_).md>) — Returns the previous consecutive location before `i`.
- [last(where:)](<last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

### Subscripts

- [subscript(_:)](<subscript(__)-2op53.md>) — Accesses the Unicode scalar value at the given position.
- [subscript(_:)](<subscript(__)-6aml8.md>) — Accesses a contiguous subrange of the collection’s elements.
