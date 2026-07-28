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
doc_path: /documentation/swift/int8/atomicrepresentable-implementations
source_url: 'https://developer.apple.com/documentation/swift/int8/atomicrepresentable-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/atomicrepresentable-implementations.json'
content_hash: 'sha256:6b407ae658badf03'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基础值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Int8](../int8.md)

# AtomicRepresentable 实现

<sub>API 集合</sub>

## 主题

### 类型别名

- [AtomicRepresentation](atomicrepresentation.md) — `Self` 编码与解码所依据的存储表示类型，此类型在用于原子操作时是一种合适的类型。

### 类型方法

- [decodeAtomicRepresentation(_:)](<decodeatomicrepresentation(__).md>) — 通过销毁从原子操作返回的某个 `AtomicRepresentation` 存储实例，恢复逻辑上的原子类型 `Self`。
- [encodeAtomicRepresentation(_:)](<encodeatomicrepresentation(__).md>) — 销毁 `Self` 的一个值，并准备一个用于原子操作的 `AtomicRepresentation` 存储类型。
