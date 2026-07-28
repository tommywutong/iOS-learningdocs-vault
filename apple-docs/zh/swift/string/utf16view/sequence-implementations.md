---
title: Sequence 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/utf16view/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/utf16view/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf16view/sequence-implementations.json'
content_hash: 'sha256:9bfeab6808763d26'
translated: true
---

> 导航：[技术](<../../../technologies.md>) · [Swift](<../../../swift.md>) · [String](<../../string.md>) · [UTF16View](../utf16view.md)

# Sequence 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [lazy](lazy.md) — 一个包含与此序列相同元素的序列，但某些操作（例如 `map` 和 `filter`）会惰性实现。

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示序列的每个元素是否都满足给定的谓词。
- [compactMap(_:)](<compactmap(__).md>) — 返回一个数组，其中包含对此序列的每个元素调用给定转换所得到的非 `nil` 结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示序列是否包含给定的元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示序列是否包含满足给定谓词的元素。
- [count(where:)](<count(where_).md>) — 返回序列中满足给定谓词的元素数量。
- [elementsEqual(_:)](<elementsequal(__).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含相同元素。
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — 返回一个布尔值，指示此序列与另一个序列是否以相同顺序包含等价元素，使用给定谓词作为等价性测试。
- [enumerated()](<enumerated().md>) — 返回一个由对偶 (_n_, _x_) 组成的序列，其中 _n_ 表示从零开始的连续整数，_x_ 表示序列的一个元素。
- [filter(_:)](<filter(__).md>) — 返回一个数组，其中按顺序包含序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-4cccc.md>) — 返回一个数组，其中包含对此序列的每个元素调用给定转换所得到的拼接结果。
- [flatMap(_:)](<flatmap(__)-5kmpj.md>)
- [forEach(_:)](<foreach(__).md>) — 以与 `for`-`in` 循环相同的顺序，在序列的每个元素上调用给定的闭包。
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — 返回一个布尔值，指示该序列在字典序中是否先于另一个序列，使用小于运算符 (`<`) 比较元素。
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — 返回一个布尔值，指示该序列在字典序中是否先于另一个序列，使用给定的谓词比较元素。
- [map(_:)](<map(__)-7ggk1.md>) — 返回一个数组，其中包含将给定闭包映射到序列元素上的结果。
- [max()](<max().md>) — 返回序列中的最大元素。
- [max(by:)](<max(by_).md>) — 返回序列中的最大元素，使用给定的谓词作为元素间的比较。
- [min()](<min().md>) — 返回序列中的最小元素。
- [min(by:)](<min(by_).md>) — 返回序列中的最小元素，使用给定的谓词作为元素间的比较。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包组合序列元素的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 返回使用给定闭包组合序列元素的结果。
- [shuffled()](<shuffled().md>) — 返回序列中打乱顺序后的元素。
- [shuffled(using:)](<shuffled(using_).md>) — 返回序列中打乱顺序后的元素，使用给定的生成器作为随机性来源。
- [sorted()](<sorted().md>) — 返回序列中排序后的元素。
- [sorted(by:)](<sorted(by_).md>) — 返回序列中排序后的元素，使用给定的谓词作为元素间的比较。
- [starts(with:)](<starts(with_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素相同。
- [starts(with:by:)](<starts(with_by_).md>) — 返回一个布尔值，指示序列的初始元素是否与另一个序列中的元素等价，使用给定的谓词作为等价性测试。
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — 对序列的连续存储执行一个闭包。

### 类型别名

- [Element](element.md) — 表示序列元素的类型。
