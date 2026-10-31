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
doc_path: /documentation/swift/anyregexoutput/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/collection-implementations.json'
content_hash: 'sha256:4896e2578d3b3bf3'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Strings and Text](../strings-and-text.md) · [AnyRegexOutput](../anyregexoutput.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [count](count.md) — 集合中元素的数量。
- [count](count-9fygb.md) — 集合中元素的数量。
- [endIndex](endindex.md) — 集合的“越过末尾”位置——即比最后一个有效下标参数大 1 的位置。
- [first](first.md) — 集合的第一个元素。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。
- [underestimatedCount](underestimatedcount.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [drop(while:)](<drop(while_).md>) — 返回一个子序列：在 `predicate` 返回 `true` 期间跳过元素，并返回其余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个子序列，其中包含除开头给定数量元素之外的所有元素。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中第一个满足给定谓词的元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的界限索引。
- [formIndex(after:)](<formindex(after_).md>) — 将给定索引替换为其后继索引。
- [indices(where:)](<indices(where_).md>) — 返回所有匹配给定谓词的元素的索引。
- [makeIterator()](<makeiterator().md>) — 返回一个遍历集合元素的迭代器。
- [map(_:)](<map(__)-1uh24.md>) — 返回一个数组，其中包含对序列元素映射给定闭包所得的结果。
- [prefix(_:)](<prefix(__).md>) — 返回一个最大不超过指定长度的子序列，其中包含集合的开头元素。
- [prefix(through:)](<prefix(through_).md>) — 返回一个从集合开头到指定位置（含）的子序列。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个从集合开头到指定位置（但不包含该位置）的子序列。
- [prefix(while:)](<prefix(while_).md>) — 返回一个子序列，其中包含开头连续的元素，直到 `predicate` 返回 `false` 为止，并跳过其余元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 使用给定的生成器作为随机源，返回集合中的一个随机元素。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回一个集合，其中包含此集合中未被给定范围集合表示的元素。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合中最长可能的子序列，其中不包含满足给定谓词的元素。
- [suffix(from:)](<suffix(from_).md>) — 返回一个从指定位置到集合末尾的子序列。
- [trimmingPrefix(while:)](<trimmingprefix(while_).md>)

### 下标

- [subscript(_:)](<subscript(__)-60hc1.md>) — 访问指定位置上的元素。
- [subscript(_:)](<subscript(__)-smvg.md>) — 访问集合元素的连续子范围。

### 类型别名

- [Index](index.md) — 一种表示集合中位置的类型。
- [Indices](indices.md) — 一种类型，表示可用于对集合进行下标操作的有效索引，按升序排列。
- [Iterator](iterator.md) — 一种提供集合迭代接口并封装其迭代状态的类型。
- [SubSequence](subsequence.md) — 一个表示此集合元素连续子范围的集合。该子序列与原集合共享索引。
