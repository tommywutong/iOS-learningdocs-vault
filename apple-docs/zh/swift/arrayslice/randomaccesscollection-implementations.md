---
title: RandomAccessCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/arrayslice/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/randomaccesscollection-implementations.json'
content_hash: 'sha256:1a1f7b6b2dbcc91d'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md) · [ArraySlice](../arrayslice.md)

# RandomAccessCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 该数组末尾之后的位置——即比最后一个有效下标参数大 1 的位置。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [startIndex](startindex.md) — 非空数组中第一个元素的位置。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [formIndex(after:)](<formindex(after_).md>) — 用其后继位置替换给定的索引。
- [formIndex(before:)](<formindex(before_).md>) — 用其前驱位置替换给定的索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回给定索引之后紧邻的位置。
- [index(before:)](<index(before_).md>) — 返回给定索引之前紧邻的位置。

### 下标

- [subscript(_:)](<subscript(__)-4e8d9.md>) — 访问指定位置的元素。
- [subscript(_:)](<subscript(__)-63qca.md>) — 访问数组元素的连续子范围。

### 类型别名

- [Index](index.md) — 数组的索引类型，`Int`。
- [Indices](indices.md) — 表示可用于对数组进行下标操作的有效索引的类型，按升序排列。
