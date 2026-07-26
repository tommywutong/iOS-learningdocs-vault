---
title: EnumeratedSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/enumeratedsequence
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence.json'
content_hash: 'sha256:855a3b04a5b68d03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# EnumeratedSequence

<sub>Structure</sub>

An enumeration of the elements of a sequence or collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct EnumeratedSequence<Base> where Base : Sequence
```

## Overview

`EnumeratedSequence` is a sequence of pairs (_n_, _x_), where _n_s are consecutive `Int` values starting at zero, and _x_s are the elements of a base sequence.

To create an instance of `EnumeratedSequence`, call `enumerated()` on a sequence or collection. The following example enumerates the elements of an array.

```swift
var s = ["foo", "bar"].enumerated()
for (n, x) in s {
    print("\(n): \(x)")
}
// Prints "0: foo"
// Prints "1: bar"
```

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [RandomAccessCollection](randomaccesscollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Default Implementations

- [BidirectionalCollection Implementations](enumeratedsequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](enumeratedsequence/collection-implementations.md)
- [RandomAccessCollection Implementations](enumeratedsequence/randomaccesscollection-implementations.md)
- [Sequence Implementations](enumeratedsequence/sequence-implementations.md)

## See Also

### Wrappers for Algorithms

- [CollectionDifference](collectiondifference.md) — A collection of insertions and removals that describe the difference between two ordered collection states.
- [DropFirstSequence](dropfirstsequence.md) — A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [DropWhileSequence](dropwhilesequence.md) — A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [FlattenCollection](flattencollection.md)
- [FlattenSequence](flattensequence.md) — A sequence consisting of all the elements contained in each segment contained in some `Base` sequence.
- [JoinedSequence](joinedsequence.md) — A sequence that presents the elements of a base sequence of sequences concatenated using a given separator.
- [PrefixSequence](prefixsequence.md) — A sequence that only consumes up to `n` elements from an underlying `Base` iterator.
- [Repeated](repeated.md) — A collection whose elements are all identical.
- [ReversedCollection](reversedcollection.md) — A collection that presents the elements of its base collection in reverse order.
- [StrideTo](strideto.md) — A sequence of values formed by striding over a half-open interval.
- [StrideThrough](stridethrough.md) — A sequence of values formed by striding over a closed interval.
- [UnfoldSequence](unfoldsequence.md) — A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [Zip2Sequence](zip2sequence.md) — A sequence of pairs built out of two underlying sequences.
