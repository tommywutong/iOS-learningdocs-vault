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
doc_path: /documentation/swift/slice/lazysequenceprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/slice/lazysequenceprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/lazysequenceprotocol-implementations.json'
content_hash: 'sha256:c96eed2eca130d03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [Slice](../slice.md)

# LazySequenceProtocol Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [elements](elements-swift.property.md) — Identical to `self`.

### Instance Methods

- [compactMap(_:)](<compactmap(__)-188bn.md>) — Returns the non-`nil` results of mapping the given transformation over this sequence.
- [filter(_:)](<filter(__)-7stzr.md>) — Returns the elements of `self` that satisfy `isIncluded`.
- [flatMap(_:)](<flatmap(__)-1q7p9.md>) — Returns the concatenated results of mapping the given transformation over this sequence.
- [flatMap(_:)](<flatmap(__)-6ng42.md>) — Returns the non-`nil` results of mapping the given transformation over this sequence.
- [joined()](<joined()-3bqi4.md>) — Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [map(_:)](<map(__)-87fp1.md>) — Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.

### Type Aliases

- [Elements](elements.md) — A `Sequence` that can contain the same elements as this one, possibly with a simpler type.
