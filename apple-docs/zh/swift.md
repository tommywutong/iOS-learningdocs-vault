---
title: Swift
framework: Swift
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift
source_url: 'https://developer.apple.com/documentation/swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift.json'
content_hash: 'sha256:e6f1017a48a98856'
translated: true
---

> 导航：[技术](technologies.md)

# Swift

<sub>框架</sub>

使用一门强大的开放语言来构建 App。

## 概述

Swift 包含类型推断、可选值和闭包（closure）等现代特性，使语法简洁而富有表现力。Swift 确保你的代码快速高效，同时其内存安全性和原生的错误处理机制让这门语言在设计上就是安全的。在 Swift Playgrounds、Xcode 中的 playground 以及 REPL 里编写 Swift 代码是互动而有趣的。

```swift
var interestingNumbers = [
    "primes": [2, 3, 5, 7, 11, 13, 17],
    "triangular": [1, 3, 6, 10, 15, 21, 28],
    "hexagonal": [1, 6, 15, 28, 45, 66, 91]
]

for key in interestingNumbers.keys {
    interestingNumbers[key]?.sort(by: >)
}

print(interestingNumbers["primes"]!)
// 输出 "[17, 13, 11, 7, 5, 3, 2]"
```

### 学习 Swift

如果你是 Swift 新手，请阅读 [The Swift Programming Language](https://docs.swift.org/swift-book/)，其中包含快速导览、全面的语言指南和完整的参考手册。如果你是编程新手，可以在 iPad 上试试 [Swift Playgrounds](https://www.apple.com/swift/playgrounds/)。

Swift 以开放的方式开发。要进一步了解 Swift 开源项目和社区，请访问 [Swift.org](https://swift.org)。

## 主题

### 基础

- [Swift 更新](updates/swift.md) — 了解 Swift 的重要变更。
- [在 Swift 6 App 中采用严格并发](swift/adoptingswift6.md) — 启用严格并发检查，在编译期找出数据争用（data race）。

### 标准库

- [Int](swift/int.md) — 一个有符号整数值类型。
- [Double](swift/double.md) — 一个双精度（64 位）浮点值类型。
- [String](swift/string.md) — 一个 Unicode 字符串值，是字符的集合。
- [Array](swift/array.md) — 一个有序、可随机访问的集合。
- [Dictionary](swift/dictionary.md) — 一个元素为键值对的集合。
- [Swift 标准库](swift/swift-standard-library.md) — 解决复杂问题，编写高性能、可读性好的代码。

### 观察

- [Observation](observation.md) — 构建响应式的 App，在底层数据变化时更新呈现。

### 分布式 Actor

- [Distributed](distributed.md) — 构建跨多个进程和设备运行分布式代码的系统。

### 正则表达式 DSL

- [RegexBuilder](regexbuilder.md) — 使用表达力强的领域特定语言构建正则表达式，用于在文本中搜索和替换等操作。

### 底层原子操作

- [Synchronization](synchronization.md) — 使用底层的原语操作构建同步构造。

### 数据建模

- [在结构体和类之间做选择](swift/choosing-between-structures-and-classes.md) — 决定如何存储数据并建模行为。
- [采用常用协议](swift/adopting-common-protocols.md) — 确保你的自定义类型符合 Swift 协议，让它们更易于使用。

### 数据流与控制流

- [在 App 中维护状态](swift/maintaining-state-in-your-apps.md) — 使用枚举来捕获和跟踪你的 App 的状态。
- [使用闭包时避免时序问题](swift/preventing-timing-problems-when-using-closures.md) — 理解对闭包的不同 API 调用会如何影响你的 App。

### 与 Objective-C 和 C 的语言互操作性

- [Objective-C 和 C 代码自定义](swift/objective-c-and-c-code-customization.md) — 将宏应用到你的 Objective-C API，以自定义它们导入 Swift 的方式。
- [将你的 Objective-C 代码迁移到 Swift](swift/migrating-your-objective-c-code-to-swift.md) — 了解迁移你的代码的推荐步骤。
- [Cocoa 设计模式](swift/cocoa-design-patterns.md) — 在你的 Swift App 中采用 Cocoa 设计模式并与之互操作。
- [在 Swift 中处理动态类型的方法和对象](swift/handling-dynamically-typed-methods-and-objects-in-swift.md) — 将 Objective-C `id` 类型的实例转换为特定的 Swift 类型。
- [在 Swift 中使用 Objective-C 运行时特性](swift/using-objective-c-runtime-features-in-swift.md) — 使用选择器（selector）和键路径与动态的 Objective-C API 交互。
- [导入的 C 和 Objective-C API](swift/imported-c-and-objective-c-apis.md) — 使用原生 Swift 语法与 C 和 Objective-C 中的类型和函数互操作。
- [异步调用 Objective-C API](swift/calling-objective-c-apis-asynchronously.md) — 了解接受完成处理程序（completion handler）的函数和方法如何被转换为 Swift 异步函数。

### 与 C++ 的语言互操作性

- [在 Xcode 项目中混用多种语言](swift/mixinglanguagesinanxcodeproject.md) — 在单一框架 target 中于 Swift 里使用 C++ API（以及在 C++ 里使用 Swift API），并在单独的 App target 中使用该框架的 API。
- [跨语言边界调用 API](swift/callingapisacrosslanguageboundaries.md) — 在 Xcode 项目的多个 target 和框架中，于 Swift 里使用各种 C++ API，反之亦然。
