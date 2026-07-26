---
title: Sequence Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyfiltersequence/iterator/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/iterator/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/iterator/sequence-implementations.json'
content_hash: 'sha256:88d399e89f89013a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Swift Standard Library](../../swift-standard-library.md) · [Collections](../../collections.md) · [Supporting Types](../../supporting-types.md) · [LazyFilterSequence](../../lazyfiltersequence.md) · [Sequence Implementations](../sequence-implementations.md) · [Iterator](../iterator.md)

# Sequence Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [underestimatedCount](underestimatedcount.md) — A value less than or equal to the number of elements in the sequence, calculated nondestructively.

### Instance Methods

- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value indicating whether the sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [count(where:)](<count(where_).md>) — Returns the number of elements in the sequence that satisfy the given predicate.
- [drop(while:)](<drop(while_).md>) — Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [dropFirst(_:)](<dropfirst(__).md>) — Returns a sequence containing all but the given number of initial elements.
- [dropLast(_:)](<droplast(__).md>) — Returns a sequence containing all but the given number of final elements.
- [elementsEqual(_:)](<elementsequal(__).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [filter(_:)](<filter(__).md>) — Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](<flatmap(__)-3dw8i.md>)
- [flatMap(_:)](<flatmap(__)-68zvx.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [joined()](<joined().md>) — Returns the elements of this sequence of sequences, concatenated.
- [joined(separator:)](<joined(separator_)-1jr9q.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [joined(separator:)](<joined(separator_)-4f0oy.md>) — Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this sequence.
- [map(_:)](<map(__).md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in the sequence.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in the sequence.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [prefix(_:)](<prefix(__).md>) — Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [prefix(while:)](<prefix(while_).md>) — Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reversed()](<reversed().md>) — Returns an array containing the elements of this sequence in reverse order.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [starts(with:)](<starts(with_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](<starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — Executes a closure on the sequence’s contiguous storage.

### Type Aliases

- [Iterator](iterator.md) — A type that provides the sequence’s iteration interface and encapsulates its iteration state.
