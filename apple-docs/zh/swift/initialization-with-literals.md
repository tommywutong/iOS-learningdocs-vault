---
title: 使用字面量初始化
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/initialization-with-literals
source_url: 'https://developer.apple.com/documentation/swift/initialization-with-literals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/initialization-with-literals.json'
content_hash: 'sha256:272543f9444efb50'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 使用字面量初始化

<sub>API 集合</sub>

让你的类型的值可以用不同种类的字面量来表达。

## 主题

### 集合字面量

- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md) — 可以使用数组字面量初始化的类型。
- [ExpressibleByDictionaryLiteral](expressiblebydictionaryliteral.md) — 可以使用字典字面量初始化的类型。

### 值字面量

- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md) — 可以用整数字面量初始化的类型。
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md) — 可以用浮点数字面量初始化的类型。
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md) — 可以用布尔字面量 `true` 和 `false` 初始化的类型。
- [ExpressibleByNilLiteral](expressiblebynilliteral.md) — 可以使用 nil 字面量 `nil` 初始化的类型。
- [StaticBigInt](staticbigint.md) — 一个不可变的任意精度有符号整数。

### 字符串字面量

- [ExpressibleByStringLiteral](expressiblebystringliteral.md) — 可以用字符串字面量初始化的类型。
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md) — 可以用包含单个扩展字素簇（extended grapheme cluster）的字符串字面量初始化的类型。
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md) — 可以用包含单个 Unicode 标量值的字符串字面量初始化的类型。
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md) — 可以通过对包含表达式的字符串字面量进行字符串插值来初始化的类型。
- [StringInterpolationProtocol](stringinterpolationprotocol.md) — 在构建过程中表示带插值的字符串字面量的内容。
- [DefaultStringInterpolation](defaultstringinterpolation.md) — 在构建过程中表示带插值的字符串字面量的内容。

### 字面量的默认类型

- [Default Literal Types](default-literal-types.md) — 表示在未提供其他类型信息时字面量所采用的具体类型的类型别名。

## 另请参阅

### 你的类型的工具

- [基本行为](basic-behaviors.md) — 在依赖相等或顺序测试的运算中使用你的自定义类型，并把它们用作集合和字典的成员。
- [编码、解码与序列化](encoding-decoding-and-serialization.md) — 使用隐式或自定义的编码来序列化和反序列化你的类型的实例。
