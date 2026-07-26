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
doc_path: /documentation/swift/unsaferawbufferpointer/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/bidirectionalcollection-implementations.json'
content_hash: 'sha256:451a239b500a2d28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Manual Memory Management](../manual-memory-management.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# BidirectionalCollection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [last](last.md) — The last element of the collection.

### Instance Methods

- [difference(from:)](<difference(from_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](<difference(from_by_).md>) — Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [dropLast(_:)](<droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [last(where:)](<last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [suffix(_:)](<suffix(__).md>) — Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
