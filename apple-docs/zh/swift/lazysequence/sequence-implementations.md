---
title: 序列实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequence/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/sequence-implementations.json'
content_hash: 'sha256:a7661ecb4a72fde2'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [LazySequence](../lazysequence.md)

# 序列实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [underestimatedCount](underestimatedcount.md) — 一个小于或等于序列中元素数量的值，以非破坏性方式计算。

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示序列中的每个元素是否都满足给定的谓词（predicate）。
- [compactMap(_:)](<compactmap(__)-420ej.md>) — 返回一个数组，包含将给定的转换闭包（closure）应用于此序列的每个元素所得到的非 `nil` 结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示序列是否包含给定的元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示序列是否包含满足给定谓词的元素。
- [count(where:)](<count(where_).md>) — 返回序列中满足给定谓词的元素数量。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个序列，包含除开头给定数量元素之外的所有元素。
- [dropLast(_:)](<droplast(__).md>) — 返回一个序列，包含除末尾给定数量元素之外的所有元素。
- [elementsEqual(_:)](<elementsequal(__).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含相同的元素。
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含等价的元素，并使用给定的谓词作为等价性测试。
- [enumerated()](<enumerated().md>) — 返回一个由对偶 (_n_, _x_) 组成的序列，其中 _n_ 表示从零开始的连续整数，_x_ 表示序列中的一个元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-6y096.md>)
- [flatMap(_:)](<flatmap(__)-8fefz.md>) — 返回一个数组，包含将给定的转换闭包应用于此序列的每个元素所得到的连接结果。
- [forEach(_:)](<foreach(__).md>) — 以与 `for`-`in` 循环相同的顺序，对序列中的每个元素调用给定的闭包。
- [joined()](<joined()-2ibvq.md>) — 返回此序列组成的序列中各元素连接后的结果。
- [joined(separator:)](<joined(separator_)-26r7k.md>) — 返回此序列组成的序列中各元素连接后的结果，并在每个元素之间插入给定的分隔符。
- [joined(separator:)](<joined(separator_)-7b5x0.md>) — 通过连接序列中的元素并在每个元素之间添加给定的分隔符，返回一个新字符串。
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — 返回一个布尔值，指示序列在字典（lexicographical）排序中是否先于另一个序列，并使用小于运算符（`<`）比较元素。
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示序列是否在字典排序中先于另一个序列，并使用给定的谓词比较元素。
- [map(_:)](<map(__)-31x8w.md>) — 返回一个数组，包含将给定的闭包映射到序列元素后得到的结果。
- [max()](<max().md>) — 返回序列中的最大元素。
- [max(by:)](<max(by_).md>) — 返回序列中的最大元素，使用给定的谓词作为元素之间的比较方式。
- [min()](<min().md>) — 返回序列中的最小元素。
- [min(by:)](<min(by_).md>) — 返回序列中的最小元素，使用给定的谓词作为元素之间的比较方式。
- [prefix(_:)](<prefix(__).md>) — 返回一个序列，最多包含指定最大数量的序列开头元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定的闭包组合序列元素后的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 返回使用给定的闭包组合序列元素后的结果。
- [reversed()](<reversed().md>) — 返回一个数组，以相反的顺序包含此序列的元素。
- [shuffled()](<shuffled().md>) — 返回打乱顺序后的序列元素。
- [shuffled(using:)](<shuffled(using_).md>) — 返回打乱顺序后的序列元素，使用给定的生成器作为随机源。
- [sorted()](<sorted().md>) — 返回排序后的序列元素。
- [sorted(by:)](<sorted(by_).md>) — 返回排序后的序列元素，使用给定的谓词作为元素之间的比较方式。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回序列中最长的、不包含满足给定谓词的元素的子序列。用于分割序列的元素不会作为任何子序列的一部分返回。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-3ls1g.md>) — 按顺序返回序列中最长的、围绕等于给定元素的元素分割得到的子序列。
- [starts(with:)](<starts(with_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素相同。
- [starts(with:by:)](<starts(with_by_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素等价，并使用给定的谓词作为等价性测试。
- [suffix(_:)](<suffix(__).md>) — 返回一个子序列，最多包含给定最大数量的序列末尾元素。
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — 对序列的连续存储执行一个闭包。

### 类型别名

- [Element](element.md) — 一种表示序列元素的类型。
