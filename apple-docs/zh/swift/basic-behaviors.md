---
title: 基本行为
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/basic-behaviors
source_url: 'https://developer.apple.com/documentation/swift/basic-behaviors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/basic-behaviors.json'
content_hash: 'sha256:c2e73490ca036e81'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# 基本行为

<sub>API 集合</sub>

在依赖相等性或顺序判断的操作中使用你的自定义类型，并将其用作集合与字典的成员。

## 主题

### 相等与排序

- [Equatable](equatable.md) — 一种可以进行值相等比较的类型。
- [Comparable](comparable.md) — 一种可以使用关系运算符 `<`、`<=`、`>=` 和 `>` 进行比较的类型。
- [Identifiable](identifiable.md) — 一类类型，其实例持有具有稳定身份的实体的值。

### 复制

- [Copyable](copyable.md) — 一种其值可以被隐式或显式复制的类型。
- [BitwiseCopyable](bitwisecopyable.md)
- [Escapable](escapable.md) — 一种其值可以在其直接局部作用域之外继续存在的类型。

### Borrowing

- [Ref](ref.md) — 一种安全的引用，允许对共享值进行就地读取。 _(beta)_
- [MutableRef](mutableref.md) — 一种安全的可变引用，允许对独占值进行就地修改。 _(beta)_

### 集合与字典

- [Hashable](hashable.md) — 一种可以散列到 `Hasher` 中以产生整数哈希值的类型。
- [Hasher](hasher.md) — `Set` 和 `Dictionary` 所使用的通用哈希函数。

### 字符串表示

- [CustomStringConvertible](customstringconvertible.md) — 一种具有自定文本表示的类型。
- [LosslessStringConvertible](losslessstringconvertible.md) — 一种可以无损且无歧义地表示为字符串的类型。
- [CustomDebugStringConvertible](customdebugstringconvertible.md) — 一种具有适合调试用途的自定文本表示的类型。

### 原始值表示

- [CaseIterable](caseiterable.md) — 一种提供其所有值的集合的类型。
- [RawRepresentable](rawrepresentable.md) — 一种可以在关联的原始值之间来回转换的类型。

## 另请参阅

### 用于你的类型的工具

- [Encoding, Decoding, and Serialization](encoding-decoding-and-serialization.md) — 使用隐式或自定编码对你的类型的实例进行序列化和反序列化。
- [Initialization with Literals](initialization-with-literals.md) — 允许你的类型的值用不同种类的字面量来表达。
