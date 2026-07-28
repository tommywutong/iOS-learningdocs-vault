---
title: 集合实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/collection-implementations.json'
content_hash: 'sha256:aee80162abc3b519'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Iterator](iterator.md) — 一种类型，提供集合的迭代接口并封装其迭代状态。

### 实例属性

- [count](count.md) — 集合中的元素数量。
- [first](first.md) — 集合的第一个元素。
- [indices](indices-swift.property.md) — 可用于通过下标访问集合的有效索引，按升序排列。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [underestimatedCount](underestimatedcount.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [drop(while:)](<drop(while_).md>) — 返回一个子序列，跳过所有使 `predicate` 返回 `true` 的元素，并返回剩余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个子序列，包含除指定数量初始元素外的所有元素。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回集合中指定值首次出现的索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中第一个满足给定谓词（predicate）的元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 将给定索引替换为其后继索引。
- [index(of:)](<index(of_).md>) — 返回集合中指定值首次出现的索引。
- [indices(of:)](<indices(of_).md>) — 返回所有等于给定元素的元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回所有匹配给定谓词（predicate）的元素的索引。
- [makeIterator()](<makeiterator().md>) — 返回集合元素上的一个迭代器。
- [map(_:)](<map(__)-56zez.md>) — 返回一个数组，包含将给定闭包（closure）映射到序列各元素的结果。
- [prefix(_:)](<prefix(__).md>) — 返回一个子序列，最多包含指定长度的初始元素。
- [prefix(through:)](<prefix(through_).md>) — 返回从集合开头到指定位置（包含该位置）的子序列。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回从集合开头到指定位置（不包含该位置）的子序列。
- [prefix(while:)](<prefix(while_).md>) — 返回一个子序列，包含初始元素直到 `predicate` 返回 `false`，并跳过剩余元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 返回集合中的一个随机元素，使用给定的生成器作为随机性来源。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回此集合中未被给定范围集（range set）表示的元素组成的集合。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合中最长的、不包含满足给定谓词（predicate）的元素的子序列。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — 按顺序返回集合中最长的子序列，这些子序列由等于给定元素的元素分隔。
- [suffix(from:)](<suffix(from_).md>) — 返回从指定位置到集合末尾的子序列。

### 下标

- [subscript(_:)](<subscript(__)-4i2sy.md>) — 访问由范围表达式指定的集合元素的连续子范围。
- [subscript(_:)](<subscript(__)-gee0.md>) — 访问此集合在给定索引处的元素的一个视图（view）。
- [subscript(_:)](<subscript(__)-qk0r.md>)

### 类型别名

- [Index](index.md) — 一种表示集合中位置的类型。
- [Indices](indices.md) — 一种类型，表示可用于通过下标访问集合的有效索引，按升序排列。
- [SubSequence](subsequence.md) — 一个表示此集合元素连续子范围的集合。子序列与原集合共享索引。
