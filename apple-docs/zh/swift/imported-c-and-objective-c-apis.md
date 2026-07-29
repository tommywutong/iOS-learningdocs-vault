---
title: 导入的 C 与 Objective-C API
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/imported-c-and-objective-c-apis
source_url: 'https://developer.apple.com/documentation/swift/imported-c-and-objective-c-apis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/imported-c-and-objective-c-apis.json'
content_hash: 'sha256:450387353785ed9f'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# 导入的 C 与 Objective-C API

使用原生 Swift 语法与 C 和 Objective-C 中的类型及函数进行互操作（interoperate）。

## 概述

你可以在 Swift 代码中访问和使用用 C 与 Objective-C 编写的代码片段。导入 Objective-C 框架、C 库或头文件后，你就可以使用 Objective-C 类和协议，以及常见的 C 构造、函数和模式。

## 主题

### 同一项目中的 Swift 与 Objective-C

- [将 Objective-C 导入 Swift](importing-objective-c-into-swift.md) —— 在 Swift 中访问 Objective-C 代码中的类及其他声明。
- [将 Swift 导入 Objective-C](importing-swift-into-objective-c.md) —— 在 Objective-C 代码库中访问 Swift 类型及声明。

### Cocoa 框架

- [使用 Foundation 类型](working-with-foundation-types.md) —— 在 Swift 代码库中使用桥接的 Foundation 类型处理日期、时间及其他值。
- [使用 Core Foundation 类型](working-with-core-foundation-types.md) —— 在 Swift 代码中直接使用内存管理的 Core Foundation 类型，并按需手动处理 retain 操作。

### Objective-C API

- [在 Swift 中使用导入的轻量级泛型](using-imported-lightweight-generics-in-swift.md) —— 了解导入的 Objective-C 轻量级泛型类型声明的约束条件。
- [在 Swift 中使用导入的协议限定类](using-imported-protocol-qualified-classes-in-swift.md) —— 了解导入的 Objective-C 协议限定类及元类是如何表示的。

### C API

- [在 Swift 中使用导入的 C 结构体与联合体](using-imported-c-structs-and-unions-in-swift.md) —— 了解 Swift 如何表示导入的 C 结构体与联合体，包括带位域（bitfield）和未命名字段的类型。
- [在 Swift 中使用导入的 C 函数](using-imported-c-functions-in-swift.md) —— 了解如何调用在 C 头文件中声明的导入函数。
- [在 Swift 中使用导入的 C 宏](using-imported-c-macros-in-swift.md) —— 将导入的 C 定义的宏用作常量。

## 另请参阅

### 与 Objective-C 和 C 的语言互操作性

- [Objective-C 与 C 代码自定义](objective-c-and-c-code-customization.md) —— 将宏应用于你的 Objective-C API，以自定义它们被导入 Swift 的方式。
- [将你的 Objective-C 代码迁移到 Swift](migrating-your-objective-c-code-to-swift.md) —— 了解迁移代码的推荐步骤。
- [Cocoa 设计模式](cocoa-design-patterns.md) —— 在你的 Swift App 中采用 Cocoa 设计模式并进行互操作。
- [在 Swift 中处理动态类型的方法和对象](handling-dynamically-typed-methods-and-objects-in-swift.md) —— 将 Objective-C 的 `id` 类型的实例转换为特定的 Swift 类型。
- [在 Swift 中使用 Objective-C 运行时特性](using-objective-c-runtime-features-in-swift.md) —— 使用选择器（selector）和键路径与动态的 Objective-C API 交互。
- [异步调用 Objective-C API](calling-objective-c-apis-asynchronously.md) —— 了解接受完成处理程序（completion handler）的函数和方法是如何转换为 Swift 异步函数的。
