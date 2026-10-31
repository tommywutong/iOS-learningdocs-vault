---
title: 集合实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/closedrange/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/closedrange/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/collection-implementations.json'
content_hash: 'sha256:8249dbe9e868a521'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [ClosedRange](../closedrange.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 该区间的“越过末尾”位置——即比最后一个有效下标参数大 1 的位置。
- [isEmpty](isempty.md) — 一个布尔值，指示该区间是否不包含任何元素。
- [startIndex](startindex.md) — 该区间中第一个元素的位置。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回与给定索引相距指定距离的索引。
- [index(after:)](<index(after_).md>) — 返回紧邻给定索引之后的位置。

### 下标

- [subscript(_:)](<subscript(__)-60m0l.md>) — 访问指定位置上的元素。
- [subscript(_:)](<subscript(__)-vph6.md>) — 访问集合元素的连续子范围。

### 类型别名

- [Indices](indices.md) — 一种类型，表示可用于对集合进行下标操作的有效索引，按升序排列。
- [SubSequence](subsequence.md) — 一个表示此集合元素连续子范围的集合。该子序列与原集合共享索引。

### 枚举

- [Index](index.md) — 一种表示集合中位置的类型。
