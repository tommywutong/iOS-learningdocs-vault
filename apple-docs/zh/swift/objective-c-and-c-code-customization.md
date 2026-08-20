---
title: Objective-C 与 C 代码自定义
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/objective-c-and-c-code-customization
source_url: 'https://developer.apple.com/documentation/swift/objective-c-and-c-code-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/objective-c-and-c-code-customization.json'
content_hash: 'sha256:64691c6d81222595'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md)

# Objective-C 与 C 代码自定义

对你的 Objective-C API 应用宏，自定义它们导入 Swift 的方式。

## 主题

### 自定义 Objective-C API

- [Designating Nullability in Objective-C APIs](designating-nullability-in-objective-c-apis.md) — 使用空性标注，或将区域标记为已标注，以控制 Objective-C 声明导入 Swift 的方式。
- [Renaming Objective-C APIs for Swift](renaming-objective-c-apis-for-swift.md) — 使用 `NS_SWIFT_NAME` 宏为 Swift 自定义 API 名称。
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md) — 使用 `NS_REFINED_FOR_SWIFT` 宏改变某个 API 导入 Swift 的方式。
- [Grouping Related Objective-C Constants](grouping-related-objective-c-constants.md) — 为你的 Objective-C 类型添加宏，以便在 Swift 中对其值进行分组。
- [Marking API Availability in Objective-C](marking-api-availability-in-objective-c.md) — 使用一个宏来标示 Objective-C API 的可用性。
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md) — 使用 `NS_SWIFT_UNAVAILABLE` 宏阻止某个 API 在 Swift 中被使用。

### Customizing C APIs

- [Customizing Your C Code for Swift](customizing-your-c-code-for-swift.md) — 使用 `CF_SWIFT_NAME` 宏对具有相关行为的函数进行分组。

## 另请参阅

### 与 Objective-C 和 C 的语言互操作性

- [Migrating Your Objective-C Code to Swift](migrating-your-objective-c-code-to-swift.md) — 了解迁移代码的推荐步骤。
- [Cocoa Design Patterns](cocoa-design-patterns.md) — 在你的 Swift App 中采纳并与 Cocoa 设计模式互操作。
- [Handling Dynamically Typed Methods and Objects in Swift](handling-dynamically-typed-methods-and-objects-in-swift.md) — 把 Objective-C `id` 类型的实例转换为特定的 Swift 类型。
- [Using Objective-C Runtime Features in Swift](using-objective-c-runtime-features-in-swift.md) — 使用选择器和键路径与动态的 Objective-C API 交互。
- [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md) — 使用原生 Swift 语法与 C 和 Objective-C 中的类型及函数互操作。
- [Calling Objective-C APIs Asynchronously](calling-objective-c-apis-asynchronously.md) — 了解接受完成处理程序的函数和方法是如何被转换为 Swift 异步函数的。
</content>
