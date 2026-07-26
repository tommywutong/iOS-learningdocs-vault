---
title: Sequence and Collection Protocols
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sequence-and-collection-protocols
source_url: 'https://developer.apple.com/documentation/swift/sequence-and-collection-protocols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence-and-collection-protocols.json'
content_hash: 'sha256:010f2e1b35388741'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Collections](collections.md)

# Sequence and Collection Protocols

<sub>API Collection</sub>

Write generic code that works with any collection, or build your own collection types.

## Topics

### First Steps

- [Sequence](sequence.md) — A type that provides sequential, iterated access to its elements.
- [Collection](collection.md) — A sequence whose elements can be traversed multiple times, nondestructively, and accessed by an indexed subscript.

### Collection Traversal

- [BidirectionalCollection](bidirectionalcollection.md) — A collection that supports backward as well as forward traversal.
- [RandomAccessCollection](randomaccesscollection.md) — A collection that supports efficient random-access index traversal.

### Collection Mutability

- [MutableCollection](mutablecollection.md) — A collection that supports subscript assignment.
- [RangeReplaceableCollection](rangereplaceablecollection.md) — A collection that supports replacement of an arbitrary subrange of elements with the elements of another collection.

### Manual Iteration

- [IteratorProtocol](iteratorprotocol.md) — A type that supplies the values of a sequence one at a time.
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md) — A type that provides borrowed access to the values of a borrowing sequence. _(beta)_
- [BorrowingIteratorAdapter](borrowingiteratoradapter.md) _(beta)_
- [BorrowingSequence](borrowingsequence.md) — A type that provides sequential, borrowing access to its elements. _(beta)_

### Algebraic Sets

- [SetAlgebra](setalgebra.md) — A type that provides mathematical set operations.

### Lazy Collections

- [LazySequenceProtocol](lazysequenceprotocol.md) — A sequence on which normally-eager sequence operations are implemented lazily.
- [LazyCollectionProtocol](lazycollectionprotocol.md)

## See Also

### Advanced Collection Topics

- [Supporting Types](supporting-types.md) — Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.
- [Managed Buffers](managed-buffers.md) — Build your own buffer-backed collection types.
