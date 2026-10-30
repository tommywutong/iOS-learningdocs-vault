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
doc_path: /documentation/swift/unsafebufferpointer/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/sequence-implementations.json'
content_hash: 'sha256:72d126567b914b92'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# 序列实现

<sub>API 集合</sub>

## 主题

### 结构体

- [Iterator](iterator.md) — 一个用于 `UnsafeBufferPointer` 或 `UnsafeMutableBufferPointer` 实例所引用缓冲区中元素的迭代器。

### 实例属性

- [lazy](lazy.md) — 一个包含与此序列相同元素的序列，但其上的某些操作（如 `map` 和 `filter`）以惰性方式实现。
- [underestimatedCount](underestimatedcount-4t0go.md) — 一个小于或等于序列中元素数量的值，以非破坏性方式计算。

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示序列的每个元素是否都满足给定的谓词。
- [compactMap(_:)](<compactmap(__).md>) — 返回一个数组，其中包含对此序列的每个元素调用给定转换所得的非 `nil` 结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示序列是否包含给定的元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示序列是否包含满足给定谓词的元素。
- [count(where:)](<count(where_).md>) — 返回序列中满足给定谓词的元素数量。
- [drop(while:)](<drop(while_)-7a7l4.md>) — 通过跳过开头连续满足给定谓词的元素来返回一个序列。
- [dropFirst(_:)](<dropfirst(__)-9f3ee.md>) — 返回一个序列，其中包含除开头给定数量元素之外的所有元素。
- [dropLast(_:)](<droplast(__)-8b3kj.md>) — 返回一个序列，其中包含除末尾给定数量元素之外的所有元素。
- [elementsEqual(_:)](<elementsequal(__).md>) — 返回一个布尔值，指示此序列和另一个序列是否以相同顺序包含相同的元素。
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — 返回一个布尔值，指示此序列和另一个序列是否以相同顺序包含等价的元素，使用给定谓词作为等价性测试。
- [enumerated()](<enumerated().md>) — 返回一个由数对（_n_, _x_）组成的序列，其中 _n_ 表示从零开始的连续整数，_x_ 表示序列中的一个元素。
- [filter(_:)](<filter(__).md>) — 返回一个数组，按顺序包含序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-6chur.md>)
- [flatMap(_:)](<flatmap(__)-i3m8.md>) — 返回一个数组，其中包含对此序列的每个元素调用给定转换所得结果的拼接。
- [forEach(_:)](<foreach(__).md>) — 以与 `for`-`in` 循环相同的顺序，对序列中的每个元素调用给定的闭包。
- [joined()](<joined().md>) — 返回此序列的序列中的元素，已拼接。
- [joined(separator:)](<joined(separator_)-1ckny.md>) — 通过拼接序列的元素返回一个新字符串，并在每个元素之间添加给定的分隔符。
- [joined(separator:)](<joined(separator_)-7ubg0.md>) — 返回此序列的序列拼接后的元素，并在每个元素之间插入给定的分隔符。
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — 返回一个布尔值，指示该序列在词典序（字典）排序中是否先于另一个序列，使用小于运算符（`<`）比较元素。
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示该序列在词典序（字典）排序中是否先于另一个序列，使用给定谓词比较元素。
- [makeIterator()](<makeiterator().md>) — 返回一个在此缓冲区的元素上进行迭代的迭代器。
- [map(_:)](<map(__)-9jnnu.md>) — 返回一个数组，其中包含将给定闭包映射到序列元素上的结果。
- [max()](<max().md>) — 返回序列中的最大元素。
- [max(by:)](<max(by_).md>) — 返回序列中的最大元素，使用给定谓词作为元素之间的比较。
- [min()](<min().md>) — 返回序列中的最小元素。
- [min(by:)](<min(by_).md>) — 返回序列中的最小元素，使用给定谓词作为元素之间的比较。
- [prefix(_:)](<prefix(__)-9jcr4.md>) — 返回一个序列，最多包含指定最大数量的序列开头元素。
- [prefix(while:)](<prefix(while_)-3il7m.md>) — 返回一个序列，其中包含开头连续满足给定谓词的元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包组合序列元素的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 返回使用给定闭包组合序列元素的结果。
- [reversed()](<reversed()-24fls.md>) — 返回一个数组，以相反的顺序包含此序列的元素。
- [shuffled()](<shuffled().md>) — 返回序列的元素，已打乱。
- [shuffled(using:)](<shuffled(using_).md>) — 返回序列的元素，使用给定的生成器作为随机性来源进行打乱。
- [sorted()](<sorted().md>) — 返回序列的元素，已排序。
- [sorted(by:)](<sorted(by_).md>) — 返回序列的元素，已使用给定谓词作为元素之间的比较进行排序。
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_)-5m0k2.md>) — 按顺序返回序列中不包含满足给定谓词的元素的最长可能子序列。用于拆分序列的元素不会作为任何子序列的一部分返回。
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-9bdw7.md>) — 按顺序返回序列中围绕等于给定元素的元素进行拆分的最长可能子序列。
- [starts(with:)](<starts(with_).md>) — 返回一个布尔值，指示序列的开头元素是否与另一个序列中的元素相同。
- [starts(with:by:)](<starts(with_by_).md>) — 返回一个布尔值，指示序列的开头元素是否与另一个序列中的元素等价，使用给定谓词作为等价性测试。
- [suffix(_:)](<suffix(__)-1rpxh.md>) — 返回一个子序列，最多包含给定最大数量的序列末尾元素。
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — 在序列的连续存储上执行闭包。
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__)-1ynrz.md>) — 在序列的连续存储上执行闭包。
