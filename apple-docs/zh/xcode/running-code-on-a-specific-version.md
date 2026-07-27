---
title: 在特定平台或操作系统版本上运行代码
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/running-code-on-a-specific-version
source_url: 'https://developer.apple.com/documentation/xcode/running-code-on-a-specific-version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/running-code-on-a-specific-version.json'
content_hash: 'sha256:83f046b15aacc989'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Build system](build-system.md)

# 在特定平台或操作系统版本上运行代码

<sub>文章</sub>

在需要特定设备系列或最低操作系统版本才能运行的代码周围添加条件编译标记。

## 概述

当你投入时间为 App 开发一项新功能时，你希望从所编写的代码中获得最大的价值。为了支持一个新的平台或操作系统版本而创建一个新项目会增加不必要的工作量，尤其是当你的大部分代码保持不变时。最佳解决方案是维护同一个版本的 App，使其能够在多个平台和操作系统版本上运行。要实现这一点，可以针对目标平台有条件地编译代码，或者使用可用性条件检查来根据操作系统版本运行代码。

### 为特定平台编译代码

Apple 平台支持许多相同的技术，但有些功能可能并非在每个平台上都可用。例如，iOS 设备上的功能在 macOS 设备上可能没有意义。为了防止代码在不支持相应功能的操作系统上编译，请添加一个条件编译块来指定目标操作系统。

```swift
/// Swift
/// `iOS` 指定了此代码要编译的目标操作系统。
/// 将 `iOS` 更改为指定另一种操作系统。
#if os(iOS)
   // iOS 代码
#endif
```

```objc
/// Objective-C
/// `IOS` 指定了此代码要编译的目标操作系统。
/// 将 `IOS` 更改为指定另一种操作系统。有关编译宏的
/// 列表，请参阅相应 SDK 中的 /usr/include/TargetConditionals.h
/// 头文件。
#if TARGET_OS_IOS
   // iOS 代码
#endif
```

你还可以针对特定环境（例如「模拟器」或 Mac Catalyst）编译或阻止编译代码。

```swift
/// Swift
/// `simulator` 指定了此代码要编译的目标环境。
/// 将 `simulator` 更改为指定另一种环境，例如 `macCatalyst`。
#if targetEnvironment(simulator)
    // 模拟器代码
#endif

```

```objc
/// Objective-C
/// `SIMULATOR` 指定了此代码所依赖的环境。
/// 将 `SIMULATOR` 更改为指定另一种环境，例如 `MACCATALYST`。
#if TARGET_OS_SIMULATOR
    // 模拟器代码
#endif
```

如果你的 Swift 代码依赖某个特定的 Swift 包或框架，你可以检查是否能够导入该包或框架。此条件测试的是能否导入某个模块，但并不会真正导入它。这种检查方式的优点是，如果未来版本的操作系统提供了该包或框架，你的代码就会使用它。

```swift
/// Swift
/// `UIKit` 指定了此代码所依赖的模块。
/// 将 `UIKit` 更改为指定另一个模块。
#if canImport(UIKit)
    // 需要 UIKit 的代码
#endif
```

有关编译器控制语句以及它们所支持的平台条件的更多信息，请参阅 Swift 语言文档中的[编译器控制语句](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Compiler-Control-Statements)。

### 为某项功能要求最低操作系统版本

你 App 的最低部署目标定义了你 App 所支持的操作系统版本范围。与其为每次 App 更新都要求最新的系统软件，不如以一两个较旧的操作系统版本为目标，让用户有时间逐步过渡。当你实现仅存在于最新操作系统版本中的功能时，请用可用性标记包裹你的代码。

- 在 Swift 中，使用 `#available` 编译器控制语句来有条件地运行代码。
- 在 Objective-C 中，使用 `@available` 编译器指令来有条件地运行代码。

平台名称同时支持发行版本的主版本号和次版本号，如下例所示：

```swift
/// Swift
if #available(iOS 15.4.1, *) {
    // 在 iOS 上，此分支在 15.4.1 及更高版本中运行。
    // 在任何其他操作系统上，此分支在该操作系统的任意版本中运行。
} else {
   // 此分支在更早的 iOS 版本中运行。
}
```

```objc
/// Objective-C
if (@available(iOS 15.4.1, *)) {
    // 在 iOS 上，此分支在 15.4.1 及更高版本中运行。
    // 在任何其他操作系统上，此分支在该操作系统的任意版本中运行。
} else {
   // 此分支在更早的 iOS 版本中运行。
}
```

`*` 匹配任何其他操作系统。要为多个操作系统指定版本，请包含多个以逗号分隔的操作系统名称。

```swift
// Swift
if #available(iOS 15, macOS 12, *) {
    // 在 iOS 上，此分支在 iOS 15 或更高版本中运行。
    // 在 macOS 上，此分支在 macOS 12 或更高版本中运行。
    // 在任何其他操作系统上，此分支将在该操作系统的任意版本中运行。
} else {
   // 此分支在更早的 iOS 和 macOS 版本中运行。
}
```

```objc
// Objective-C
if (@available(iOS 15, macOS 12, *)) {
    // 在 iOS 上，此分支在 iOS 15 或更高版本中运行。
    // 在 macOS 上，此分支在 macOS 12 或更高版本中运行。
    // 在任何其他操作系统上，此分支将在该操作系统的任意版本中运行。
} else {
   // 此分支在更早的 iOS 和 macOS 版本中运行。
}
```

有关可用性条件语句的更多信息，请参阅 Swift 语言文档中的[可用性条件](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Availability-Condition)。

### 在代码中为声明添加注解

你可以通过将具有共同要求的代码归并在一起并为声明添加注解，来减少 App 执行的条件运行时检查的数量。

- 在 Swift 中，使用 `@available` 属性来表明某个声明是可用的。
- 在 Objective-C 中，使用 `API_AVAILABLE` 宏来添加可用性信息。

```swift
@available(iOS 15, macOS 12, *)
func newMethod() {
    // 使用 iOS 15 的 API。
}
```

```objc
@interface MyViewController : UIViewController
- (void) newMethod API_AVAILABLE(ios(15));
@end
```

有了上述注解，调用 `newMethod` 可能仍需要一条编译器控制语句，但你不再需要在函数体内部再次进行检查。

有关在 Swift 中标记可用性的更多信息，请参阅 [available](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#available)。

## 另请参阅

### 构建自定

- [自定项目的构建 Scheme](customizing-the-build-schemes-for-a-project.md) — 指定要构建哪些目标，并自定 Xcode 用于构建、运行、测试和分析这些目标的设置。
- [自定目标的构建阶段](customizing-the-build-phases-of-a-target.md) — 指定在构建过程中要执行的任务，包括要编译的源文件、要运行的脚本，以及要包含在最终产品中的资源。
- [为自定文件类型创建构建规则](creating-build-rules-for-custom-file-types.md) — 告诉 Xcode 如何构建你项目中的自定文件类型，并提供依赖信息，以针对每个文件优化构建过程。
- [在构建期间运行自定脚本](running-custom-scripts-during-a-build.md) — 在构建过程中执行自定 Shell 脚本，并运行你项目所需的工具或其他命令。
