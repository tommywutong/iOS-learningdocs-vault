---
title: 使 Objective-C API 在 Swift 中不可用
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/making-objective-c-apis-unavailable-in-swift
source_url: 'https://developer.apple.com/documentation/swift/making-objective-c-apis-unavailable-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/making-objective-c-apis-unavailable-in-swift.json'
content_hash: 'sha256:3a2bb3b28c7804f9'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Objective-C 与 C 代码定制](objective-c-and-c-code-customization.md)

# 使 Objective-C API 在 Swift 中不可用

<sub>文章</sub>

使用 `NS_SWIFT_UNAVAILABLE` 宏来阻止某个 API 在 Swift 中被使用。

## 概述

如果某个 Objective-C API 的部分内容不适合 Swift，你可以让这些部分在 Swift 中不可用。在引入替代现有 Objective-C API 部分功能的新 Swift API 时，你可以将部分 API 设置为在 Swift 中不可用。例如，你可以用一个嵌套在某个 Swift 类型中的 Swift 常量来替换一个 Objective-C 常量。

### 阻止导入 Objective-C API

要阻止导入 Objective-C API 中的某个声明，请向 `NS_SWIFT_UNAVAILABLE` 宏传递一个参数。该参数指示使用 Swift 的开发人员应该改用其他方式，而非使用你设为不可用的那部分 API。

在以下示例中，一个 Objective-C 类提供了一个便捷初始化方法，该方法接受可变数量的键值对参数，并建议改用字典字面量：

```occ
+ (instancetype)collectionWithValues:(NSArray *)values
                             forKeys:(NSArray<NSCopying> *)keys
NS_SWIFT_UNAVAILABLE("Use a dictionary literal instead.");
```

在 Swift 中尝试调用 `collectionWithValues:forKeys:` 方法会导致编译器错误。

### 使 API 在两种语言中均不可用

要使 Objective-C 声明在 Swift 和 Objective-C 的编译时均不可用，请使用 `NS_UNAVAILABLE` 宏。该宏的行为与 `NS_SWIFT_UNAVAILABLE` 宏类似，只是不支持自定义错误消息，并且会限制在 Objective-C 代码中对该声明的编译时访问。

## 另请参阅

### 自定义 Objective-C API

- [在 Objective-C API 中标注可空性](designating-nullability-in-objective-c-apis.md) — 使用可空性注解或将区域标记为已注解，以控制 Objective-C 声明导入 Swift 的方式。
- [为 Swift 重命名 Objective-C API](renaming-objective-c-apis-for-swift.md) — 使用 `NS_SWIFT_NAME` 宏为 Swift 定制 API 名称。
- [改进用于 Swift 的 Objective-C API 声明](improving-objective-c-api-declarations-for-swift.md) — 使用 `NS_REFINED_FOR_SWIFT` 宏更改 API 导入 Swift 的方式。
- [对相关的 Objective-C 常量进行分组](grouping-related-objective-c-constants.md) — 向你的 Objective-C 类型添加宏，以在 Swift 中对其值进行分组。
- [在 Objective-C 中标记 API 可用性](marking-api-availability-in-objective-c.md) — 使用宏来标注 Objective-C API 的可用性。
