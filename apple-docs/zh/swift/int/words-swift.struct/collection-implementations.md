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
doc_path: /documentation/swift/int/words-swift.struct/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/int/words-swift.struct/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/words-swift.struct/collection-implementations.json'
content_hash: 'sha256:3a767612cfacc1f0'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [Int](../../int.md) · [Words](../words-swift.struct.md)

# 集合实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [first](first.md) — 集合的第一个元素。
- [isEmpty](isempty.md) — 一个布尔值，指示集合是否为空。
- [underestimatedCount](underestimatedcount.md) — 一个小于或等于集合中元素数量的值。

### 实例方法

- [drop(while:)](<drop(while_).md>) — 返回一个子序列，跳过 `predicate` 返回 `true` 的元素，并返回其余的元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个子序列，包含除开头给定数量元素之外的所有元素。
- [firstIndex(of:)](<firstindex(of_).md>) — 返回指定值在集合中出现的第一个索引。
- [firstIndex(where:)](<firstindex(where_).md>) — 返回集合中第一个满足给定谓词的元素的索引。
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — 将给定索引偏移指定的距离。
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — 将给定索引偏移指定的距离，或使其等于给定的限制索引。
- [formIndex(after:)](<formindex(after_).md>) — 用其后继位置替换给定的索引。
- [index(of:)](<index(of_).md>) — 返回指定值在集合中出现的第一个索引。
- [indices(of:)](<indices(of_).md>) — 返回所有与给定元素相等的元素的索引。
- [indices(where:)](<indices(where_).md>) — 返回所有匹配给定谓词的元素的索引。
- [makeIterator()](<makeiterator().md>) — 返回一个遍历集合元素的迭代器。
- [map(_:)](<map(__)-1zq6m.md>) — 返回一个数组，包含将给定的闭包映射到序列元素后得到的结果。
- [prefix(_:)](<prefix(__).md>) — 返回一个子序列，包含集合开头的元素，长度不超过指定的最大长度。
- [prefix(through:)](<prefix(through_).md>) — 返回一个从集合开头直到指定位置（含）的子序列。
- [prefix(upTo:)](<prefix(upto_).md>) — 返回一个从集合开头直到（但不包括）指定位置的子序列。
- [prefix(while:)](<prefix(while_).md>) — 返回一个子序列，包含开头的元素直到 `predicate` 返回 `false`，并跳过其余的元素。
- [randomElement()](<randomelement().md>) — 返回集合中的一个随机元素。
- [randomElement(using:)](<randomelement(using_).md>) — 返回集合中的一个随机元素，使用给定的生成器作为随机源。
- [removingSubranges(_:)](<removingsubranges(__).md>) — 返回一个集合，包含此集合中未被给定范围集所表示的元素。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合中最长的、不包含满足给定谓词的元素的子序列。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — 按顺序返回集合中最长的、围绕等于给定元素的元素分割出的子序列。
- [suffix(from:)](<suffix(from_).md>) — 返回一个子序列，从指定位置到集合末尾。
