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
doc_path: /documentation/swift/unicode/scalar/utf8view/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf8view/collection-implementations.json'
content_hash: 'sha256:f2645deb142608f5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Swift Standard Library](../../../swift-standard-library.md) · [Strings and Text](../../../strings-and-text.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF8View](../utf8view.md)

# Collection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [count](count.md) — The number of elements in the collection.
- [first](first.md) — The first element of the collection.
- [isEmpty](isempty.md) — A Boolean value indicating whether the collection is empty.
- [underestimatedCount](underestimatedcount.md) — A value less than or equal to the number of elements in the collection.

### Instance Methods

- [drop(while:)](<drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [firstIndex(of:)](<firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [index(of:)](<index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [indices(of:)](<indices(of_).md>) — Returns the indices of all the elements that are equal to the given element.
- [indices(where:)](<indices(where_).md>) — Returns the indices of all the elements that match the given predicate.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of the collection.
- [map(_:)](<map(__)-26p1x.md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [prefix(_:)](<prefix(__).md>) — Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](<prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
- [removingSubranges(_:)](<removingsubranges(__).md>) — Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](<subscript(__)-4krnk.md>) — Accesses a contiguous subrange of the collection’s elements.

### Type Aliases

- [Index](index.md) — A type that represents a position in the collection.
- [Indices](indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Iterator](iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [SubSequence](subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
