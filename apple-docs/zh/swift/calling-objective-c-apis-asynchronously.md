---
title: 异步调用 Objective-C API
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/calling-objective-c-apis-asynchronously
source_url: 'https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/calling-objective-c-apis-asynchronously.json'
content_hash: 'sha256:c4e85d0c2f648dc4'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# 异步调用 Objective-C API

<sub>文章</sub>

了解带有完成处理程序（completion handler）的函数和方法是如何转换成 Swift 异步函数的。

## 概述

在 Cocoa 中，执行异步操作的方法会将完成处理程序（completion handler）作为其最后一个参数，操作完成后方法会调用该 block 来返回结果或错误。Swift 5.5 及更高版本除了将基于回调的方法版本导入到 Swift 中之外，还会自动将带有完成处理程序的 Objective-C 方法转换为使用 Swift 原生并发支持的异步方法。由于这两个 Swift 方法行为相同，它们在文档中共享同一页面。

有关异步函数的信息，请参阅 [Swift 编程语言](https://docs.swift.org/swift-book/) 中的[并发](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html)。

### 了解 Swift 如何导入完成处理程序

Swift 会将带有完成处理程序的 Objective-C 方法导入为两个相关的 Swift 方法：一个接受闭包（closure）的方法，以及一个不接受闭包的异步方法。例如，考虑 PassKit 中的 [present(completion:)](<../passkit/pkpaymentauthorizationcontroller/present(completion_).md>) 方法。在 Objective-C 中，它声明如下：

```occ
- (void)presentWithCompletion:(void (^)(BOOL success))completion;
```

然而，在 Swift 中，它被导入为两个方法：

```swift
func present(completion: ((Bool) -> Void)? = nil)

func present() async -> Bool
```

第一个版本 `present(completion:)` 的返回类型为 `Void`，并接受一个完成处理程序。第二个版本 `present()` 返回一个布尔值，并且是一个异步方法。

其完成处理程序会填充 [NSError](../foundation/nserror.md) 指针参数的方法在 Swift 中也会变为抛出方法，如[关于导入的 Cocoa 错误参数](about-imported-cocoa-error-parameters.md)中所述。异步抛出方法上的 `NSError` 参数也必须是可空的，这表明该参数仅用于传递错误。例如，考虑 [URLSessionStreamTask](../foundation/urlsessionstreamtask.md) 中的 [write(_:timeout:completionHandler:)](<../foundation/urlsessionstreamtask/write(__timeout_completionhandler_).md>) 方法。在 Objective-C 中，它声明如下：

```occ
- (void)writeData:(NSData *)data
          timeout:(NSTimeInterval)timeout
completionHandler:(void (^) (NSError * _Nullable error))completionHandler;
```

与前一个示例一样，Swift 将此 Objective-C 方法导入为两个方法：一个接受闭包的异步方法，和一个异步抛出方法。

```swift
func write(
    _ data: Data, 
    timeout: TimeInterval, 
    completionHandler: @escaping (Error?) -> Void
)

func write(_ data: Data, timeout: TimeInterval) async throws
```

其完成处理程序接受多个参数的方法会变成返回元组的方法。例如，PassKit 中的 [sign(_:using:completion:)](<../passkit/pkpasslibrary/sign(__using_completion_).md>) 方法在 Objective-C 中声明如下：

```occ
- (void)signData:(NSData *)signData 
withSecureElementPass:(PKSecureElementPass *)secureElementPass 
      completion:(void (^)(NSData *signedData, NSData *signature, NSError *error))completion;
```

在 Swift 中，它被导入为两个方法：一个接受闭包的异步方法，和一个返回元组的异步抛出方法：

```swift
func sign(
    _ signData: Data, 
    using secureElementPass: PKSecureElementPass, 
    completion: @escaping (Data?, Data?, Error?) -> Void
)

func sign(_ signData: Data, 
    using secureElementPass: PKSecureElementPass
) async throws -> (Data, Data)
```

### 了解转换规则

接受完成处理程序的方法必须满足以下要求：

- 该方法具有 `void` 返回类型。
- 该 block 具有 `void` 返回类型。
- 该 block 在所有可能的控制流路径上都恰好被调用一次。

如果该方法只有一个参数，并且其选择器（selector）以下列某个后缀结尾，则 Swift 会将该方法导入为异步方法：

- `WithCompletion`
- `WithCompletionHandler`
- `WithCompletionBlock`
- `WithReplyTo`
- `WithReply`

如果该方法有多个参数，并且最后一个参数的选择器片段是以下某个，则 Swift 会将该方法导入为异步方法：

- `completion`
- `withCompletion`
- `completionHandler`
- `withCompletionHandler`
- `completionBlock`
- `withCompletionBlock`
- `replyTo`
- `withReplyTo`
- `reply`
- `replyTo`

Swift 方法的名称会按如下方式从 Objective-C 方法进行修改：

- 移除完成处理程序的选择器片段。
- 如果选择器以 `get` 开头，则移除该前缀，并将开头的首字母缩写词转换为小写。
- 如果选择器以 `Asynchronously` 结尾，则移除该后缀。
- 如果方法调用其完成处理程序时带有可空参数，则 Swift 中的异步版本会标记为 `@discardableResult` 特性（attribute）。

## 另请参阅

### 与 Objective-C 和 C 的语言互操作性

- [Objective-C 和 C 代码自定义](objective-c-and-c-code-customization.md) — 对你的 Objective-C API 应用宏以自定义它们导入到 Swift 的方式。
- [将你的 Objective-C 代码迁移到 Swift](migrating-your-objective-c-code-to-swift.md) — 了解迁移代码的推荐步骤。
- [Cocoa 设计模式](cocoa-design-patterns.md) — 在你的 Swift App 中采用 Cocoa 设计模式并与之互操作。
- [在 Swift 中处理动态类型方法和对象](handling-dynamically-typed-methods-and-objects-in-swift.md) — 将 Objective-C `id` 类型的实例转换为特定的 Swift 类型。
- [在 Swift 中使用 Objective-C 运行时特性](using-objective-c-runtime-features-in-swift.md) — 使用选择器（selector）和键路径（key path）与动态 Objective-C API 进行交互。
- [导入的 C 和 Objective-C API](imported-c-and-objective-c-apis.md) — 使用原生 Swift 语法与 C 和 Objective-C 中的类型和函数进行互操作。
