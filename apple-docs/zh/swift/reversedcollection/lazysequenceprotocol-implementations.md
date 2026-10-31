---
title: LazySequenceProtocol 实现
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
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [ReversedCollection](../reversedcollection.md)

# LazySequenceProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [elements](elements-swift.property.md) — 与 `self` 相同。

### 实例方法

- [compactMap(_:)](<compactmap(__)-45kvo.md>) — 返回将给定转换映射到此序列后得到的非 `nil` 结果。
- [filter(_:)](<filter(__)-4t9rn.md>) — 返回 `self` 中满足 `isIncluded` 的元素。
- [flatMap(_:)](<flatmap(__)-4wxgx.md>) — 返回将给定转换映射到此序列后得到的连接结果。
- [flatMap(_:)](<flatmap(__)-81zng.md>) — 返回将给定转换映射到此序列后得到的非 `nil` 结果。
- [joined()](<joined()-2x3z5.md>) — 返回一个惰性序列，连接此序列的序列中的元素。
- [map(_:)](<map(__)-88nu3.md>) — 返回此 `Sequence` 上的一个 `LazyMapSequence`。结果的元素是惰性计算的，每次读取时都会对基础元素调用 `transform` 函数来得出。

### 类型别名

- [Elements](elements.md) — 一个 `Sequence`，可以包含与此序列相同的元素，类型可能更简单。
