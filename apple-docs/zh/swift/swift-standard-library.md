---
title: Swift 标准库
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/swift-standard-library
source_url: 'https://developer.apple.com/documentation/swift/swift-standard-library'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/swift-standard-library.json'
content_hash: 'sha256:22e1ba846ae61d13'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# Swift 标准库

解决复杂问题，编写高性能、可读性强的代码。

## 概述

Swift 标准库为编写 Swift 程序定义了一个基础功能层，包括：

- 基础数据类型，例如 [Int](int.md)、[Double](double.md) 和 [String](string.md)
- 常见数据结构，例如 [Array](array.md)、[Dictionary](dictionary.md) 和 [Set](set.md)
- 全局函数，例如 [print(_:separator:terminator:)](<print(__separator_terminator_).md>) 和 [abs(_:)](<abs(__).md>)
- 描述常见抽象的协议，例如 [Collection](collection.md) 和 [Equatable](equatable.md)。
- 用于自定可供所有类型使用的操作的协议，例如 [CustomDebugStringConvertible](customdebugstringconvertible.md) 和 [CustomReflectable](customreflectable.md)。
- 用于提供原本需要样板代码的实现的协议，例如 [OptionSet](optionset.md)。

> [!note] 注意
> 借助可视化和实际示例来试验 Swift 标准库类型并学习高级概念。了解 Swift 标准库如何使用协议和泛型来表达强大的约束。下载下面的 playground 即可开始。
>
> [Swift Standard Library.playground](https://developer.apple.com/sample-code/swift/downloads/standard-library.zip)

## 主题

### 值与集合

- [数字与基本值](numbers-and-basic-values.md) — 使用数字、布尔值和其他基础类型为数据建模。
- [字符串与文本](strings-and-text.md) — 使用 Unicode 安全的字符串处理文本。
- [集合](collections.md) — 使用数组、字典、集合和其他数据结构来存储和组织数据。
- [时间](time-and-duration.md) — 测量一次操作耗费的时长，并确定未来的时间安排。

### 你的类型可用的工具

- [基本行为](basic-behaviors.md) — 在依赖相等性或顺序判断的操作中使用你的自定义类型，并将其用作集合与字典的成员。
- [编码、解码与序列化](encoding-decoding-and-serialization.md) — 通过隐式或自定义编码对你的类型的实例进行序列化和反序列化。
- [用字面量初始化](initialization-with-literals.md) — 允许使用不同种类的字面量来表达你的类型的值。

### 编程任务

- [输入与输出](input-and-output.md) — 将值打印到控制台，从文本流中读取和写入，并使用命令行参数。
- [调试与反射](debugging-and-reflection.md) — 使用运行时检查强化你的代码，并检查你的值的运行时表示。
- [宏](macros.md) — 生成样板代码，并执行其他编译期操作。
- [并发](concurrency.md) — 执行异步和并行操作。
- [键路径表达式](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [手动内存管理](manual-memory-management.md) — 手动分配和管理内存。
- [类型转换与既存类型](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [C 互操作性](c-interoperability.md) — 使用导入的 C 类型，或调用 C 可变参数函数。
- [运算符声明](operator-declarations.md) — 使用前缀、后缀和中缀运算符。

### 已废弃

- [已废弃](deprecated.md)

## 另请参阅

### 标准库

- [Int](int.md) — 一个有符号整数值类型。
- [Double](double.md) — 一个双精度（64 位）浮点值类型。
- [String](string.md) — 一个 Unicode 字符串值，是字符的集合。
- [Array](array.md) — 一个有序的随机访问集合。
- [Dictionary](dictionary.md) — 一个元素为键值对的集合。
