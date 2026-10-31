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
doc_path: /documentation/swift/lazymapsequence/lazysequenceprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/lazysequenceprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/lazysequenceprotocol-implementations.json'
content_hash: 'sha256:a9e10d26dfbb6be7'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [LazyMapSequence](../lazymapsequence.md)

# LazySequenceProtocol 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [elements](elements-swift.property.md) — 与 `self` 相同。
- [lazy](lazy.md)

### 实例方法

- [compactMap(_:)](<compactmap(__)-9pvcf.md>) — 返回对该序列映射给定变换所得的非 `nil` 结果。
- [drop(while:)](<drop(while_).md>) — 返回一个惰性序列，跳过开头满足 `predicate` 的元素。
- [filter(_:)](<filter(__).md>) — 返回 `self` 中满足 `isIncluded` 的元素。
- [flatMap(_:)](<flatmap(__)-94qg.md>) — 返回对该序列映射给定变换所得的非 `nil` 结果。
- [flatMap(_:)](<flatmap(__)-q9wd.md>) — 返回对该序列映射给定变换所得的结果的拼接。
- [joined()](<joined()-3sfyr.md>) — 返回一个惰性序列，将此序列中各个子序列的元素拼接起来。
- [map(_:)](<map(__)-8mwhr.md>) — 返回一个基于此 `Sequence` 的 `LazyMapSequence`。结果的元素是惰性计算的，每次读取时通过对基础元素调用 `transform` 函数来得到。
- [prefix(while:)](<prefix(while_).md>) — 返回一个由开头连续满足 `predicate` 的元素组成的惰性序列。
