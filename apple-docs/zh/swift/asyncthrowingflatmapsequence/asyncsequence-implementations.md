---
title: AsyncSequence 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingflatmapsequence/asyncsequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingflatmapsequence/asyncsequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingflatmapsequence/asyncsequence-implementations.json'
content_hash: 'sha256:e42e438ae876bb9c'
translated: true
---

> 导航：[技术](<../../technologies.md>) · [Swift](<../../swift.md>) · [Swift 标准库](../swift-standard-library.md) · [并发](../concurrency.md) · [AsyncSequence](../asyncsequence.md) · [AsyncThrowingFlatMapSequence](../asyncthrowingflatmapsequence.md)

# AsyncSequence 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示异步序列（asynchronous sequence）生成的所有元素是否都满足给定的谓词（predicate）。
- [compactMap(_:)](<compactmap(__)-4299z.md>) — 创建一个异步序列，该序列将给定的闭包（closure）映射到异步序列的元素上，并省略那些不返回值的元素。
- [compactMap(_:)](<compactmap(__)-8k2p7.md>) — 创建一个异步序列，该序列将一个可抛出错误的闭包映射到基础序列（base sequence）的元素上，并省略那些不返回值的元素。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示异步序列是否包含给定元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示异步序列是否包含满足给定谓词的元素。
- [drop(while:)](<drop(while_).md>) — 从基础异步序列中省略元素，直到给定的闭包返回 `false`，之后传递所有剩余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 从基础异步序列中省略指定数量的元素，然后传递所有剩余元素。
- [filter(_:)](<filter(__).md>) — 创建一个异步序列，该序列按顺序包含满足给定谓词的基础序列的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-305n4.md>) — 创建一个异步序列，该序列连接了对该序列的每个元素调用给定转换的结果。
- [flatMap(_:)](<flatmap(__)-39bbv.md>) — 创建一个异步序列，该序列连接了对该序列的每个元素调用给定的可抛出错误的转换的结果。
- [flatMap(_:)](<flatmap(__)-6oqyf.md>) — 创建一个异步序列，该序列连接了对该序列的每个元素调用给定转换的结果。
- [flatMap(_:)](<flatmap(__)-917rm.md>) — 创建一个异步序列，该序列连接了对该序列的每个元素调用给定转换的结果。
- [makeAsyncIterator()](<makeasynciterator().md>) — 创建一个用于生成此异步序列元素的异步迭代器。
- [map(_:)](<map(__)-81b46.md>) — 创建一个异步序列，该序列将给定的可抛出错误的闭包映射到异步序列的元素上。
- [map(_:)](<map(__)-p3ci.md>) — 创建一个异步序列，该序列将给定的闭包映射到异步序列的元素上。
- [max()](<max().md>) — 返回一个由可比较元素组成的异步序列中的最大元素。
- [max(by:)](<max(by_).md>) — 返回异步序列中的最大元素，使用给定的谓词作为元素之间的比较。
- [min()](<min().md>) — 返回一个由可比较元素组成的异步序列中的最小元素。
- [min(by:)](<min(by_).md>) — 返回异步序列中的最小元素，使用给定的谓词作为元素之间的比较。
- [prefix(_:)](<prefix(__).md>) — 返回一个异步序列，包含基础异步序列的初始元素，最多不超过指定的最大长度。
- [prefix(while:)](<prefix(while_).md>) — 返回一个异步序列，包含基础序列中满足给定谓词的初始、连续元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包组合异步序列元素的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 给定一个可变的初始值，返回使用给定闭包组合异步序列元素的结果。

### 类型别名

- [AsyncIterator](asynciterator.md) — 生成序列元素的迭代器类型。
- [Element](element.md) — 此异步序列生成的元素类型。
