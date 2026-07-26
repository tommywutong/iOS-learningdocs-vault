---
title: Collection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/flattensequence/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/flattensequence/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/flattensequence/collection-implementations.json'
content_hash: 'sha256:ad905fc7f65efbcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [FlattenSequence](../flattensequence.md)

# Collection Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [Index](index.md) — A position in a FlattenCollection

### Instance Properties

- [count](count.md) — The number of elements in the collection.
- [endIndex](endindex.md) — The collection’s “past the end” position.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [isEmpty](isempty.md) — A Boolean value indicating whether the collection is empty.
- [startIndex](startindex.md) — The position of the first element in a non-empty collection.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [distance(from:to:)](<distance(from_to_)-1neyu.md>) — Returns the distance between two indices.
- [firstIndex(of:)](<firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_)-9h4a8.md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_)-5809f.md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [formIndex(after:)](<formindex(after_)-7v0c1.md>) — Replaces the given index with its successor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:)](<index(__offsetby_)-20r2m.md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_)-7gfpk.md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(of:)](<index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [indices(of:)](<indices(of_).md>) — Returns the indices of all the elements that are equal to the given element.
- [indices(where:)](<indices(where_).md>) — Returns the indices of all the elements that match the given predicate.
- [map(_:)](<map(__)-9pfsv.md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
- [removingSubranges(_:)](<removingsubranges(__).md>) — Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-9yjf5.md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](<subscript(__)-1cq56.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-1eq7u.md>) — Accesses the element at `position`.
- [subscript(_:)](<subscript(__)-3w5sk.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-4nz3b.md>) — Accesses a view of this collection with the elements at the given indices.
- [subscript(_:)](<subscript(__)-cutv.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-v1s4.md>)

### Type Aliases

- [Indices](indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [SubSequence](subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
