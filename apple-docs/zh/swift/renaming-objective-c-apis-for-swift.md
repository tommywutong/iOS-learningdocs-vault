---
title: 为 Swift 重命名 Objective-C API
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/renaming-objective-c-apis-for-swift
source_url: 'https://developer.apple.com/documentation/swift/renaming-objective-c-apis-for-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/renaming-objective-c-apis-for-swift.json'
content_hash: 'sha256:c02135ccbe787d7f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Objective-C 和 C 代码定制](objective-c-and-c-code-customization.md)

# 为 Swift 重命名 Objective-C API

<sub>文章</sub>

使用 `NS_SWIFT_NAME` 宏为 Swift 自定义 API 名称。

## 概述

如果你想把一个 Objective-C API 以不同的名称导入 Swift，可以使用 `NS_SWIFT_NAME` 宏。这个宏会保留 Objective-C 代码里使用的原名称，因此这个 API 在每种语言里都有恰当的名称。

你可以把 `NS_SWIFT_NAME` 宏应用到 Objective-C 里某个单独的类型、方法或函数声明上。应用这个宏之后，你在 Swift 代码里使用的名称就会是你通过这个宏选定的名称。

### 重命名 API

下面的示例重命名了一个类及其中一个属性：

```occ
NS_SWIFT_NAME(Sandwich.Preferences)
@interface SandwichPreferences : NSObject

@property BOOL includesCrust NS_SWIFT_NAME(isCrusty);

@end

@interface Sandwich : NSObject
@end
```

`SandwichPreferences` 类及其 `includesCrust` 属性，在 Swift 里被分别重命名为 `Sandwich.Preferences` 和 `isCrusty`：

```swift
var preferences = Sandwich.Preferences()
preferences.isCrusty = true
```

对于类和协议，你要把 `NS_SWIFT_NAME` 宏用作前缀。对于其他所有种类的声明——比如属性、枚举 case 和类型别名——你要把这个宏用作后缀。下面的示例把这个宏用作后缀，重命名了一个枚举：

```occ
typedef NS_ENUM(NSInteger, SandwichBreadType) {
    brioche, pumpernickel, pretzel, focaccia
} NS_SWIFT_NAME(SandwichPreferences.BreadType);
```

## 另请参阅

### 自定义 Objective-C API

- [在 Objective-C API 里指定可空性](designating-nullability-in-objective-c-apis.md) — 使用可空性标注，或者把某些区域标记为已标注，来控制 Objective-C 声明导入 Swift 的方式。
- [为 Swift 改进 Objective-C API 声明](improving-objective-c-api-declarations-for-swift.md) — 使用 `NS_REFINED_FOR_SWIFT` 宏来改变一个 API 导入 Swift 的方式。
- [对相关的 Objective-C 常量分组](grouping-related-objective-c-constants.md) — 在你的 Objective-C 类型里添加宏，将它们的值在 Swift 里分组。
- [在 Objective-C 里标记 API 可用性](marking-api-availability-in-objective-c.md) — 使用宏来标示一个 Objective-C API 的可用性。
- [让 Objective-C API 在 Swift 里不可用](making-objective-c-apis-unavailable-in-swift.md) — 使用 `NS_SWIFT_UNAVAILABLE` 宏来阻止一个 API 在 Swift 里被使用。
