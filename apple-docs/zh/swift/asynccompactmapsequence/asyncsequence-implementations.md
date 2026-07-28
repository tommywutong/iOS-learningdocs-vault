---
title: AsyncSequence 的实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asynccompactmapsequence/asyncsequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/asynccompactmapsequence/asyncsequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynccompactmapsequence/asyncsequence-implementations.json'
content_hash: 'sha256:baec589082e65cc6'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [并发](../concurrency.md) · [AsyncSequence](../asyncsequence.md) · [AsyncCompactMapSequence](../asynccompactmapsequence.md)

# AsyncSequence 的实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示异步序列产生的所有元素是否都满足给定的谓词（predicate）。
- [compactMap(_:)](<compactmap(__)-2zfm7.md>) — 创建一个异步序列，该序列将给定闭包映射到异步序列的元素上，并忽略不返回值的那些结果。
- [compactMap(_:)](<compactmap(__)-9t1q8.md>) — 创建一个异步序列，该序列将可能抛出错误的闭包映射到基础序列的元素上，并忽略不返回值的那些结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示异步序列是否包含给定的元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示异步序列是否包含满足给定谓词（predicate）的元素。
- [drop(while:)](<drop(while_).md>) — 在给定闭包返回 `false` 之前，忽略基础异步序列中的元素，之后会传递所有剩余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 忽略基础异步序列中指定数量的元素，然后传递所有剩余元素。
- [filter(_:)](<filter(__).md>) — 创建一个异步序列，该序列按顺序包含基础序列中满足给定谓词（predicate）的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词（predicate）的第一个元素。
- [flatMap(_:)](<flatmap(__)-4d56a.md>) — 创建一个异步序列，该序列对该异步序列的每个元素调用给定的变换，并将所有结果拼接在一起。
- [flatMap(_:)](<flatmap(__)-7yxkz.md>) — 创建一个异步序列，该序列对该异步序列的每个元素调用可能抛出错误的给定变换，并将所有结果拼接在一起。
- [flatMap(_:)](<flatmap(__)-9qp1p.md>) — 创建一个异步序列，该序列对该异步序列的每个元素调用给定的变换，并将所有结果拼接在一起。
- [flatMap(_:)](<flatmap(__)-zzcb.md>) — 创建一个异步序列，该序列对该异步序列的每个元素调用给定的变换，并将所有结果拼接在一起。
- [makeAsyncIterator()](<makeasynciterator().md>) — 创建产生此异步序列元素的异步迭代器。
- [map(_:)](<map(__)-21iha.md>) — 创建一个异步序列，该序列将可能抛出错误的给定闭包映射到异步序列的元素上。
- [map(_:)](<map(__)-8rz0x.md>) — 创建一个异步序列，该序列将给定闭包映射到异步序列的元素上。
- [max()](<max().md>) — 返回由可比较元素组成的异步序列中的最大元素。
- [max(by:)](<max(by_).md>) — 返回异步序列中的最大元素，使用给定的谓词（predicate）作为元素之间的比较准则。
- [min()](<min().md>) — 返回由可比较元素组成的异步序列中的最小元素。
- [min(by:)](<min(by_).md>) — 返回异步序列中的最小元素，使用给定的谓词（predicate）作为元素之间的比较准则。
- [prefix(_:)](<prefix(__).md>) — 返回一个异步序列，包含基础异步序列的初始元素，长度不超过指定的最大值。
- [prefix(while:)](<prefix(while_).md>) — 返回一个异步序列，包含基础序列中连续、满足给定谓词（predicate）的初始元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包合并异步序列元素后的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 返回使用给定闭包合并异步序列元素后的结果，并给定一个可变的初始值。

### 类型别名

- [AsyncIterator](asynciterator.md) — 产生序列元素的迭代器类型。
- [Element](element.md) — 此异步序列产生的元素类型。
