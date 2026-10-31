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
doc_path: /documentation/swift/asyncfiltersequence/asyncsequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence/asyncsequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence/asyncsequence-implementations.json'
content_hash: 'sha256:8e240375d0ca92ea'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Concurrency](../concurrency.md) · [AsyncSequence](../asyncsequence.md) · [AsyncFilterSequence](../asyncfiltersequence.md)

# AsyncSequence 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [allSatisfy(_:)](<allsatisfy(__).md>) — 返回一个布尔值，指示异步序列生成的所有元素是否都满足给定谓词。
- [compactMap(_:)](<compactmap(__)-1ux9n.md>) — 创建一个异步序列，将给定闭包映射到该异步序列的元素，并省略未返回值的结果。
- [compactMap(_:)](<compactmap(__)-670wo.md>) — 创建一个异步序列，将可抛出错误的闭包映射到基础序列的元素，并省略未返回值的结果。
- [contains(_:)](<contains(__).md>) — 返回一个布尔值，指示异步序列是否包含给定元素。
- [contains(where:)](<contains(where_).md>) — 返回一个布尔值，指示异步序列是否包含满足给定谓词的元素。
- [drop(while:)](<drop(while_).md>) — 从基础异步序列中省略元素，直到给定闭包返回 `false`，随后传递所有剩余元素。
- [dropFirst(_:)](<dropfirst(__).md>) — 从基础异步序列中省略指定数量的元素，随后传递所有剩余元素。
- [filter(_:)](<filter(__).md>) — 创建一个异步序列，其中按顺序包含基础序列中满足给定谓词的元素。
- [first(where:)](<first(where_).md>) — 返回序列中满足给定谓词的第一个元素。
- [flatMap(_:)](<flatmap(__)-5h1r5.md>) — 创建一个异步序列，该序列对此序列的每个元素调用给定的变换，并将所得的结果拼接在一起。
- [flatMap(_:)](<flatmap(__)-7q9h4.md>) — 创建一个异步序列，该序列对此序列的每个元素调用给定的变换，并将所得的结果拼接在一起。
- [flatMap(_:)](<flatmap(__)-8hfy4.md>) — 创建一个异步序列，该序列对此序列的每个元素调用给定的变换，并将所得的结果拼接在一起。
- [flatMap(_:)](<flatmap(__)-kp0l.md>) — 创建一个异步序列，该序列对此序列的每个元素调用给定的可抛出错误的变换，并将所得的结果拼接在一起。
- [makeAsyncIterator()](<makeasynciterator().md>) — 创建生成此异步序列元素的异步迭代器。
- [map(_:)](<map(__)-9wvb.md>) — 创建一个异步序列，将给定可抛出错误的闭包映射到异步序列的元素。
- [map(_:)](<map(__)-ljd0.md>) — 创建一个异步序列，将给定闭包映射到该异步序列的元素。
- [max()](<max().md>) — 返回由可比较元素组成的异步序列中的最大元素。
- [max(by:)](<max(by_).md>) — 使用给定谓词比较元素，返回异步序列中的最大元素。
- [min()](<min().md>) — 返回由可比较元素组成的异步序列中的最小元素。
- [min(by:)](<min(by_).md>) — 使用给定谓词比较元素，返回异步序列中的最小元素。
- [prefix(_:)](<prefix(__).md>) — 返回一个最大不超过指定长度的异步序列，其中包含基础异步序列的开头元素。
- [prefix(while:)](<prefix(while_).md>) — 返回一个异步序列，其中包含基础序列开头连续且满足给定谓词的元素。
- [reduce(_:_:)](<reduce(____).md>) — 返回使用给定闭包合并异步序列元素所得的结果。
- [reduce(into:_:)](<reduce(into___).md>) — 给定一个可变初始值，返回使用给定闭包合并异步序列元素所得的结果。

### 类型别名

- [AsyncIterator](asynciterator.md) — 生成序列元素的迭代器类型。
- [Element](element.md) — 此异步序列生成的元素类型。
