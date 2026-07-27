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
doc_path: /documentation/swift/asyncthrowingmapsequence/asyncsequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/asyncsequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingmapsequence/asyncsequence-implementations.json'
content_hash: 'sha256:da47b60746f90dd4'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [并发](../concurrency.md) · [AsyncSequence](../asyncsequence.md) · [AsyncThrowingMapSequence](../asyncthrowingmapsequence.md)

# AsyncSequence 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示异步序列生成的所有元素是否都满足给定谓词。
- [compactMap(_:)](<compactmap(__)-1rx1n.md>) — 创建一个异步序列，将可抛出错误的闭包映射到基础序列的元素上，并省略未返回值的结果。
- [compactMap(_:)](<compactmap(__)-91i6y.md>) — 创建一个异步序列，将给定闭包映射到异步序列的元素上，并省略未返回值的结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示异步序列是否包含给定元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示异步序列是否包含满足给定谓词的元素。
- [drop(while:)](<drop(while_).md>) — 从基础异步序列中省略元素，直到给定闭包返回 false，之后传递所有剩余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 从基础异步序列中省略指定数量的元素，然后传递所有剩余元素。
- [filter(_:)](<filter(__).md>) — 创建一个异步序列，其中按顺序包含基础序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-1wg0y.md>) — 创建一个异步序列，串接以此序列的每个元素调用给定转换所得到的结果。
- [flatMap(_:)](<flatmap(__)-3jfma.md>) — 创建一个异步序列，串接以此序列的每个元素调用给定转换所得到的结果。
- [flatMap(_:)](<flatmap(__)-53stf.md>) — 创建一个异步序列，串接以此序列的每个元素调用给定可抛出错误转换所得到的结果。
- [flatMap(_:)](<flatmap(__)-9qxu8.md>) — 创建一个异步序列，串接以此序列的每个元素调用给定转换所得到的结果。
- [makeAsyncIterator()](<makeasynciterator().md>) — 创建生成此异步序列元素的异步迭代器。
- [map(_:)](<map(__)-845vf.md>) — 创建一个异步序列，将给定可抛出错误的闭包映射到异步序列的元素上。
- [map(_:)](<map(__)-9s7sb.md>) — 创建一个异步序列，将给定闭包映射到异步序列的元素上。
- [max()](<max().md>) — 返回由可比较元素组成的异步序列中的最大元素。
- [max(by:)](<max(by_).md>) — 使用给定谓词比较元素，返回异步序列中的最大元素。
- [min()](<min().md>) — 返回由可比较元素组成的异步序列中的最小元素。
- [min(by:)](<min(by_).md>) — 使用给定谓词比较元素，返回异步序列中的最小元素。
- [prefix(_:)](<prefix(__).md>) — 返回一个不超过指定最大长度的异步序列，其中包含基础异步序列的起始元素。
- [prefix(while:)](<prefix(while_).md>) — 返回一个异步序列，其中包含基础序列中满足给定谓词的连续起始元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包合并异步序列元素的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 在给定可变初始值的情况下，返回使用给定闭包合并异步序列元素的结果。

### 类型别名

- [AsyncIterator](asynciterator.md) — 生成序列元素的迭代器类型。
- [Element](element.md) — 此异步序列生成的元素类型。
