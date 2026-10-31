---
title: 集合实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/values-swift.struct/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct/collection-implementations.json'
content_hash: 'sha256:6720aef99b2dfd42'
translated: true
---

> 导航： [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Values](../values-swift.struct.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Iterator](iterator.md) — 一种提供集合迭代接口并封装其迭代状态的类型。

### 实例属性

- [first](first.md) — 集合的第一个元素。
- [indices](indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。
- [underestimatedCount](underestimatedcount.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [distance(from:to:)](<distance(from_to_).md>) — 返回两个索引之间的距离。
- [drop(while:)](<drop(while_).md>) — 返回一个子序列：在 `predicate` 返回 `true` 期间跳过元素，并返回其余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个子序列，其中包含除开头给定数量元素之外的所有元素。
- [dropLast(_:)](<droplast(__).md>) — 返回一个子序列，其中包含除末尾指定数量元素之外的所有元素。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回集合中出现指定值的第一个索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中第一个满足给定谓词的元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的界限索引。
- [index(_:offsetBy:)](<index(__offsetby_).md>) — 返回与给定索引相距指定距离的索引。
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — 返回与给定索引相距指定距离的索引，除非该距离超出了给定的界限索引。
- [index(of:)](<index(of_).md>) — 返回集合中出现指定值的第一个索引。
- [indices(of:)](<indices(of_).md>) — 返回所有等于给定元素的元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回所有匹配给定谓词的元素的索引。
- [makeIterator()](<makeiterator().md>) — 返回一个遍历集合元素的迭代器。
- [map(_:)](<map(__)-8qoco.md>) — 返回一个数组，其中包含对序列元素映射给定闭包所得的结果。
- [prefix(_:)](<prefix(__).md>) — 返回一个最大不超过指定长度的子序列，其中包含集合的开头元素。
- [prefix(through:)](<prefix(through_).md>) — 返回一个从集合开头到指定位置（含）的子序列。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个从集合开头到指定位置（但不包含该位置）的子序列。
- [prefix(while:)](<prefix(while_).md>) — 返回一个子序列，其中包含开头连续的元素，直到 `predicate` 返回 `false` 为止，并跳过其余元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 使用给定的生成器作为随机源，返回集合中的一个随机元素。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回一个集合，其中包含此集合中未被给定范围集合表示的元素。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合中最长可能的子序列，其中不包含满足给定谓词的元素。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-4wty7.md>) — 按顺序返回集合中最长可能的子序列，以等于给定元素的元素作为分隔。
- [suffix(_:)](<suffix(__).md>) — 返回一个最大不超过给定长度的子序列，其中包含集合的末尾元素。
- [suffix(from:)](<suffix(from_).md>) — 返回一个从指定位置到集合末尾的子序列。
