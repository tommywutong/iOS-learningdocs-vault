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
doc_path: /documentation/swift/unsafemutablebufferpointer/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/collection-implementations.json'
content_hash: 'sha256:afbd075c103a6eb7'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [endIndex](endindex.md) — 该缓冲区末尾之后的位置——即比最后一个有效下标参数大 1 的位置。
- [first](first.md) — 集合的第一个元素。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [isEmpty](isempty.md) — 一个布尔值，指示缓冲区是否为空。
- [startIndex](startindex.md) — 非空缓冲区中第一个元素的索引。
- [underestimatedCount](underestimatedcount-4ggr6.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [drop(while:)](<drop(while_)-37wq1.md>) — 通过跳过 `predicate` 返回 `true` 的元素并返回其余元素，返回一个子序列。
- [dropFirst(_:)](<dropfirst(__)-1ruqu.md>) — 返回一个子序列，包含除开头给定数量元素之外的所有元素。
- [dropLast(_:)](<droplast(__)-6rw2x.md>) — 返回一个子序列，包含除末尾指定数量元素之外的所有元素。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回指定值在集合中首次出现的索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中第一个元素满足给定谓词（predicate）的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定的索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定的索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 用其后继位置替换给定的索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回与给定索引相距指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回与给定索引相距指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回紧随给定索引之后的位置。
- [index(of:)](<index(of_).md>) — 返回指定值在集合中首次出现的索引。
- [indices(of:)](<indices(of_).md>) — 返回所有与给定元素相等的元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回所有匹配给定谓词的元素的索引。
- [map(_:)](<map(__)-5p6og.md>) — 返回一个数组，包含将给定的闭包映射到序列元素后得到的结果。
- [prefix(_:)](<prefix(__)-1n69c.md>) — 返回一个子序列，包含集合开头的元素，长度不超过指定的最大长度。
- [prefix(through:)](<prefix(through_).md>) — 返回一个从集合开头直到（包含）指定位置的子序列。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个从集合开头直到（但不包含）指定位置的子序列。
- [prefix(while:)](<prefix(while_)-3arjm.md>) — 返回一个子序列，包含 `predicate` 返回 `false` 之前的开头元素，并跳过其余元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 返回集合中的一个随机元素，使用给定的生成器作为随机源。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回一个集合，包含此集合中未被给定范围集表示的元素。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_)-4pbql.md>) — 按顺序返回集合中最长的、不包含满足给定谓词的元素的子序列。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-3dgmc.md>) — 按顺序返回集合中最长的、围绕等于给定元素的元素分割得到的子序列。
- [suffix(_:)](<suffix(__)-qdce.md>) — 返回一个子序列，包含集合末尾的元素，长度不超过给定的最大长度。
- [suffix(from:)](<suffix(from_).md>) — 返回一个从指定位置到集合末尾的子序列。

### 下标

- [subscript(_:)](<subscript(__)-13u1d.md>) — 访问缓冲区元素的连续子范围。
- [subscript(_:)](<subscript(__)-9t9gq.md>) — 访问指定位置的元素。

### 类型别名

- [Index](index.md) — 一种表示集合中位置的类型。
- [Indices](indices-swift.typealias.md) — 一种类型，表示可用于对集合进行下标操作的有效索引，按升序排列。
- [SubSequence](subsequence.md) — 一个表示此集合元素连续子范围的集合。子序列与原集合共享索引。
