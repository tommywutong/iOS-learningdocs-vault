---
title: 托管缓冲区
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managed-buffers
source_url: 'https://developer.apple.com/documentation/swift/managed-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managed-buffers.json'
content_hash: 'sha256:aba950ded852a0ab'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [集合](collections.md)

# 托管缓冲区

<sub>API 集合</sub>

构建你自己的基于缓冲区的集合类型。

## 主题

### 缓冲区实现

- [ManagedBuffer](managedbuffer.md) — 一个类，其实例包含一个 `Header` 类型的属性和用于 `Element` 数组的原始存储，其大小在实例创建时确定。
- [ManagedBufferPointer](managedbufferpointer.md) — 包含一个缓冲区对象，并提供对 `Header` 实例以及存储在该缓冲区中的任意数量 `Element` 实例的连续存储的访问。

### 唯一性检查

- [isKnownUniquelyReferenced(_:)](<isknownuniquelyreferenced(__)-98zpp.md>) — 返回一个布尔值，指示给定对象是否已知仅有一个强引用。
- [isKnownUniquelyReferenced(_:)](<isknownuniquelyreferenced(__)-5kvtu.md>) — 返回一个布尔值，指示给定对象是否已知仅有一个强引用。

## 另请参阅

### 高级集合主题

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md) — 编写适用于任意集合的通用代码，或构建你自己的集合类型。
- [Supporting Types](supporting-types.md) — 在对集合进行切片、展平和反转等操作时，使用包装器、索引和迭代器。
