---
title: MutableCollection 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations.json'
content_hash: 'sha256:3c6c315723539bb2'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Manual Memory Management](../manual-memory-management.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# MutableCollection 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [moveSubranges(_:to:)](<movesubranges(__to_).md>) — 将给定子范围内的元素移动到指定位置上元素之前。
- [partition(by:)](<partition(by_)-33su4.md>) — 重新排列集合中的元素，使所有匹配给定谓词的元素都排在所有不匹配的元素之后。
- [partition(by:)](<partition(by_)-90pny.md>) — 重新排列集合中的元素，使所有匹配给定谓词的元素都排在所有不匹配的元素之后。
- [reverse()](<reverse().md>) — 就地反转集合中的元素。
- [shuffle()](<shuffle().md>) — 就地打乱集合。
- [shuffle(using:)](<shuffle(using_).md>) — 就地打乱集合，使用给定的生成器作为随机源。
- [sort()](<sort().md>) — 就地对集合排序。
- [sort(by:)](<sort(by_).md>) — 就地对集合排序，使用给定谓词作为元素间的比较。
- [swapAt(_:_:)](<swapat(____).md>) — 交换此缓冲区内存中指定索引处的字节值。
- [withContiguousMutableStorageIfAvailable(_:)](<withcontiguousmutablestorageifavailable(__).md>) — 在集合的连续存储上执行一个闭包。

### 下标

- [subscript(_:)](<subscript(__)-3g42.md>) — 访问集合元素的连续子范围。
- [subscript(_:)](<subscript(__)-3i1y.md>) — 访问集合元素的连续子范围。 _(已废弃)_
- [subscript(_:)](<subscript(__)-3kwnc.md>)
- [subscript(_:)](<subscript(__)-3pmfu.md>)
- [subscript(_:)](<subscript(__)-9v9lo.md>) _(已废弃)_
- [subscript(_:)](<subscript(__)-u791.md>) — 以 `UInt8` 值的形式访问内存区域中给定偏移量处的字节。
- [subscript(_:)](<subscript(__)-znv7.md>) — 访问指定内存区域中的字节。
