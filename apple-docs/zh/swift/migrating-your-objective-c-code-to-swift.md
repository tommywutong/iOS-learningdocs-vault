---
title: 将你的 Objective-C 代码迁移到 Swift
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/migrating-your-objective-c-code-to-swift
source_url: 'https://developer.apple.com/documentation/swift/migrating-your-objective-c-code-to-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/migrating-your-objective-c-code-to-swift.json'
content_hash: 'sha256:bfe7e95ecced3a1f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md)

# 将你的 Objective-C 代码迁移到 Swift

<sub>文章</sub>

了解迁移代码的推荐步骤。

## 概述

你可以通过用 Swift 替换其中的部分内容，来改进某个 Objective-C App 的架构、逻辑和性能。互操作性使得把已迁移到 Swift 的功能整合进 Objective-C 代码变得毫不费力。你不需要一次性把整个 App 都重写成 Swift。

### 整理你的代码

通过整理和现代化你现有的 Objective-C 代码库，确保你的 Objective-C 代码和 Swift 代码具有最佳的兼容性。例如，如果你的代码库中有些部分还没有添加空性标注，现在就是添加它们的时候。确保你的代码遵循现代编码实践，以便它能更有效地与 Swift 交互。

### 迁移你的代码

将代码迁移到 Swift 的最有效方法是逐文件进行——也就是一次迁移一个类。因为你无法在 Objective-C 中子类化 Swift 类，所以最好选择你 App 中一个没有任何子类的类。你将用一个单独的 `.swift` 文件替换该类的 `.m` 和 `.h` 文件。你实现和接口中的一切内容都直接放进这一个 Swift 文件里。你不需要创建头文件；如果你需要引用它，Xcode 会自动生成一个头文件。

1. 依次选择 File \> New \> File \> (iOS、watchOS、tvOS 或 macOS) \> Source \> Swift File，为你对应的 Objective-C .m 和 .h 文件创建一个 Swift 类。你可以使用与你的 Objective-C 类相同或不同的名称。类前缀在 Swift 中是可选的。
2. 导入相关的系统框架。
3. 如果你需要在 Swift 文件里访问同一个 App target 中的 Objective-C 代码，就填写一个 Objective-C 桥接头文件。
4. 要让你的 Swift 类在 Objective-C 中可访问和可用，把它变成某个 Objective-C 类的后代。要为这个类指定一个在 Objective-C 中使用的特定名称，用 `@objc(`_name_`)` 标记它，其中 name 是你的 Objective-C 代码用来引用这个 Swift 类的名称。

#### 在编写过程中

1. 你可以通过子类化 Objective-C 类、采纳 Objective-C 协议等方式，让你的 Swift 类整合 Objective-C 行为。
2. 在使用 Objective-C API 的过程中，你需要了解 Swift 如何转换某些 Objective-C 语言特性。更多信息，参见 [Objective-C and C Code Customization](objective-c-and-c-code-customization.md)。
3. 必要时使用 `@objc(`_name_`)` 属性为属性和方法提供 Objective-C 名称。
4. 分别用 `func` 和 `class func` 表示实例方法（`-`）和类方法（`+`）。
5. 将简单的宏声明为全局常量，把复杂的宏转换为函数。

#### 完成之后

1. 更新你 Objective-C 代码中的 import 语句（改为 `#import "ProductModuleName-Swift.h"`），使其引用你新写的 Swift 代码。
2. 通过取消勾选 target 成员资格复选框，将原来的 Objective-C `.m` 文件从 target 中移除。不要立刻删除 `.m` 和 `.h` 文件；用它们来排查问题。
3. 如果你给 Swift 类起了不同的名称，就更新你的代码，改用 Swift 类名而不是 Objective-C 名称。

### 故障排查提示与提醒

迁移体验因你现有代码库的不同而不同，但下面是一些通用的步骤和工具，可以帮助你排查这一过程中的问题：

- 记住你无法在 Objective-C 中子类化一个 Swift 类。因此，你迁移的类不能有任何 Objective-C 子类。
- 一旦你将一个类迁移到 Swift，你必须在构建之前把 target 中对应的 `.m` 文件移除，以避免出现重复符号错误。
- 要让一个 Swift 类在 Objective-C 中可用，把它变成某个 Objective-C 类的后代。
- Command-click 一个 Swift 类名，可以查看其生成的头文件。
- Option-click 一个符号，可以查看关于它的隐式信息，比如它的类型、属性和文档注释。

## 另请参阅

### Language Interoperability with Objective-C and C

- [Objective-C and C Code Customization](objective-c-and-c-code-customization.md) — 对你的 Objective-C API 应用宏，自定义它们导入 Swift 的方式。
- [Cocoa Design Patterns](cocoa-design-patterns.md) — 在你的 Swift App 中采纳并与 Cocoa 设计模式互操作。
- [Handling Dynamically Typed Methods and Objects in Swift](handling-dynamically-typed-methods-and-objects-in-swift.md) — 把 Objective-C `id` 类型的实例转换为特定的 Swift 类型。
- [Using Objective-C Runtime Features in Swift](using-objective-c-runtime-features-in-swift.md) — 使用选择器和键路径与动态的 Objective-C API 交互。
- [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md) — 使用原生 Swift 语法与 C 和 Objective-C 中的类型及函数互操作。
- [Calling Objective-C APIs Asynchronously](calling-objective-c-apis-asynchronously.md) — 了解接受完成处理程序的函数和方法是如何被转换为 Swift 异步函数的。
</content>
