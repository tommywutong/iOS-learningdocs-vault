---
title: BidirectionalCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/bidirectionalcollection-implementations.json'
content_hash: 'sha256:e27de79dbe82cdfc'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# BidirectionalCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [last](last.md) — 集合的最后一个元素。

### 实例方法

- [difference(from:)](<difference(from_).md>) — 返回从给定集合产生此集合的有序元素所需的差异。
- [difference(from:by:)](<difference(from_by_).md>) — 返回从给定集合产生此集合的有序元素所需的差异，并使用给定的谓词作为等价性测试。
- [dropLast(_:)](<droplast(__).md>) — 返回一个子序列，包含除末尾指定数量元素之外的所有元素。
- [formIndex(before:)](<formindex(before_).md>) — 用其前驱位置替换给定的索引。
- [last(where:)](<last(where_).md>) — 返回序列中满足给定谓词的最后一个元素。
- [lastIndex(of:)](<lastindex(of_).md>) — 返回指定值在集合中最后一次出现的索引。
- [lastIndex(where:)](<lastindex(where_).md>) — 返回集合中匹配给定谓词的最后一个元素的索引。
- [reversed()](<reversed().md>) — 返回一个按逆序呈现集合元素的视图。
- [suffix(_:)](<suffix(__).md>) — 返回一个子序列，包含集合末尾的元素，长度不超过给定的最大长度。
