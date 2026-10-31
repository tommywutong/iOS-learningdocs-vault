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
doc_path: /documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations.json'
content_hash: 'sha256:646418f613cf1682'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# RandomAccessCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 该集合末尾之后的位置——即比最后一个有效下标参数大 1 的位置。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [formIndex(after:)](<formindex(after_).md>) — 用其后继位置替换给定的索引。
- [formIndex(before:)](<formindex(before_).md>) — 用其前驱位置替换给定的索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回给定索引之后紧邻的位置。
- [index(before:)](<index(before_).md>) — 返回给定索引之前紧邻的位置。

### 下标

- [subscript(_:)](<subscript(__)-37hui.md>) — 访问 `position` 所指示的元素。
- [subscript(_:)](<subscript(__)-6jydx.md>) — 访问集合元素的连续子范围。
