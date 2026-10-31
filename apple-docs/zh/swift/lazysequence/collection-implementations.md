---
title: 集合实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequence/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/collection-implementations.json'
content_hash: 'sha256:348da1ccd77051af'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [LazySequence](../lazysequence.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [count](count.md) — 返回元素的数量。
- [count](count-1cggd.md) — 集合中的元素数量。
- [endIndex](endindex.md) — 集合的“末尾之后”位置，即最后一个有效下标参数的下一个位置。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [isEmpty](isempty-1upms.md) — 一个布尔值，指示集合是否为空。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [distance(from:to:)](<distance(from_to_)-396sb.md>) — 返回两个索引之间的距离。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回指定值在集合中首次出现的索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中满足给定谓词（predicate）的第一个元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 将给定索引替换为其后继索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:)](<index(__offsetby_)-t8sl.md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_)-62vws.md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回给定索引之后紧邻的位置。
- [index(of:)](<index(of_).md>) — 返回指定值在集合中首次出现的索引。
- [indices(of:)](<indices(of_).md>) — 返回与给定元素相等的所有元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回与给定谓词匹配的所有元素的索引。
- [makeIterator()](<makeiterator().md>) — 返回一个遍历集合元素的迭代器。
- [map(_:)](<map(__)-7wx5z.md>) — 返回一个数组，其中包含将给定闭包（closure）映射到序列元素上的结果。
- [prefix(through:)](<prefix(through_).md>) — 返回一个子序列，从集合开头到指定位置（含）。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个子序列，从集合开头到指定位置（不含）。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 使用给定的生成器作为随机源，返回集合中的一个随机元素。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回此集合中由给定范围集表示的元素以外的元素所组成的一个集合。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-ki1c.md>) — 按顺序返回集合中围绕与给定元素相等的元素的最长子序列。
- [suffix(from:)](<suffix(from_).md>) — 返回一个子序列，从指定位置到集合末尾。

### 下标

- [subscript(_:)](<subscript(__).md>) — 访问 `position` 处的元素。
- [subscript(_:)](<subscript(__)-1iwxl.md>) — 访问此集合的一个视图，该视图包含给定索引处的元素。
- [subscript(_:)](<subscript(__)-1rlj.md>)
- [subscript(_:)](<subscript(__)-8iflg.md>) — 访问集合元素的一个连续子范围。
- [subscript(_:)](<subscript(__)-9kt1v.md>) — 访问由范围表达式指定的集合元素连续子范围。

### 类型别名

- [Index](index.md) — 表示集合中有效位置的类型。
- [Indices](indices-swift.typealias.md) — 表示可用于对集合进行下标操作的有效索引的类型，按升序排列。
- [Iterator](iterator.md) — 提供集合迭代接口并封装其迭代状态的类型。
- [SubSequence](subsequence.md) — 一个集合，表示此集合元素的连续子范围。该子序列与原始集合共享索引。
