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
doc_path: /documentation/swift/lazyfiltersequence/lazysequenceprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/lazysequenceprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/lazysequenceprotocol-implementations.json'
content_hash: 'sha256:04999c440379ee35'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# LazySequenceProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [elements](elements-swift.property.md) — 与 `self` 相同。
- [lazy](lazy.md)

### 实例方法

- [compactMap(_:)](<compactmap(__)-72vhr.md>) — 返回对该序列映射给定变换所得的非 `nil` 结果。
- [drop(while:)](<drop(while_).md>) — 返回一个惰性序列，跳过开头满足 `predicate` 的元素。
- [flatMap(_:)](<flatmap(__)-5g3dt.md>) — 返回对该序列映射给定变换所得的结果的拼接。
- [flatMap(_:)](<flatmap(__)-5pe4l.md>) — 返回对该序列映射给定变换所得的非 `nil` 结果。
- [joined()](<joined()-2q2lq.md>) — 返回一个惰性序列，将此序列中各个子序列的元素拼接起来。
- [map(_:)](<map(__)-9kh6q.md>) — 返回一个基于此 `Sequence` 的 `LazyMapSequence`。结果的元素是惰性计算的，每次读取时通过对基础元素调用 `transform` 函数来得到。
- [prefix(while:)](<prefix(while_).md>) — 返回一个由开头连续满足 `predicate` 的元素组成的惰性序列。

### 类型别名

- [Elements](elements.md) — 一个可以包含与此序列相同元素的 `Sequence`，但类型可能更简单。
