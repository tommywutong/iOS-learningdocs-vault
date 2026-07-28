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
doc_path: /documentation/swift/asyncdropfirstsequence/iterator/asynciteratorprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncdropfirstsequence/iterator/asynciteratorprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdropfirstsequence/iterator/asynciteratorprotocol-implementations.json'
content_hash: 'sha256:346152ba8cf21ebc'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [Swift 标准库](../../swift-standard-library.md) · [并发](../../concurrency.md) · [AsyncSequence](../../asyncsequence.md) · [AsyncDropFirstSequence](../../asyncdropfirstsequence.md) · [迭代器](../iterator.md)

# AsyncIteratorProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [next()](<next()-9cp7j.md>) — `next()` 的默认实现基于 `next(isolation:)`，这是为了与现有异步迭代器（async iterator）保持向后兼容。
- [next(isolation:)](<next(isolation_)-46dp7.md>) — `next(isolation:)` 的默认实现基于 `next()`，这是为了与现有异步迭代器保持向后兼容。
