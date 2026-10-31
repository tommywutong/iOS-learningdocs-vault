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
doc_path: /documentation/swift/unsafemutablebufferpointer/bidirectionalcollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/bidirectionalcollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/bidirectionalcollection-implementations.json'
content_hash: 'sha256:e0fc01dd96cce8e8'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# BidirectionalCollection 实现

<sub>API 集合</sub>

## 主题

### 实例属性

- [last](last.md) — 集合的最后一个元素。

### 实例方法

- [difference(from:)](<difference(from_).md>) — 返回通过给定集合得到此集合有序元素所需的差异。
- [difference(from:by:)](<difference(from_by_).md>) — 返回通过给定集合得到此集合有序元素所需的差异，并使用给定谓词作为等价性测试。
- [dropLast(_:)](<droplast(__)-7846m.md>) — 返回一个子序列，其中包含除末尾指定数量元素之外的所有元素。
- [formIndex(before:)](<formindex(before_).md>) — 将给定索引替换为其前驱索引。
- [index(before:)](<index(before_).md>) — 返回紧邻给定索引之前的位置。
- [joined(separator:)](<joined(separator_)-5do13.md>) — 通过拼接序列的元素返回一个新字符串，并在每个元素之间添加给定的分隔符。
- [last(where:)](<last(where_).md>) — 返回序列中满足给定谓词的最后一个元素。
- [lastIndex(of:)](<lastindex(of_).md>) — 返回集合中出现指定值的最后一个索引。
- [lastIndex(where:)](<lastindex(where_).md>) — 返回集合中最后一个匹配给定谓词的元素的索引。
- [reversed()](<reversed()-3wn5k.md>) — 返回一个按相反顺序呈现集合元素的视图。
- [suffix(_:)](<suffix(__)-3w6rj.md>) — 返回一个最大不超过给定长度的子序列，其中包含集合的末尾元素。
