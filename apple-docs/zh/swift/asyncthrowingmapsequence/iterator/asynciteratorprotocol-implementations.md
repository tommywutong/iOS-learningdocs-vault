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
doc_path: /documentation/swift/asyncthrowingmapsequence/iterator/asynciteratorprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/iterator/asynciteratorprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingmapsequence/iterator/asynciteratorprotocol-implementations.json'
content_hash: 'sha256:1214d710773be395'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [Swift Standard Library](../../swift-standard-library.md) · [并发](../../concurrency.md) · [AsyncSequence](../../asyncsequence.md) · [AsyncThrowingMapSequence](../../asyncthrowingmapsequence.md) · [Iterator](../iterator.md)

# AsyncIteratorProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [next()](<next()-7a2r8.md>) — `next()` 的默认实现，其内部基于 `next(isolation:)`，这是为保持与现有异步迭代器的向后兼容性所必需的。
- [next(isolation:)](<next(isolation_)-82aes.md>) — `next(isolation:)` 的默认实现，其内部基于 `next()`，这是为保持与现有异步迭代器的向后兼容性所必需的。
