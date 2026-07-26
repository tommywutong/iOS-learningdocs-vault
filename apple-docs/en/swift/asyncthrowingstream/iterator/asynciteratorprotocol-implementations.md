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
doc_path: /documentation/swift/asyncthrowingstream/iterator/asynciteratorprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/iterator/asynciteratorprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/iterator/asynciteratorprotocol-implementations.json'
content_hash: 'sha256:478ff53814db87ba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Swift Standard Library](../../swift-standard-library.md) · [Concurrency](../../concurrency.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Iterator](../iterator.md)

# AsyncIteratorProtocol Implementations

<sub>API Collection</sub>

## Topics

### Instance Methods

- [next()](<next()-2s2hx.md>) — Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [next(isolation:)](<next(isolation_)-3l7jg.md>) — Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.
