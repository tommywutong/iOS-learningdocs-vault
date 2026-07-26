---
title: 序列与集合协议
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sequence-and-collection-protocols
source_url: 'https://developer.apple.com/documentation/swift/sequence-and-collection-protocols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence-and-collection-protocols.json'
content_hash: 'sha256:010f2e1b35388741'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [集合](collections.md)

# 序列与集合协议

<sub>API 集合</sub>

编写适用于任何集合的泛型代码，或者构建你自己的集合类型。

## 主题

### 第一步

- [Sequence](sequence.md) — 一种提供对其元素进行顺序、迭代访问的类型。
- [Collection](collection.md) — 一种序列，其元素可以被多次、非破坏性地遍历，并可以通过带索引的下标访问。

### 集合遍历

- [BidirectionalCollection](bidirectionalcollection.md) — 一种既支持向后遍历、也支持向前遍历的集合。
- [RandomAccessCollection](randomaccesscollection.md) — 一种支持高效随机访问索引遍历的集合。

### 集合可变性

- [MutableCollection](mutablecollection.md) — 一种支持下标赋值的集合。
- [RangeReplaceableCollection](rangereplaceablecollection.md) — 一种支持用另一个集合的元素替换任意子范围元素的集合。

### 手动迭代

- [IteratorProtocol](iteratorprotocol.md) — 一种逐个提供序列中值的类型。
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md) — 一种为借用序列的值提供借用访问的类型。_(beta)_
- [BorrowingIteratorAdapter](borrowingiteratoradapter.md) _(beta)_
- [BorrowingSequence](borrowingsequence.md) — 一种为其元素提供顺序、借用访问的类型。_(beta)_

### 代数集合

- [SetAlgebra](setalgebra.md) — 一种提供数学集合运算的类型。

### 惰性集合

- [LazySequenceProtocol](lazysequenceprotocol.md) — 一种序列，其上原本会立即执行的序列操作会以惰性方式实现。
- [LazyCollectionProtocol](lazycollectionprotocol.md)

## 另请参阅

### 集合进阶主题

- [支持类型](supporting-types.md) — 在切片、展平和反转集合等操作中使用包装器、索引和迭代器。
- [托管缓冲区](managed-buffers.md) — 构建你自己的、由缓冲区支持的集合类型。
