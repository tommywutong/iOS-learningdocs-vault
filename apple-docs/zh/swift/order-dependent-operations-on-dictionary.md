---
title: 字典上依赖顺序的操作
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/order-dependent-operations-on-dictionary
source_url: 'https://developer.apple.com/documentation/swift/order-dependent-operations-on-dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/order-dependent-operations-on-dictionary.json'
content_hash: 'sha256:1c141d92dc956878'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Dictionary](dictionary.md)

# 字典上依赖顺序的操作

<sub>API 集合</sub>

执行所有集合通用的依赖顺序的操作，即 `Dictionary` 所采用的实现。

## 主题

### 比较字典

- [elementsEqual(_:by:)](<dictionary/elementsequal(__by_).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含等价的元素，并使用给定的谓词作为等价性测试。
- [starts(with:by:)](<dictionary/starts(with_by_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素等价，并使用给定的谓词作为等价性测试。
- [lexicographicallyPrecedes(_:by:)](<dictionary/lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示序列是否在字典排序中先于另一个序列，并使用给定的谓词比较元素。

### 操作索引

- [startIndex](dictionary/startindex.md) — 非空字典中第一个元素的位置。
- [endIndex](dictionary/endindex.md) — 该字典末尾之后的位置——即比最后一个有效下标参数大 1 的位置。
- [index(after:)](<dictionary/index(after_).md>) — 返回紧随给定索引之后的位置。
- [formIndex(after:)](<dictionary/formindex(after_).md>) — 用其后继位置替换给定的索引。
- [index(_:offsetBy:)](<dictionary/index(__offsetby_).md>) — 返回与给定索引相距指定距离的索引。
- [formIndex(_:offsetBy:)](<dictionary/formindex(__offsetby_).md>) — 将给定的索引偏移指定的距离。
- [index(_:offsetBy:limitedBy:)](<dictionary/index(__offsetby_limitedby_).md>) — 返回与给定索引相距指定距离的索引，除非该距离超出了给定的限制索引。
- [formIndex(_:offsetBy:limitedBy:)](<dictionary/formindex(__offsetby_limitedby_).md>) — 将给定的索引偏移指定的距离，或使其等于给定的限制索引。
- [distance(from:to:)](<dictionary/distance(from_to_).md>) — 返回两个索引之间的距离。
- [indices](dictionary/indices-swift.property.md) — 可用于对集合进行下标操作的有效索引，按升序排列。

### 选择元素

- [subscript(_:)](<dictionary/subscript(__)-2ny9y.md>) — 访问集合元素的一个连续子范围。
- [subscript(_:)](<dictionary/subscript(__)-4h7sk.md>) — 访问由范围表达式指定的集合元素的连续子范围。
- [subscript(_:)](<dictionary/subscript(__)-4al9z.md>)
- [prefix(_:)](<dictionary/prefix(__).md>) — 返回一个子序列，包含集合开头的元素，长度不超过指定的最大长度。
- [prefix(through:)](<dictionary/prefix(through_).md>) — 返回一个从集合开头直到（包含）指定位置的子序列。
- [prefix(upTo:)](<dictionary/prefix(upto_).md>) — 返回一个从集合开头直到（但不包含）指定位置的子序列。
- [prefix(while:)](<dictionary/prefix(while_).md>) — 返回一个子序列，包含 `predicate` 返回 `false` 之前的开头元素，并跳过其余元素。
- [suffix(_:)](<dictionary/suffix(__).md>) — 返回一个子序列，包含集合末尾的元素，长度不超过给定的最大长度。
- [suffix(from:)](<dictionary/suffix(from_).md>) — 返回一个从指定位置到集合末尾的子序列。

### 排除元素

- [dropFirst(_:)](<dictionary/dropfirst(__).md>) — 返回一个子序列，包含除开头给定数量元素之外的所有元素。
- [drop(while:)](<dictionary/drop(while_).md>) — 通过跳过 `predicate` 返回 `true` 的元素并返回其余元素，返回一个子序列。
- [dropLast(_:)](<dictionary/droplast(__).md>) — 返回一个子序列，包含除末尾指定数量元素之外的所有元素。
- [popFirst()](<dictionary/popfirst().md>) — 如果字典非空，则移除并返回字典的第一个键值对。

### 转换字典的元素

- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<dictionary/split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回集合中最长的、不包含满足给定谓词的元素的子序列。
- [reversed()](<dictionary/reversed().md>) — 返回一个数组，以相反顺序包含此序列中的元素。
- [withContiguousStorageIfAvailable(_:)](<dictionary/withcontiguousstorageifavailable(__).md>) — 对序列的连续存储执行一个闭包。
