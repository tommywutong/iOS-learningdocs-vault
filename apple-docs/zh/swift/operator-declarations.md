---
title: 运算符声明
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/operator-declarations
source_url: 'https://developer.apple.com/documentation/swift/operator-declarations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/operator-declarations.json'
content_hash: 'sha256:71f16857abfe6c6d'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 运算符声明

<sub>文章</sub>

使用前缀、后缀和中缀运算符。

## 概述

下表列出了 Swift 标准库声明的运算符。有关运算符声明的更多信息，请参阅《[The Swift Programming Language](https://docs.swift.org/swift-book/)》中的 [Operator Declaration](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Operator-Declaration)。

前缀运算符如下：

| 运算符 | 描述 |
|---|---|
| `!` | 逻辑非 |
| `.!` | 逐点逻辑非 |
| `~` | 按位非 |
| `+` | 一元加号 |
| `-` | 一元减号 |
| `..<` | 半开区间 |
| `...` | 闭区间 |

后缀运算符如下：

| 运算符 | 描述 |
|---|---|
| `...` | 范围 |

下文的中缀运算符按优先级组分组，并按优先级从高到低排列。如果你在声明新运算符时未指定优先级组，它将属于 `DefaultPrecedence` 优先级组。`DefaultPrecedence` 不具有结合性，其优先级紧高于 `TernaryPrecedence`。

`BitwiseShiftPrecedence` 组不具有结合性，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `<<` | 按位左移 |
| `>>` | 按位右移 |
| `&<<` | 按位左移，忽略溢出 |
| `&>>` | 按位右移，忽略溢出 |

`MultiplicationPrecedence` 组为左结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `*` | 相乘 |
| `/` | 相除 |
| `%` | 求余 |
| `&` | 按位与 |
| `&*` | 带溢出的相乘 |

`AdditionPrecedence` 组为左结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `+` | 相加 |
| `-` | 相减 |
| `\|` | 按位或 |
| `^` | 按位异或 |
| `&+` | 带溢出的相加 |
| `&-` | 带溢出的相减 |

`RangeFormationPrecedence` 组不具有结合性，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `..<` | 半开区间 |
| `...` | 闭区间 |

`CastingPrecedence` 组为左结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `is` | 类型检查 |
| `as`, `as?`, and `as!` | 类型转换 |

`NilCoalescingPrecedence` 组为右结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `??` | nil 合并 |

`ComparisonPrecedence` 组不具有结合性，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `<` | 小于 |
| `<=` | 小于或等于 |
| `>` | 大于 |
| `>=` | 大于或等于 |
| `==` | 等于 |
| `!=` | 不等于 |
| `===` | 同一（identical） |
| `!==` | 非同一（not identical） |
| `~=` | 模式匹配 |
| `.<` | 逐点小于 |
| `.<=` | 逐点小于或等于 |
| `.>` | 逐点大于 |
| `.>=` | 逐点大于或等于 |
| `.==` | 逐点等于 |
| `.!=` | 逐点不等于 |

`LogicalConjunctionPrecedence` 组为左结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `&&` | 逻辑与 |
| `.&` | 逐点按位与 |

`LogicalDisjunctionPrecedence` 组为左结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `\|\|` | 逻辑或 |
| `.\|` | 逐点按位或 |
| `.^` | 逐点按位异或 |

`TernaryPrecedence` 组为右结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `?` `:` | 三元条件 |

`AssignmentPrecedence` 组为右结合，包含以下中缀运算符：

| 运算符 | 描述 |
|---|---|
| `=` | 赋值 |
| `*=` | 相乘并赋值 |
| `/=` | 相除并赋值 |
| `%=` | 求余并赋值 |
| `+=` | 相加并赋值 |
| `-=` | 相减并赋值 |
| `<<=` | 按位左移并赋值 |
| `>>=` | 按位右移并赋值 |
| `&=` | 按位与并赋值 |
| `\|=` | 按位或并赋值 |
| `^=` | 按位异或并赋值 |
| `&*=` | 带溢出的相乘并赋值 |
| `&+=` | 带溢出的相加并赋值 |
| `&-=` | 带溢出的相减并赋值 |
| `&<<=` | 忽略溢出的按位左移并赋值 |
| `&>>=` | 忽略溢出的按位右移并赋值 |
| `.&=` | 逐点按位与并赋值 |
| `.\|=` | 逐点按位或并赋值 |
| `.^=` | 逐点按位异或并赋值 |

## 另请参阅

### 编程任务

- [输入与输出](input-and-output.md) — 将值打印到控制台，从文本流读取和写入，并使用命令行参数。
- [调试与反射](debugging-and-reflection.md) — 使用运行时检查强化你的代码，并检查你的值的运行时表示。
- [宏](macros.md) — 生成样板代码并执行其他编译期操作。
- [并发](concurrency.md) — 执行异步和并行操作。
- [键路径表达式](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [手动内存管理](manual-memory-management.md) — 手动分配和管理内存。
- [类型转换与既存类型](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [C 互操作性](c-interoperability.md) — 使用导入的 C 类型或调用 C 可变参数函数。
