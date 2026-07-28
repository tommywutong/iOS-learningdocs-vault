---
title: AtomicOptionalRepresentable 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafepointer/atomicoptionalrepresentable-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/atomicoptionalrepresentable-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/atomicoptionalrepresentable-implementations.json'
content_hash: 'sha256:39ef19a9bfbd81a3'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafePointer](../unsafepointer.md)

# AtomicOptionalRepresentable 实现

<sub>API 集合</sub>

## 主题

### 类型别名

- [AtomicOptionalRepresentation](atomicoptionalrepresentation.md) — 一种存储表示类型，可编码为 `Optional<Self>` 并从中解码，适合用于 `Optional` 的原子操作。

### 类型方法

- [decodeAtomicOptionalRepresentation(_:)](<decodeatomicoptionalrepresentation(__).md>) — 通过销毁从对 `Optional` 的原子操作返回的某个 `AtomicOptionalRepresentation` 存储实例，恢复逻辑原子类型 `Self?`。
- [encodeAtomicOptionalRepresentation(_:)](<encodeatomicoptionalrepresentation(__).md>) — 销毁 `Self` 的一个值，并准备一个 `AtomicOptionalRepresentation` 存储类型，用于对 `Optional` 执行原子操作。
