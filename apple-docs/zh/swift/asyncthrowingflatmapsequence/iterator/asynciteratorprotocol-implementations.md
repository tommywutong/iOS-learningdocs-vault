---
title: AsyncIteratorProtocol 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingflatmapsequence/iterator/asynciteratorprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingflatmapsequence/iterator/asynciteratorprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingflatmapsequence/iterator/asynciteratorprotocol-implementations.json'
content_hash: 'sha256:620bb6f43fd3e600'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [Swift Standard Library](../../swift-standard-library.md) · [并发](../../concurrency.md) · [AsyncSequence](../../asyncsequence.md) · [AsyncThrowingFlatMapSequence](../../asyncthrowingflatmapsequence.md) · [Iterator](../iterator.md)

# AsyncIteratorProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [next()](<next()-9sxa4.md>) — `next()` 的默认实现是通过 `next(isolation:)` 定义的，以保持与现有异步迭代器的向后兼容性。
- [next(isolation:)](<next(isolation_)-1y6ga.md>) — `next(isolation:)` 的默认实现是通过 `next()` 定义的，以保持与现有异步迭代器的向后兼容性。
