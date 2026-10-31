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
doc_path: /documentation/swift/unsaferawpointer/atomicoptionalrepresentable-implementations
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/atomicoptionalrepresentable-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/atomicoptionalrepresentable-implementations.json'
content_hash: 'sha256:064b8c2a892bdd66'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [手动内存管理](../manual-memory-management.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# AtomicOptionalRepresentable 实现

<sub>API 集合</sub>

## 主题

### 类型别名

- [AtomicOptionalRepresentation](atomicoptionalrepresentation.md) — 与 `Optional<Self>` 相互编码和解码的存储表示类型，适合在对 `Optional` 的原子操作中使用。

### 类型方法

- [decodeAtomicOptionalRepresentation(_:)](<decodeatomicoptionalrepresentation(__).md>) — 通过销毁某个由对 `Optional` 的原子操作返回的 `AtomicOptionalRepresentation` 存储实例，恢复逻辑原子类型 `Self?`。
- [encodeAtomicOptionalRepresentation(_:)](<encodeatomicoptionalrepresentation(__).md>) — 销毁一个 `Self` 值，并准备一个用于对 `Optional` 的原子操作的 `AtomicOptionalRepresentation` 存储类型。
