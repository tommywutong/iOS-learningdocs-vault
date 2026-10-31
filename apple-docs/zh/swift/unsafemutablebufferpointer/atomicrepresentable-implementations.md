---
title: AtomicRepresentable 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablebufferpointer/atomicrepresentable-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/atomicrepresentable-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/atomicrepresentable-implementations.json'
content_hash: 'sha256:3774ec472412b59e'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# AtomicRepresentable 实现

<sub>API 集合</sub>

## 主题

### 类型别名

- [AtomicRepresentation](atomicrepresentation.md) — `Self` 编码到和解码自的存储表示类型，适合在原子操作中使用。

### 类型方法

- [decodeAtomicRepresentation(_:)](<decodeatomicrepresentation(__).md>) — 通过销毁某个由原子操作返回的 `AtomicRepresentation` 存储实例，恢复逻辑原子类型 `Self`。
- [encodeAtomicRepresentation(_:)](<encodeatomicrepresentation(__).md>) — 销毁一个 `Self` 值，并准备一个用于原子操作的 `AtomicRepresentation` 存储类型。
