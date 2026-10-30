---
title: 集合上依赖顺序的操作
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/order-dependent-operations-on-set
source_url: 'https://developer.apple.com/documentation/swift/order-dependent-operations-on-set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/order-dependent-operations-on-set.json'
content_hash: 'sha256:ea864ecc27ebe990'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [集合](collections.md) · [Set](set.md)

# 集合上依赖顺序的操作

<sub>API 集合</sub>

执行所有集合通用的依赖顺序的操作，即 `Set` 所采用的实现。

## 主题

### 操作索引

- [startIndex](set/startindex.md) — 迭代集合成员时的起始位置。
- [endIndex](set/endindex.md) — 该集合末尾之后的位置——即比最后一个有效下标参数大 1 的位置。
- [index(after:)](<set/index(after_).md>) — 返回紧随给定索引之后的位置。
- [formIndex(after:)](<set/formindex(after_).md>) — 用其后继位置替换给定的索引。
- [index(_:offsetBy:)](<set/index(__offsetby_).md>) — 返回与给定索引相距指定距离的索引。
- [formIndex(_:offsetBy:)](<set/formindex(__offsetby_).md>) — 将给定的索引偏移指定的距离。
- [index(_:offsetBy:limitedBy:)](<set/index(__offsetby_limitedby_).md>) — 返回与给定索引相距指定距离的索引，除非该距离超出了给定的限制索引。
- [formIndex(_:offsetBy:limitedBy:)](<set/formindex(__offsetby_limitedby_).md>) — 将给定的索引偏移指定的距离，或使其等于给定的限制索引。
- [distance(from:to:)](<set/distance(from_to_).md>) — 返回两个索引之间的距离。
- [indices](set/indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。

### 比较集合

- [elementsEqual(_:)](<set/elementsequal(__).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含相同的元素。
- [elementsEqual(_:by:)](<set/elementsequal(__by_).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含等价的元素，并使用给定的谓词作为等价性测试。
- [lexicographicallyPrecedes(_:)](<set/lexicographicallyprecedes(__).md>) — 返回一个布尔值，指示序列在字典（lexicographical）排序中是否先于另一个序列，并使用小于运算符（`<`）比较元素。
- [lexicographicallyPrecedes(_:by:)](<set/lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示序列是否在字典排序中先于另一个序列，并使用给定的谓词比较元素。
- [starts(with:)](<set/starts(with_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素相同。
- [starts(with:by:)](<set/starts(with_by_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素等价，并使用给定的谓词作为等价性测试。

### 选择元素

- [subscript(_:)](<set/subscript(__).md>) — 访问给定位置处的成员。
- [prefix(_:)](<set/prefix(__).md>) — 返回一个子序列，包含集合开头的元素，长度不超过指定的最大长度。
- [prefix(upTo:)](<set/prefix(upto_).md>) — 返回一个从集合开头直到（但不包含）指定位置的子序列。
- [prefix(through:)](<set/prefix(through_).md>) — 返回一个从集合开头直到（包含）指定位置的子序列。
- [prefix(while:)](<set/prefix(while_).md>) — 返回一个子序列，包含 `predicate` 返回 `false` 之前的开头元素，并跳过其余元素。
- [suffix(_:)](<set/suffix(__).md>) — 返回一个子序列，包含集合末尾的元素，长度不超过给定的最大长度。
- [suffix(from:)](<set/suffix(from_).md>) — 返回一个从指定位置到集合末尾的子序列。

### 排除元素

- [drop(while:)](<set/drop(while_).md>) — 通过跳过 `predicate` 返回 `true` 的元素并返回其余元素，返回一个子序列。
- [dropFirst(_:)](<set/dropfirst(__).md>) — 返回一个子序列，包含除开头给定数量元素之外的所有元素。
- [dropLast(_:)](<set/droplast(__).md>) — 返回一个子序列，包含除末尾指定数量元素之外的所有元素。
- [popFirst()](<set/popfirst().md>) — 移除并返回集合的第一个元素。

### 反转集合的元素

- [reversed()](<set/reversed().md>) — 返回一个数组，以相反顺序包含此序列中的元素。

### 分割与连接元素

- [joined()](<set/joined().md>) — 返回此序列组成的序列中各元素连接后的结果。
- [joined(separator:)](<set/joined(separator_)-7ubey.md>) — 返回此序列组成的序列中各元素连接后的结果，并在每个元素之间插入给定的分隔符。
- [joined(separator:)](<set/joined(separator_)-1cko4.md>) — 通过连接序列中的元素并在每个元素之间添加给定的分隔符，返回一个新字符串。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<set/split(separator_maxsplits_omittingemptysubsequences_).md>) — 按顺序返回集合中最长的、围绕等于给定元素的元素分割得到的子序列。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<set/split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合中最长的、不包含满足给定谓词的元素的子序列。
