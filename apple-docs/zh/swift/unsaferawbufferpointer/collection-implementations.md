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
doc_path: /documentation/swift/unsaferawbufferpointer/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/collection-implementations.json'
content_hash: 'sha256:a8657ac11e8f6e96'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [count](count.md) — 缓冲区中的字节数。
- [endIndex](endindex.md) — “末尾之后”位置，即最后一个有效下标参数的下一个位置。
- [first](first.md) — 集合的第一个元素。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [startIndex](startindex.md) — 恒为零，即非空缓冲区中第一个字节的索引。
- [underestimatedCount](underestimatedcount.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [drop(while:)](<drop(while_).md>) — 在 `predicate` 返回 `true` 时跳过元素，并返回剩余元素，从而返回一个子序列。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个子序列，其中包含除给定数量的初始元素之外的所有元素。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回指定值在集合中首次出现的索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中满足给定谓词（predicate）的第一个元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 将给定索引替换为其后继索引。
- [index(of:)](<index(of_).md>) — 返回指定值在集合中首次出现的索引。
- [indices(of:)](<indices(of_).md>) — 返回与给定元素相等的所有元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回与给定谓词匹配的所有元素的索引。
- [map(_:)](<map(__)-5p6ph.md>) — 返回一个数组，其中包含将给定闭包（closure）映射到序列元素上的结果。
- [prefix(_:)](<prefix(__).md>) — 返回一个子序列，包含集合开头的元素，最多为指定的最大长度。
- [prefix(through:)](<prefix(through_).md>) — 返回一个子序列，从集合开头到指定位置（含）。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个子序列，从集合开头到指定位置（不含）。
- [prefix(while:)](<prefix(while_).md>) — 返回一个子序列，包含初始元素，直到 `predicate` 返回 `false`，并跳过剩余元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 使用给定的生成器作为随机源，返回集合中的一个随机元素。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回此集合中由给定范围集表示的元素以外的元素所组成的一个集合。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合的最长子序列，这些子序列不包含满足给定谓词的元素。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — 按顺序返回集合中围绕与给定元素相等的元素的最长子序列。
- [suffix(from:)](<suffix(from_).md>) — 返回一个子序列，从指定位置到集合末尾。

### 下标

- [subscript(_:)](<subscript(__)-2nyad.md>) — 访问集合元素的一个连续子范围。
- [subscript(_:)](<subscript(__)-392oj.md>) — 访问此集合的一个视图，该视图包含给定索引处的元素。
- [subscript(_:)](<subscript(__)-4al9g.md>)
- [subscript(_:)](<subscript(__)-4dk2n.md>) — 以 `UInt8` 值的形式访问内存区域中给定偏移量处的字节。
- [subscript(_:)](<subscript(__)-4h7s7.md>) — 访问由范围表达式指定的集合元素连续子范围。
- [subscript(_:)](<subscript(__)-58r3z.md>) — 访问指定内存区域中的字节。

### 类型别名

- [Index](index.md) — 表示集合中位置的类型。
- [Indices](indices-swift.typealias.md) — 表示可用于对集合进行下标操作的有效索引的类型，按升序排列。
- [SubSequence](subsequence.md) — 一个集合，表示此集合元素的连续子范围。该子序列与原始集合共享索引。
