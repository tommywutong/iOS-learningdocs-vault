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
doc_path: /documentation/swift/reversedcollection/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/sequence-implementations.json'
content_hash: 'sha256:ae5c0a7a2214e1c2'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [集合](../collections.md) · [支持类型](../supporting-types.md) · [ReversedCollection](../reversedcollection.md)

# 序列实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Iterator](iterator.md) — 提供序列的迭代接口并封装其迭代状态的类型。

### 实例属性

- [lazy](lazy.md) — 一个包含与此序列相同元素的序列，但某些操作（如 `map` 和 `filter`）会惰性实现。

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示序列中的每个元素是否都满足给定的谓词（predicate）。
- [compactMap(_:)](<compactmap(__)-2ra13.md>) — 返回一个数组，其中包含对此序列的每个元素调用给定转换后得到的非 `nil` 结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示序列是否包含给定的元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示序列是否包含满足给定谓词的某个元素。
- [count(where:)](<count(where_).md>) — 返回序列中满足给定谓词的元素个数。
- [elementsEqual(_:)](<elementsequal(__).md>) — 返回一个布尔值，指示此序列与另一序列是否以相同顺序包含相同元素。
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — 返回一个布尔值，指示此序列与另一序列是否以相同顺序包含等价元素，使用给定的谓词作为等价性测试。
- [enumerated()](<enumerated().md>) — 返回一个由对偶 (_n_, _x_) 组成的序列，其中 _n_ 表示从零开始的连续整数，_x_ 是序列中的元素。
- [filter(_:)](<filter(__)-9g9gk.md>) — 返回一个数组，按顺序包含序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-17mz1.md>) — 返回一个数组，包含对此序列的每个元素调用给定转换后，将所有结果拼接在一起的内容。
- [flatMap(_:)](<flatmap(__)-9kclv.md>)
- [forEach(_:)](<foreach(__).md>) — 按与 `for`-`in` 循环相同的顺序，对序列中的每个元素调用给定的闭包（closure）。
- [joined()](<joined()-448f.md>) — 返回此序列的序列的元素，将它们拼接起来。
- [joined(separator:)](<joined(separator_)-1ijrz.md>) — 通过拼接序列的元素并添加给定的分隔符，返回一个新字符串。
- [joined(separator:)](<joined(separator_)-xipx.md>) — 返回此序列的序列的拼接元素，并在每个元素之间插入给定的分隔符。
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — 返回一个布尔值，指示字典序中该序列是否先于另一序列，使用小于运算符（`<`）比较元素。
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示字典序中该序列是否先于另一序列，使用给定的谓词比较元素。
- [makeIterator()](<makeiterator().md>) — 返回一个作用于该序列元素的迭代器。
- [map(_:)](<map(__)-6gkpm.md>) — 返回一个数组，包含在序列的元素上映射给定闭包的结果。
- [max()](<max().md>) — 返回序列中的最大元素。
- [max(by:)](<max(by_).md>) — 返回序列中的最大元素，使用给定的谓词作为元素间的比较。
- [min()](<min().md>) — 返回序列中的最小元素。
- [min(by:)](<min(by_).md>) — 返回序列中的最小元素，使用给定的谓词作为元素间的比较。
- [reduce(_:_:)](<reduce(____).md>) — 通过给定的闭包组合序列的元素，并返回结果。
- [reduce(into:_:)](<reduce(into___).md>) — 通过给定的闭包组合序列的元素，并返回结果。
- [shuffled()](<shuffled().md>) — 返回随机重排后的序列元素。
- [shuffled(using:)](<shuffled(using_).md>) — 返回随机重排后的序列元素，使用给定的生成器作为随机源。
- [sorted()](<sorted().md>) — 返回排序后的序列元素。
- [sorted(by:)](<sorted(by_).md>) — 返回排序后的序列元素，使用给定的谓词作为元素间的比较。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-59vb5.md>) — 按顺序返回序列中最长的可能子序列，这些子序列由与给定元素相等的元素进行分隔。
- [starts(with:)](<starts(with_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一序列中的元素相同。
- [starts(with:by:)](<starts(with_by_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一序列中的元素等价，使用给定的谓词作为等价性测试。
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — 在序列的连续存储上执行一个闭包。

### 类型别名

- [Element](element.md) — 表示集合中有效位置的类型。
