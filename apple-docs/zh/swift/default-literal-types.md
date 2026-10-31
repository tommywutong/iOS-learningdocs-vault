---
title: 默认字面量类型
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/default-literal-types
source_url: 'https://developer.apple.com/documentation/swift/default-literal-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/default-literal-types.json'
content_hash: 'sha256:22e20c494bfb9d3b'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Initialization with Literals](initialization-with-literals.md)

# 默认字面量类型

<sub>API 集合</sub>

表示在未提供其他类型信息时字面量所采用的具体类型的类型别名。

## 概述

下面的示例声明了 `numberOfCookies` 常量，用一个整数字面量来表示它的值：

```swift
let numberOfCookies = 5
// type(of: numberOfCookies) == Int.self
```

当字面量表达式在不带任何类型信息的情况下写出时，Swift 会使用这些类型别名来确定该表达式采用的类型。在这个例子中，`numberOfCookies` 常量具有整数字面量的默认类型 `Int`，该类型由 `IntegerLiteralType` 类型别名指定。

## 主题

### 基本值

- [BooleanLiteralType](booleanliteraltype.md) — 在没有其他约束的情况下，布尔字面量采用的默认类型。
- [IntegerLiteralType](integerliteraltype.md) — 在没有其他约束的情况下，整数字面量采用的默认类型。
- [FloatLiteralType](floatliteraltype.md) — 在没有其他约束的情况下，浮点字面量采用的默认类型。

### 字符串与文本

- [StringLiteralType](stringliteraltype.md) — 在没有其他约束的情况下，字符串字面量采用的默认类型。
- [ExtendedGraphemeClusterType](extendedgraphemeclustertype.md) — 在没有其他约束的情况下，Unicode 扩展字素簇字面量采用的默认类型。
- [UnicodeScalarType](unicodescalartype.md) — 在没有其他约束的情况下，Unicode 标量字面量采用的默认类型。
