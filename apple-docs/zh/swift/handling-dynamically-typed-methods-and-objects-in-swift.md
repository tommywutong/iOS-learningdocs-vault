---
title: 在 Swift 中处理动态类型的方法和对象
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/handling-dynamically-typed-methods-and-objects-in-swift
source_url: 'https://developer.apple.com/documentation/swift/handling-dynamically-typed-methods-and-objects-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/handling-dynamically-typed-methods-and-objects-in-swift.json'
content_hash: 'sha256:bbd4085bcff8284d'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# 在 Swift 中处理动态类型的方法和对象

<sub>文章</sub>

把 Objective-C `id` 类型的实例转换为特定的 Swift 类型。

## 概述

在 Objective-C 中，`id` 类型表示可以是任何 Objective-C 类的实例的对象。`id` 类型则被 Swift 导入为 `Any` 类型。当你把 Swift 实例传给 Objective-C API 时，它会被桥接为 `id` 参数，从而可以在该 API 中作为 Objective-C 对象使用。当 `id` 值作为 `Any` 导入到 Swift 时，运行时会自动处理桥接回去的工作，无论是桥接为类引用还是值类型。

```swift
var x: Any = "hello" as String
x as? String   // 值为 "hello" 的 String
x as? NSString // 值为 "hello" 的 NSString

x = "goodbye" as NSString
x as? String   // 值为 "goodbye" 的 String
x as? NSString // 值为 "goodbye" 的 NSString
```

### 向下转换对象以调用方法和访问属性

当你处理 `Any` 类型的对象并且知道其底层类型时，把这些对象向下转换为底层类型通常很有用。但是，由于 `Any` 类型可以指代任何类型，编译器无法保证向下转换到更具体的类型一定成功。

你可以使用条件类型转换运算符（`as?`），它返回一个可选值，其类型是你尝试向下转换到的类型：

```swift
let userDefaults = UserDefaults.standard
let lastRefreshDate = userDefaults.object(forKey: "LastRefreshDate") // lastRefreshDate 的类型是 Any?
if let date = lastRefreshDate as? Date {
    print("\(date.timeIntervalSinceReferenceDate)")
}
```

如果你完全确定对象的类型，可以改用强制向下转换运算符（`as!`）。

```swift
let myDate = lastRefreshDate as! Date
let timeInterval = myDate.timeIntervalSinceReferenceDate
```

但是，如果强制向下转换失败，就会触发运行时错误：

```swift
let myDate = lastRefreshDate as! String // 错误
```

## 另请参阅

### 与 Objective-C 和 C 的语言互操作性

- [Objective-C 与 C 代码自定义](objective-c-and-c-code-customization.md) — 为你的 Objective-C API 应用宏，自定它们导入 Swift 的方式。
- [将你的 Objective-C 代码迁移到 Swift](migrating-your-objective-c-code-to-swift.md) — 了解迁移代码的推荐步骤。
- [Cocoa 设计模式](cocoa-design-patterns.md) — 在你的 Swift App 中采用 Cocoa 设计模式并与之互操作。
- [在 Swift 中使用 Objective-C 运行时特性](using-objective-c-runtime-features-in-swift.md) — 使用选择器（selector）和键路径与动态的 Objective-C API 交互。
- [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md) — 使用原生 Swift 语法与 C 和 Objective-C 中的类型和函数互操作。
- [异步调用 Objective-C API](calling-objective-c-apis-asynchronously.md) — 了解接受完成处理程序的函数和方法如何被转换为 Swift 异步函数。
