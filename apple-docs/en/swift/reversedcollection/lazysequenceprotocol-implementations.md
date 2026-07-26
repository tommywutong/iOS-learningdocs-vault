---
title: LazySequenceProtocol Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection/lazysequenceprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/lazysequenceprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/lazysequenceprotocol-implementations.json'
content_hash: 'sha256:eb8f57da511b12c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [ReversedCollection](../reversedcollection.md)

# LazySequenceProtocol Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [elements](elements-swift.property.md) — Identical to `self`.

### Instance Methods

- [compactMap(_:)](<compactmap(__)-45kvo.md>) — Returns the non-`nil` results of mapping the given transformation over this sequence.
- [filter(_:)](<filter(__)-4t9rn.md>) — Returns the elements of `self` that satisfy `isIncluded`.
- [flatMap(_:)](<flatmap(__)-4wxgx.md>) — Returns the concatenated results of mapping the given transformation over this sequence.
- [flatMap(_:)](<flatmap(__)-81zng.md>) — Returns the non-`nil` results of mapping the given transformation over this sequence.
- [joined()](<joined()-2x3z5.md>) — Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [map(_:)](<map(__)-88nu3.md>) — Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.

### Type Aliases

- [Elements](elements.md) — A `Sequence` that can contain the same elements as this one, possibly with a simpler type.
