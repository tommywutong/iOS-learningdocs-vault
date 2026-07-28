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
doc_path: /documentation/swift/asyncthrowingfiltersequence/asyncsequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingfiltersequence/asyncsequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingfiltersequence/asyncsequence-implementations.json'
content_hash: 'sha256:d7ce02bc57467116'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [并发](../concurrency.md) · [AsyncSequence](../asyncsequence.md) · [AsyncThrowingFilterSequence](../asyncthrowingfiltersequence.md)

# AsyncSequence 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示异步序列产生的所有元素是否都满足给定的谓词（predicate）。
- [compactMap(_:)](<compactmap(__)-6sxlx.md>) — 创建一个异步序列，该序列对基础序列中的元素映射一个会抛出错误的闭包（closure），并忽略不返回值的结果。
- [compactMap(_:)](<compactmap(__)-7anrq.md>) — 创建一个异步序列，该序列对异步序列中的元素映射给定的闭包，并忽略不返回值的结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示异步序列是否包含给定的元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示异步序列是否包含满足给定谓词的元素。
- [drop(while:)](<drop(while_).md>) — 从基础异步序列中丢弃元素，直到给定的闭包返回 `false`，之后放行所有剩余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 从基础异步序列中丢弃指定数量的元素，然后放行所有剩余元素。
- [filter(_:)](<filter(__).md>) — 创建一个异步序列，按顺序包含基础序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-4l7g6.md>) — 创建一个异步序列，该序列通过对每个元素调用给定的转换，并将所得的结果拼接起来。
- [flatMap(_:)](<flatmap(__)-646yb.md>) — 创建一个异步序列，该序列通过对每个元素调用给定的转换，并将所得的结果拼接起来。
- [flatMap(_:)](<flatmap(__)-jrk7.md>) — 创建一个异步序列，该序列通过对每个元素调用给定的会抛出错误的转换，并将所得的结果拼接起来。
- [flatMap(_:)](<flatmap(__)-lxav.md>) — 创建一个异步序列，该序列通过对每个元素调用给定的转换，并将所得的结果拼接起来。
- [makeAsyncIterator()](<makeasynciterator().md>) — 创建用于产生此异步序列元素的异步迭代器。
- [map(_:)](<map(__)-56b34.md>) — 创建一个异步序列，该序列对异步序列中的元素映射给定的可能抛出错误的闭包。
- [map(_:)](<map(__)-6flae.md>) — 创建一个异步序列，该序列对异步序列中的元素映射给定的闭包。
- [max()](<max().md>) — 返回包含可比较元素的异步序列中的最大元素。
- [max(by:)](<max(by_).md>) — 使用给定的谓词作为元素间的比较，返回异步序列中的最大元素。
- [min()](<min().md>) — 返回包含可比较元素的异步序列中的最小元素。
- [min(by:)](<min(by_).md>) — 使用给定的谓词作为元素间的比较，返回异步序列中的最小元素。
- [prefix(_:)](<prefix(__).md>) — 返回一个异步序列，包含基础异步序列中直到指定最大数量的起始元素。
- [prefix(while:)](<prefix(while_).md>) — 返回一个异步序列，包含基础序列中连续且满足给定谓词的起始元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包组合异步序列中元素得到的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 给定一个可变的初始值，返回使用给定闭包组合异步序列中元素得到的结果。

### 类型别名

- [AsyncIterator](asynciterator.md) — 产生序列元素的迭代器的类型。
- [Element](element.md) — 此异步序列产生的元素的类型。
