---
title: 在 Objective-C 中标记 API 可用性
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/marking-api-availability-in-objective-c
source_url: 'https://developer.apple.com/documentation/swift/marking-api-availability-in-objective-c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/marking-api-availability-in-objective-c.json'
content_hash: 'sha256:76c96f75a93d90e5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Objective-C and C Code Customization](objective-c-and-c-code-customization.md)

# 在 Objective-C 中标记 API 可用性

<sub>文章</sub>

使用一个宏来标示 Objective-C API 的可用性。

## 概述

在 Swift 中，你使用 `@available` 属性来控制某个声明在为特定目标平台构建 App 时是否可用。类似地，你使用可用性条件 `#available`，根据所需的平台和版本条件来有条件地执行代码。这两种可用性说明符在 Objective-C 中同样可用。

关于指定和检查平台可用性的详细信息，参见 [The Swift Programming Language](https://docs.swift.org/swift-book/) 中的 [available](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#available) 和 [检查 API 可用性](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow#Checking-API-Availability)。

### 标记可用性

使用 `API_AVAILABLE` 宏在 Objective-C 中添加可用性信息：

```occ
@interface MyViewController : UIViewController
- (void) newMethod API_AVAILABLE(ios(11), macosx(10.13));
@end
```

这等价于在 Swift 中对某个声明使用 `@available` 属性：

```swift
@available(iOS 11, macOS 10.13, *)
func newMethod() {
    // Use iOS 11 APIs.
}
```

### 检查可用性

在 Objective-C 的条件语句中使用 `@available()` 关键字来检查可用性信息：

```occ
if (@available(iOS 11, *)) {
    // Use iOS 11 APIs.
} else {
    // Alternative code for earlier versions of iOS.
}
```

这等价于 Swift 中的以下条件语句：

```swift
if #available(iOS 11, *) {
    // Use iOS 11 APIs.
} else {
    // Alternative code for earlier versions of iOS.
}
```

## 另请参阅

### 自定义 Objective-C API

- [Designating Nullability in Objective-C APIs](designating-nullability-in-objective-c-apis.md) — 使用空性标注，或将区域标记为已标注，以控制 Objective-C 声明导入 Swift 的方式。
- [Renaming Objective-C APIs for Swift](renaming-objective-c-apis-for-swift.md) — 使用 `NS_SWIFT_NAME` 宏为 Swift 自定义 API 名称。
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md) — 使用 `NS_REFINED_FOR_SWIFT` 宏改变某个 API 导入 Swift 的方式。
- [Grouping Related Objective-C Constants](grouping-related-objective-c-constants.md) — 为你的 Objective-C 类型添加宏，以便在 Swift 中对其值进行分组。
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md) — 使用 `NS_SWIFT_UNAVAILABLE` 宏阻止某个 API 在 Swift 中被使用。
</content>
