---
title: BidirectionalCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations.json'
content_hash: 'sha256:cff27d6688afc273'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# BidirectionalCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 「越过末尾」位置——即比最后一个有效下标实参大 1 的位置。
- [last](last.md) — 集合的最后一个元素。
- [startIndex](startindex.md) — 如果字符串非空，则为第一个 Unicode 标量值的位置。

### 实例方法

- [difference(from:)](<difference(from_).md>) — 返回从给定集合生成此集合有序元素所需的差异。
- [difference(from:by:)](<difference(from_by_).md>) — 返回从给定集合生成此集合有序元素所需的差异，并使用给定的谓词作为等价性测试。
- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [dropLast(_:)](<droplast(__).md>) — 返回一个子序列，包含除末尾指定数量元素之外的所有元素。
- [formIndex(before:)](<formindex(before_).md>) — 用其前驱位置替换给定的索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回 `i` 之后的下一个连续位置。
- [index(before:)](<index(before_).md>) — 返回 `i` 之前的上一个连续位置。
- [last(where:)](<last(where_).md>) — 返回序列中满足给定谓词的最后一个元素。
- [lastIndex(of:)](<lastindex(of_).md>) — 返回指定值在集合中出现的最后一个索引。
- [lastIndex(where:)](<lastindex(where_).md>) — 返回集合中匹配给定谓词的最后一个元素的索引。
- [reversed()](<reversed().md>) — 返回一个以相反顺序呈现集合元素的视图。
- [suffix(_:)](<suffix(__).md>) — 返回一个子序列，包含集合末尾的元素，长度不超过给定的最大长度。

### 下标

- [subscript(_:)](<subscript(__)-2op53.md>) — 访问给定位置上的 Unicode 标量值。
- [subscript(_:)](<subscript(__)-6aml8.md>) — 访问集合元素的一个连续子范围。
