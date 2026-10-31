---
title: BidirectionalCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations.json'
content_hash: 'sha256:83b874b2fc72bfd4'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# BidirectionalCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 集合的「越过末尾」位置——即比最后一个有效下标实参大 1 的位置。
- [last](last.md) — 集合的最后一个元素。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。

### 实例方法

- [difference(from:)](<difference(from_).md>) — 返回从给定集合生成此集合有序元素所需的差异。
- [difference(from:by:)](<difference(from_by_).md>) — 返回从给定集合生成此集合有序元素所需的差异，并使用给定的谓词作为等价性测试。
- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [formIndex(after:)](<formindex(after_).md>) — 用其后继位置替换给定的索引。
- [formIndex(before:)](<formindex(before_).md>) — 用其前驱位置替换给定的索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回紧随给定索引之后的位置。
- [index(before:)](<index(before_).md>) — 返回紧邻给定索引之前的位置。
- [joined(separator:)](<joined(separator_)-6ag5z.md>) — 通过连接序列中的元素并在每个元素之间添加给定的分隔符，返回一个新字符串。
- [last(where:)](<last(where_).md>) — 返回序列中满足给定谓词的最后一个元素。
- [lastIndex(of:)](<lastindex(of_).md>) — 返回指定值在集合中出现的最后一个索引。
- [lastIndex(where:)](<lastindex(where_).md>) — 返回集合中匹配给定谓词的最后一个元素的索引。
- [popLast()](<poplast().md>) — 移除并返回集合的最后一个元素。
- [removeLast()](<removelast().md>) — 移除并返回集合的最后一个元素。
- [removeLast(_:)](<removelast(__).md>) — 从集合末尾移除给定数量的元素。
- [reversed()](<reversed().md>) — 返回一个以相反顺序呈现集合元素的视图。

### 下标

- [subscript(_:)](<subscript(__)-95c1r.md>) — 访问 `position` 所指示的元素。
- [subscript(_:)](<subscript(__)-9b37e.md>) — 访问集合元素的一个连续子范围。
