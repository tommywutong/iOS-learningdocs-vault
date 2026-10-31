---
title: 关于导入的 Cocoa 错误参数
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/about-imported-cocoa-error-parameters
source_url: 'https://developer.apple.com/documentation/swift/about-imported-cocoa-error-parameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/about-imported-cocoa-error-parameters.json'
content_hash: 'sha256:235b53a16535698e'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Cocoa 设计模式](cocoa-design-patterns.md)

# 关于导入的 Cocoa 错误参数

<sub>文章</sub>

了解 Cocoa 错误参数如何被转换为 Swift 的抛出方法。

## 概述

在 Cocoa 中，会产生错误的方法以一个 [NSError](../foundation/nserror.md) 指针参数作为其最后一个参数，如果发生错误，该实参会被填充为一个 [NSError](../foundation/nserror.md) 对象。Swift 会根据 Swift 原生的错误处理功能，自动把产生错误的 Objective-C 方法转换为抛出错误的方法。

### 了解错误参数是如何导入的

Swift 会检查 Objective-C 方法声明，并把它们转换为 Swift 的抛出方法，在可能的情况下使用更短的名称。

例如，考虑 [FileManager](../foundation/filemanager.md) 中的 [removeItem(at:)](<../foundation/filemanager/removeitem(at_).md>) 方法。在 Objective-C 中，它声明如下：

```occ
- (BOOL)removeItemAtURL:(NSURL *)URL
                  error:(NSError **)error;
```

在 Swift 中，它被导入为：

```swift
func removeItem(at: URL) throws
```

注意，[removeItem(at:)](<../foundation/filemanager/removeitem(at_).md>) 方法被 Swift 导入时具有 `Void` 返回类型、没有错误参数，并带有 `throws` 声明。

如果 Objective-C 方法的最后一个非 block 参数的类型是 `NSError **`，Swift 会用 throws 关键字替换它，以表明该方法可以抛出错误。如果 Objective-C 方法的错误参数同时也是它的第一个参数，Swift 会尝试进一步简化方法名称，方法是从选择器（selector）的第一部分中移除 `WithError` 或 `AndReturnError` 后缀（如果存在）。如果结果得到的选择器已经声明了另一个方法，则方法名称不会改变。

如果产生错误的 Objective-C 方法返回一个 [BOOL](../objectivec/bool.md) 值来指示方法调用的成功与否，Swift 会把函数的返回类型改为 `Void`。同样，如果产生错误的 Objective-C 方法返回 `nil` 来指示方法调用失败，Swift 会把函数的返回类型改为非可选类型。

否则，如果无法推断出任何约定，则方法保持原样。

> [!note] 注意
> 在会产生 [NSError](../foundation/nserror.md) 的 Objective-C 方法声明上使用 `NS_SWIFT_NOTHROW` 宏，可以防止它被 Swift 导入为抛出方法。

## 另请参阅

### 常用模式

- [在 Swift 中使用键值观察](using-key-value-observing-in-swift.md) — 把其他对象属性的变化通知给对象。
- [使用委托自定对象行为](using-delegates-to-customize-object-behavior.md) — 代表委托方响应事件。
- [使用单例管理共享资源](managing-a-shared-resource-using-a-singleton.md) — 使用单一的共享类实例来提供对共享资源的访问。
- [在 Swift 中处理 Cocoa 错误](handling-cocoa-errors-in-swift.md) — 抛出和捕获使用 Cocoa 错误类型的错误。
