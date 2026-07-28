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
doc_path: /documentation/swift/asyncthrowingdropwhilesequence/iterator/asynciteratorprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence/iterator/asynciteratorprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingdropwhilesequence/iterator/asynciteratorprotocol-implementations.json'
content_hash: 'sha256:b15d132ce3b45661'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [Swift 标准库](../../swift-standard-library.md) · [并发](../../concurrency.md) · [AsyncSequence](../../asyncsequence.md) · [AsyncThrowingDropWhileSequence](../../asyncthrowingdropwhilesequence.md) · [Iterator](../iterator.md)

# AsyncIteratorProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [next()](<next()-3odrt.md>) — `next()` 的默认实现，基于 `next(isolation:)` 实现，这是保持与现有异步迭代器 (async iterator) 向后兼容所必需的。
- [next(isolation:)](<next(isolation_)-323s.md>) — `next(isolation:)` 的默认实现，基于 `next()` 实现，这是保持与现有异步迭代器向后兼容所必需的。
