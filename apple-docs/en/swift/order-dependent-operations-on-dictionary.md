---
title: Order Dependent Operations on Dictionary
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/order-dependent-operations-on-dictionary
source_url: 'https://developer.apple.com/documentation/swift/order-dependent-operations-on-dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/order-dependent-operations-on-dictionary.json'
content_hash: 'sha256:1c141d92dc956878'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Dictionary](dictionary.md)

# Order Dependent Operations on Dictionary

<sub>API Collection</sub>

Perform order-dependent operations common to all collections, as implemented for `Dictionary`.

## Topics

### Comparing Dictionaries

- [elementsEqual(_:by:)](<dictionary/elementsequal(__by_).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [starts(with:by:)](<dictionary/starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:by:)](<dictionary/lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

### Manipulating Indices

- [startIndex](dictionary/startindex.md) — The position of the first element in a nonempty dictionary.
- [endIndex](dictionary/endindex.md) — The dictionary’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<dictionary/index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<dictionary/formindex(after_).md>) — Replaces the given index with its successor.
- [index(_:offsetBy:)](<dictionary/index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](<dictionary/formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [index(_:offsetBy:limitedBy:)](<dictionary/index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:limitedBy:)](<dictionary/formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<dictionary/distance(from_to_).md>) — Returns the distance between two indices.
- [indices](dictionary/indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.

### Selecting Elements

- [subscript(_:)](<dictionary/subscript(__)-2ny9y.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<dictionary/subscript(__)-4h7sk.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<dictionary/subscript(__)-4al9z.md>)
- [prefix(_:)](<dictionary/prefix(__).md>) — Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](<dictionary/prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<dictionary/prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](<dictionary/prefix(while_).md>) — Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](<dictionary/suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](<dictionary/suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Excluding Elements

- [dropFirst(_:)](<dictionary/dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [drop(while:)](<dictionary/drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropLast(_:)](<dictionary/droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [popFirst()](<dictionary/popfirst().md>) — Removes and returns the first key-value pair of the dictionary if the dictionary isn’t empty.

### Transforming a Dictionary’s Elements

- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<dictionary/split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [reversed()](<dictionary/reversed().md>) — Returns an array containing the elements of this sequence in reverse order.
- [withContiguousStorageIfAvailable(_:)](<dictionary/withcontiguousstorageifavailable(__).md>) — Executes a closure on the sequence’s contiguous storage.
