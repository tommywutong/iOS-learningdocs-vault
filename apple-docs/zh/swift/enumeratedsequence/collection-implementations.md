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
doc_path: /documentation/swift/enumeratedsequence/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/collection-implementations.json'
content_hash: 'sha256:d7c4480702cd2385'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [EnumeratedSequence](../enumeratedsequence.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Index](index.md) — 一种表示集合中位置的类型。

### 实例属性

- [count](count.md) — 集合中的元素数量。
- [count](count-3o2fx.md) — 集合中的元素数量。
- [endIndex](endindex.md) — 该集合末尾之后的位置——即比最后一个有效下标参数大 1 的位置。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [isEmpty](isempty-1yllc.md) — 一个布尔值，指示集合是否为空。
- [startIndex](startindex.md) — 非空集合中第一个元素的位置。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [distance(from:to:)](<distance(from_to_)-6kmqj.md>) — 返回两个索引之间的距离。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中第一个元素满足给定谓词（predicate）的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 将给定索引替换为其后继索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:)](<index(__offsetby_)-4bcg9.md>) — 返回一个距离给定索引指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_)-4rme3.md>) — 返回一个距离给定索引指定距离的索引，除非该距离超出了给定的限制索引。
- [index(after:)](<index(after_).md>) — 返回给定索引之后紧邻的位置。
- [indices(where:)](<indices(where_).md>) — 返回所有匹配给定谓词的元素的索引。
- [map(_:)](<map(__)-9le0.md>) — 返回一个数组，包含将给定的闭包映射到序列元素后得到的结果。
- [prefix(through:)](<prefix(through_).md>) — 返回一个从集合开头直到（包含）指定位置的子序列。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个从集合开头直到（但不包含）指定位置的子序列。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 返回集合中的一个随机元素，使用给定的生成器作为随机源。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回一个集合，包含此集合中未被给定范围集表示的元素。
- [suffix(from:)](<suffix(from_).md>) — 返回一个从指定位置到集合末尾的子序列。

### 下标

- [subscript(_:)](<subscript(__).md>) — 访问指定位置的元素。
- [subscript(_:)](<subscript(__)-5gng6.md>) — 访问集合元素的一个连续子范围。
- [subscript(_:)](subscript(__)-7y5my.md)
- [subscript(_:)](<subscript(__)-8ubal.md>) — 访问由范围表达式指定的集合元素连续子范围。
- [subscript(_:)](<subscript(__)-91gqg.md>) — 访问此集合的一个视图，该视图包含给定索引处的元素。

### 类型别名

- [Indices](indices.md) — 一种类型，表示可用于对集合进行下标操作的有效索引，按升序排列。
- [SubSequence](subsequence.md) — 一个表示此集合元素连续子范围的集合。子序列与原集合共享索引。
