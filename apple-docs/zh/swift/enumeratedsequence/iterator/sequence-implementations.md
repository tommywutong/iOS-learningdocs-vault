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
doc_path: /documentation/swift/enumeratedsequence/iterator/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/iterator/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/iterator/sequence-implementations.json'
content_hash: 'sha256:969979c419b80007'
translated: true
---

> 导航：[技术](../../../technologies.md) · [Swift](../../../swift.md) · [Swift 标准库](../../swift-standard-library.md) · [集合](../../collections.md) · [支持类型](../../supporting-types.md) · [EnumeratedSequence](../../enumeratedsequence.md) · [序列实现](../sequence-implementations.md) · [Iterator](../iterator.md)

# 序列实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [lazy](lazy.md) — 一个序列，包含与此序列相同的元素，但一些操作（例如 `map` 和 `filter`）是以惰性方式实现的。
- [underestimatedCount](underestimatedcount.md) — 以非破坏方式计算出的值，小于或等于序列中的元素数量。

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示序列中的每个元素是否都满足给定的谓词（predicate）。
- [compactMap(_:)](<compactmap(__).md>) — 返回一个数组，包含将给定的转换闭包（closure）应用于此序列的每个元素所得到的非 `nil` 结果。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示序列是否包含满足给定谓词的元素。
- [count(where:)](<count(where_).md>) — 返回序列中满足给定谓词的元素数量。
- [drop(while:)](<drop(while_).md>) — 返回一个序列，通过跳过开头连续的、满足给定谓词的元素得到。
- [dropFirst(_:)](<dropfirst(__).md>) — 返回一个序列，包含除开头给定数量元素之外的所有元素。
- [dropLast(_:)](<droplast(__).md>) — 返回一个序列，包含除末尾给定数量元素之外的所有元素。
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含等价的元素，并使用给定的谓词作为等价性测试。
- [enumerated()](<enumerated().md>) — 返回一个由对偶 (_n_, _x_) 组成的序列，其中 _n_ 表示从零开始的连续整数，_x_ 表示序列中的一个元素。
- [filter(_:)](<filter(__).md>) — 返回一个数组，按顺序包含序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-50wvd.md>)
- [flatMap(_:)](<flatmap(__)-98frp.md>) — 返回一个数组，包含将给定的转换闭包应用于此序列的每个元素所得到的连接结果。
- [forEach(_:)](<foreach(__).md>) — 以与 `for`-`in` 循环相同的顺序，对序列中的每个元素调用给定的闭包。
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示序列是否在字典排序中先于另一个序列，并使用给定的谓词比较元素。
- [makeIterator()](<makeiterator().md>) — 返回一个在此序列的元素上进行迭代的迭代器。
- [map(_:)](<map(__).md>) — 返回一个数组，包含将给定的闭包映射到序列元素后得到的结果。
- [max(by:)](<max(by_).md>) — 返回序列中的最大元素，使用给定的谓词作为元素之间的比较方式。
- [min(by:)](<min(by_).md>) — 返回序列中的最小元素，使用给定的谓词作为元素之间的比较方式。
- [prefix(_:)](<prefix(__).md>) — 返回一个序列，包含序列开头的元素，长度不超过指定的最大长度。
- [prefix(while:)](<prefix(while_).md>) — 返回一个序列，包含开头连续的、满足给定谓词的元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定的闭包组合序列元素后的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 返回使用给定的闭包组合序列元素后的结果。
- [reversed()](<reversed().md>) — 返回一个数组，以相反顺序包含此序列中的元素。
- [shuffled()](<shuffled().md>) — 返回打乱顺序后的序列元素。
- [shuffled(using:)](<shuffled(using_).md>) — 返回打乱顺序后的序列元素，使用给定的生成器作为随机源。
- [sorted(by:)](<sorted(by_).md>) — 返回排序后的序列元素，使用给定的谓词作为元素之间的比较方式。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — 按顺序返回序列中最长的、不包含满足给定谓词的元素的子序列。用于分割序列的元素不会作为任何子序列的一部分返回。
- [starts(with:by:)](<starts(with_by_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素等价，并使用给定的谓词作为等价性测试。
- [suffix(_:)](<suffix(__).md>) — 返回一个子序列，包含序列末尾的元素，长度不超过给定的最大长度。
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — 对序列的连续存储执行一个闭包。

### 类型别名

- [Iterator](iterator.md) — 一种提供序列迭代接口并封装其迭代状态的类型。
