---
title: 支持类型
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/supporting-types
source_url: 'https://developer.apple.com/documentation/swift/supporting-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/supporting-types.json'
content_hash: 'sha256:0cf9790e18d0c612'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [集合](collections.md)

# 支持类型

<sub>API 集合</sub>

在切片、展平和反转集合等操作中使用包装器、索引和迭代器。

## 主题

### 切片

- [Slice](slice.md) — 一个用于查看另一个集合中元素子序列的视图。

### 范围表达式

- [PartialRangeUpTo](partialrangeupto.md) — 一个部分半开区间，止于但不包含某个上界。
- [PartialRangeThrough](partialrangethrough.md) — 一个部分区间，止于并包含某个上界。
- [PartialRangeFrom](partialrangefrom.md) — 一个部分区间，从某个下界向上延伸。
- [RangeExpression](rangeexpression.md) — 一种可用于对集合进行切片的类型。
- [UnboundedRange_](unboundedrange_.md) — 一种表示集合整个范围的范围表达式。

### 类型擦除包装器

- [AnySequence](anysequence.md) — 一个类型擦除的序列。
- [AnyCollection](anycollection.md) — 一种类型擦除的包装器，适用于任何索引支持前向遍历的集合。
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — 一种类型擦除的包装器，适用于任何索引支持双向遍历的集合。
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — 一种类型擦除的包装器，适用于任何索引支持随机访问遍历的集合。
- [AnyIterator](anyiterator.md) — 一个 `Element` 的类型擦除迭代器。
- [AnyIndex](anyindex.md) — 一个包装底层索引的包装器，隐藏了具体的底层类型。
- [AnyHashable](anyhashable.md) — 一个类型擦除的可哈希值。

### 惰性包装器

- [LazySequence](lazysequence.md) — 一个序列，包含与某个 `Base` 序列相同的元素，但一些操作（例如 `map` 和 `filter`）是以惰性方式实现的。
- [LazyMapSequence](lazymapsequence.md) — 一个 `Sequence`，其元素由某个 `Base` `Sequence` 中的元素经过一个返回 `Element` 的转换函数得到。这些元素以惰性方式计算，每次读取时都会对某个基础元素调用该转换函数。
- [LazyFilterSequence](lazyfiltersequence.md) — 一个序列，其元素由某个基础序列中同时满足给定谓词的元素组成。
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md) — 一个序列，其元素由某个基础序列中开头连续满足给定谓词的元素组成。
- [LazyDropWhileSequence](lazydropwhilesequence.md) — 一个序列，其元素由某个基础序列中开头连续满足给定谓词的元素之后的那些元素组成。
- [LazyCollection](lazycollection.md) — 一个集合，包含与某个 `Base` 集合相同的元素，但一些操作（例如 `map` 和 `filter`）是以惰性方式实现的。
- [LazyDropWhileCollection](lazydropwhilecollection.md) — 一个惰性包装器，包含底层集合中开头连续满足谓词的元素之后的元素。
- [LazyFilterCollection](lazyfiltercollection.md) — 一个惰性 `Collection` 包装器，包含底层集合中满足谓词的元素。
- [LazyMapCollection](lazymapcollection.md) — 一个 `Collection`，其元素由某个 `Base` `Collection` 中的元素经过一个返回 `Element` 的转换函数得到。这些元素以惰性方式计算，每次读取时都会对某个基础元素调用该转换函数。
- [LazyPrefixWhileCollection](lazyprefixwhilecollection.md) — 一个惰性集合包装器，包含底层集合中开头连续满足谓词的元素。

### 算法包装器

- [CollectionDifference](collectiondifference.md) — 一个由插入和移除组成的集合，描述两个有序集合状态之间的差异。
- [DropFirstSequence](dropfirstsequence.md) — 一个序列，在可能返回第一个可用元素之前，以惰性方式从底层 `Base` 迭代器中消费并丢弃 `n` 个元素。
- [DropWhileSequence](dropwhilesequence.md) — 一个序列，在可能返回第一个可用元素之前，以惰性方式从底层 `Base` 迭代器中消费并丢弃 `n` 个元素。
- [EnumeratedSequence](enumeratedsequence.md) — 一个序列或集合中元素的枚举。
- [FlattenCollection](flattencollection.md)
- [FlattenSequence](flattensequence.md) — 一个序列，由某个 `Base` 序列所包含的每个分段中的所有元素组成。
- [JoinedSequence](joinedsequence.md) — 一个序列，呈现使用给定分隔符连接某个基础序列组成的序列中的元素。
- [PrefixSequence](prefixsequence.md) — 一个序列，仅从底层 `Base` 迭代器中消费最多 `n` 个元素。
- [Repeated](repeated.md) — 一个元素完全相同的集合。
- [ReversedCollection](reversedcollection.md) — 一个以相反顺序呈现其基础集合元素的集合。
- [StrideTo](strideto.md) — 一个由跨越半开区间得到的值组成的序列。
- [StrideThrough](stridethrough.md) — 一个由跨越闭区间得到的值组成的序列。
- [UnfoldSequence](unfoldsequence.md) — 一个序列，其元素通过对某个可变状态反复应用闭包来产生。
- [Zip2Sequence](zip2sequence.md) — 一个由两个底层序列构建的对偶序列。

### 索引集合

- [DefaultIndices](defaultindices.md) — 一个适用于任意集合的索引集合

### 索引与迭代器

- [IteratorSequence](iteratorsequence.md) — 一个围绕 `Base` 类型的迭代器构建的序列。
- [IndexingIterator](indexingiterator.md) — 一种使用集合自身索引在其上进行迭代的类型。
- [EnumeratedIterator](enumeratediterator.md)
- [SetIterator](setiterator.md)
- [StrideThroughIterator](stridethroughiterator.md) — 一个 `StrideThrough` 实例的迭代器。
- [StrideToIterator](stridetoiterator.md) — 一个 `StrideTo` 实例的迭代器。

### 已废弃

- [DictionaryIndex](dictionaryindex.md)
- [SetIndex](setindex.md)
- [CountableClosedRange](countableclosedrange.md)
- [CountablePartialRangeFrom](countablepartialrangefrom.md)
- [CountableRange](countablerange.md)

## 另请参阅

### 高级集合主题

- [序列与集合协议](sequence-and-collection-protocols.md) — 编写可作用于任何集合的泛型代码，或构建你自己的集合类型。
- [托管缓冲区](managed-buffers.md) — 构建你自己的基于缓冲区的集合类型。
