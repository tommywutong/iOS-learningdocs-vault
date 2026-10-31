---
title: BidirectionalCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/bidirectionalcollection-implementations.json'
content_hash: 'sha256:7c7bebc252374370'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# BidirectionalCollection 实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Index](index.md) — 字符串中字符或代码单元的位置。

### 实例属性

- [endIndex](endindex.md) — 字符串的「越过末尾」位置——即比最后一个有效下标实参大 1 的位置。
- [last](last.md) — 集合的最后一个元素。
- [startIndex](startindex.md) — 非空字符串中第一个字符的位置。

### 实例方法

- [difference(from:)](<difference(from_).md>) — 返回从给定集合生成此集合有序元素所需的差异。
- [difference(from:by:)](<difference(from_by_).md>) — 返回从给定集合生成此集合有序元素所需的差异，并使用给定的谓词作为等价性测试。
- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [dropLast(_:)](<droplast(__).md>) — 返回一个子序列，包含除末尾指定数量元素之外的所有元素。
- [formIndex(before:)](<formindex(before_).md>) — 用其前驱位置替换给定的索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回紧随给定索引之后的位置。
- [index(before:)](<index(before_).md>) — 返回紧邻给定索引之前的位置。
- [last(where:)](<last(where_).md>) — 返回序列中满足给定谓词的最后一个元素。
- [lastIndex(of:)](<lastindex(of_).md>) — 返回指定值在集合中出现的最后一个索引。
- [lastIndex(where:)](<lastindex(where_).md>) — 返回集合中匹配给定谓词的最后一个元素的索引。
- [reversed()](<reversed().md>) — 返回一个以相反顺序呈现集合元素的视图。
- [suffix(_:)](<suffix(__).md>) — 返回一个子序列，包含集合末尾的元素，长度不超过给定的最大长度。

### 下标

- [subscript(_:)](<subscript(__)-2so14.md>) — 访问集合元素的一个连续子范围。
- [subscript(_:)](<subscript(__)-lc0v.md>) — 访问给定位置上的字符。
