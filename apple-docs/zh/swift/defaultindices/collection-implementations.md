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
doc_path: /documentation/swift/defaultindices/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/defaultindices/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/defaultindices/collection-implementations.json'
content_hash: 'sha256:cb89565c0ebcbb8f'
translated: true
---

> 导航：[技术](<../../technologies.md>) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [DefaultIndices](../defaultindices.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [count](count.md) — 集合中的元素数量。
- [endIndex](endindex.md) — 集合的“末尾之后”位置，即最后一个有效下标参数的下一个位置。
- [first](first.md) — 集合的第一个元素。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。
- [underestimatedCount](underestimatedcount.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [drop(while:)](<drop(while_).md>) — 在 `predicate` 返回 `true` 时跳过元素，并返回剩余元素，从而返回一个子序列。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个子序列，其中包含除给定数量的初始元素之外的所有元素。
- [dropLast(_:)](<droplast(__).md>) — 返回一个子序列，其中包含除指定数量的末尾元素之外的所有元素。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回指定值在集合中首次出现的索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中满足给定谓词（predicate）的第一个元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 将给定索引替换为其后继索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回给定索引之后紧邻的位置。
- [index(of:)](<index(of_).md>) — 返回指定值在集合中首次出现的索引。
- [indices(of:)](<indices(of_).md>) — 返回与给定元素相等的所有元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回与给定谓词匹配的所有元素的索引。
- [makeIterator()](<makeiterator().md>) — 返回一个遍历集合元素的迭代器。
- [map(_:)](<map(__)-5p6p7.md>) — 返回一个数组，其中包含将给定闭包（closure）映射到序列元素上的结果。
- [popFirst()](<popfirst().md>) — 移除并返回集合的第一个元素。
- [prefix(_:)](<prefix(__).md>) — 返回一个子序列，包含集合开头的元素，最多为指定的最大长度。
- [prefix(through:)](<prefix(through_).md>) — 返回一个子序列，从集合开头到指定位置（含）。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个子序列，从集合开头到指定位置（不含）。
- [prefix(while:)](<prefix(while_).md>) — 返回一个子序列，包含初始元素，直到 `predicate` 返回 `false`，并跳过剩余元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 使用给定的生成器作为随机源，返回集合中的一个随机元素。
- [removeFirst()](<removefirst().md>) — 移除并返回集合的第一个元素。
- [removeFirst(_:)](<removefirst(__).md>) — 从集合开头移除指定数量的元素。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回此集合中由给定范围集表示的元素以外的元素所组成的一个集合。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合的最长子序列，这些子序列不包含满足给定谓词的元素。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — 按顺序返回集合中围绕与给定元素相等的元素的最长子序列。
- [suffix(_:)](<suffix(__).md>) — 返回一个子序列，包含集合末尾的元素，最多为给定的最大长度。
- [suffix(from:)](<suffix(from_).md>) — 返回一个子序列，从指定位置到集合末尾。

### 下标

- [subscript(_:)](<subscript(__)-1grsk.md>) — 访问指定位置的元素。
- [subscript(_:)](<subscript(__)-392od.md>) — 访问此集合的一个视图，该视图包含给定索引处的元素。
- [subscript(_:)](<subscript(__)-4ala2.md>)
- [subscript(_:)](<subscript(__)-4h7sp.md>) — 访问由范围表达式指定的集合元素连续子范围。
- [subscript(_:)](<subscript(__)-8o3ct.md>) — 访问集合元素的一个连续子范围。

### 类型别名

- [Index](index.md) — 表示集合中位置的类型。
- [Indices](indices-swift.typealias.md) — 表示可用于对集合进行下标操作的有效索引的类型，按升序排列。
- [Iterator](iterator.md) — 提供集合迭代接口并封装其迭代状态的类型。
- [SubSequence](subsequence.md) — 一个集合，表示此集合元素的连续子范围。该子序列与原始集合共享索引。
