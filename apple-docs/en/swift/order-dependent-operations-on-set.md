---
title: Order Dependent Operations on Set
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/order-dependent-operations-on-set
source_url: 'https://developer.apple.com/documentation/swift/order-dependent-operations-on-set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/order-dependent-operations-on-set.json'
content_hash: 'sha256:ea864ecc27ebe990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Collections](collections.md) · [Set](set.md)

# Order Dependent Operations on Set

<sub>API Collection</sub>

Perform order-dependent operations common to all collections, as implemented for `Set`.

## Topics

### Manipulating Indices

- [startIndex](set/startindex.md) — The starting position for iterating members of the set.
- [endIndex](set/endindex.md) — The “past the end” position for the set—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<set/index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<set/formindex(after_).md>) — Replaces the given index with its successor.
- [index(_:offsetBy:)](<set/index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](<set/formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [index(_:offsetBy:limitedBy:)](<set/index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:limitedBy:)](<set/formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<set/distance(from_to_).md>) — Returns the distance between two indices.
- [indices](set/indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.

### Comparing Sets

- [elementsEqual(_:)](<set/elementsequal(__).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](<set/elementsequal(__by_).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:)](<set/lexicographicallyprecedes(__).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](<set/lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [starts(with:)](<set/starts(with_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](<set/starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.

### Selecting Elements

- [subscript(_:)](<set/subscript(__).md>) — Accesses the member at the given position.
- [prefix(_:)](<set/prefix(__).md>) — Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(upTo:)](<set/prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(through:)](<set/prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(while:)](<set/prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](<set/suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](<set/suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Excluding Elements

- [drop(while:)](<set/drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](<set/dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [dropLast(_:)](<set/droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [popFirst()](<set/popfirst().md>) — Removes and returns the first element of the set.

### Reversing a Set’s Elements

- [reversed()](<set/reversed().md>) — Returns an array containing the elements of this sequence in reverse order.

### Splitting and Joining Elements

- [joined()](<set/joined().md>) — Returns the elements of this sequence of sequences, concatenated.
- [joined(separator:)](<set/joined(separator_)-7ubey.md>) — Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [joined(separator:)](<set/joined(separator_)-1cko4.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<set/split(separator_maxsplits_omittingemptysubsequences_).md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<set/split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
