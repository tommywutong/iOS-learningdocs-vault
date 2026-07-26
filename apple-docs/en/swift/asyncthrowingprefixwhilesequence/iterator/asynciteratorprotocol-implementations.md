---
title: AsyncIteratorProtocol Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingprefixwhilesequence/iterator/asynciteratorprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence/iterator/asynciteratorprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingprefixwhilesequence/iterator/asynciteratorprotocol-implementations.json'
content_hash: 'sha256:a005f096ac43b500'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Swift Standard Library](../../swift-standard-library.md) · [Concurrency](../../concurrency.md) · [AsyncSequence](../../asyncsequence.md) · [AsyncThrowingPrefixWhileSequence](../../asyncthrowingprefixwhilesequence.md) · [Iterator](../iterator.md)

# AsyncIteratorProtocol Implementations

<sub>API Collection</sub>

## Topics

### Instance Methods

- [next()](<next()-8ijyt.md>) — Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [next(isolation:)](<next(isolation_)-4t5g.md>) — Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.
