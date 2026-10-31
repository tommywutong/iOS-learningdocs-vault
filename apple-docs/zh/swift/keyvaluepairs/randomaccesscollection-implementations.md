---
title: RandomAccessCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyvaluepairs/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/keyvaluepairs/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyvaluepairs/randomaccesscollection-implementations.json'
content_hash: 'sha256:f61efed4f34ab367'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [KeyValuePairs](../keyvaluepairs.md)

# RandomAccessCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 集合的“越过末尾”位置——即比最后一个有效下标参数大 1 的位置。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回与给定索引相距指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回与给定索引相距指定距离的索引，除非该距离超出了给定的界限索引。
- [index(after:)](<index(after_).md>) — 返回紧邻给定索引之后的位置。
- [index(before:)](<index(before_).md>) — 返回紧邻给定索引之后的位置。

### 下标

- [subscript(_:)](<subscript(__).md>) — 访问指定位置上的元素。

### 类型别名

- [Element](element.md) — `KeyValuePairs` 的元素类型：包含单个键值对的元组。
