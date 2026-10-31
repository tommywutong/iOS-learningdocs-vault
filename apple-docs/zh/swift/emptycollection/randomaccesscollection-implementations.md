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
doc_path: /documentation/swift/emptycollection/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/emptycollection/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/emptycollection/randomaccesscollection-implementations.json'
content_hash: 'sha256:a3aeec64ef176bef'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [EmptyCollection](../emptycollection.md)

# RandomAccessCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 始终为零，与 `startIndex` 相同。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [startIndex](startindex.md) — 始终为零，与 `endIndex` 相同。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 两个索引之间的距离（始终为零）。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 始终触发陷阱。
- [index(before:)](<index(before_).md>) — 始终触发陷阱。

### 下标

- [subscript(_:)](<subscript(__)-1wkfh.md>) — 访问给定位置的元素。
- [subscript(_:)](<subscript(__)-5fxf8.md>) — 访问集合元素的一个连续子范围。

### 类型别名

- [Index](index.md) — 表示集合中有效位置的类型。
