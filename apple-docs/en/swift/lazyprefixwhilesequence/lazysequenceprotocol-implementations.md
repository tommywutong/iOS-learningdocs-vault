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
doc_path: /documentation/swift/lazyprefixwhilesequence/lazysequenceprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/lazysequenceprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyprefixwhilesequence/lazysequenceprotocol-implementations.json'
content_hash: 'sha256:eed3b3fd7897b71d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [LazyPrefixWhileSequence](../lazyprefixwhilesequence.md)

# LazySequenceProtocol Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [elements](elements-swift.property.md) — Identical to `self`.
- [lazy](lazy.md)

### Instance Methods

- [compactMap(_:)](<compactmap(__)-2xgdq.md>) — Returns the non-`nil` results of mapping the given transformation over this sequence.
- [drop(while:)](<drop(while_).md>) — Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [filter(_:)](<filter(__).md>) — Returns the elements of `self` that satisfy `isIncluded`.
- [flatMap(_:)](<flatmap(__)-8pzjy.md>) — Returns the non-`nil` results of mapping the given transformation over this sequence.
- [flatMap(_:)](<flatmap(__)-907vo.md>) — Returns the concatenated results of mapping the given transformation over this sequence.
- [joined()](<joined()-h5vc.md>) — Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [map(_:)](<map(__)-24l6d.md>) — Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [prefix(while:)](<prefix(while_).md>) — Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.

### Type Aliases

- [Elements](elements.md) — A `Sequence` that can contain the same elements as this one, possibly with a simpler type.
