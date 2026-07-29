---
title: 为 Swift 改进 Objective-C API 声明
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/improving-objective-c-api-declarations-for-swift
source_url: 'https://developer.apple.com/documentation/swift/improving-objective-c-api-declarations-for-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/improving-objective-c-api-declarations-for-swift.json'
content_hash: 'sha256:a965474baf9c6c7b'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Objective-C 与 C 代码定制](objective-c-and-c-code-customization.md)

# 为 Swift 改进 Objective-C API 声明

<sub>文章</sub>

使用 `NS_REFINED_FOR_SWIFT` 宏来更改 API 导入 Swift 的方式。

## 概述

如果你希望以不同的声明向 Swift 公开某个 Objective-C API，但底层实现相似，请使用 `NS_REFINED_FOR_SWIFT` 宏。当你将 Objective-C API 导入 Swift 时，可以采用仅支持 Swift 的类型，例如元组（tuples）。你还可以重新排序、组合和重命名参数，使该 API 与其他 Swift API 保持一致。

### 选择新名称和声明

下面的示例展示了一个 Objective-C API，该 API 在导入 Swift 后可以表达得更简洁：

```occ
@interface Color : NSObject

- (void)getRed:(nullable CGFloat *)red
         green:(nullable CGFloat *)green
          blue:(nullable CGFloat *)blue
         alpha:(nullable CGFloat *)alpha;

@end
```

在 Swift 中调用 `getRed(red:green:blue:alpha:)` 方法需要传入四个 in-out 参数。一个重新构想的 Swift 计算属性（computed property），用于表达相同的功能——获取颜色的分量——可以写成一个四元素元组：

```swift
var rgba: (red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

新名称更短，但仍然易于理解，因为它使用了颜色分量的行业标准缩写：RGBA。由新声明定义的属性在 Swift 中更易于使用。

### 公开现有实现

应用 `NS_REFINED_FOR_SWIFT` 宏可以公开现有的 Objective-C API，以便在你的改进 API 中重用。导入后，现有 API 的名称将带上双下划线（`__`）前缀，以帮助防止你在其他地方意外使用现有 API。

下面的示例将 `NS_REFINED_FOR_SWIFT` 宏添加到 `getRed(red:green:blue:alpha:)` 方法：

```occ
@interface Color : NSObject

- (void)getRed:(nullable CGFloat *)red
         green:(nullable CGFloat *)green
          blue:(nullable CGFloat *)blue
         alpha:(nullable CGFloat *)alpha NS_REFINED_FOR_SWIFT;

@end
```

以下规则决定了 API 的现有接口如何导入：

- 初始化方法（Initializer methods）在导入 Swift 后，会将其第一个参数标签（argument label）前加上双下划线（`__`）前缀。
- 对象下标方法（Object subscripting methods）在导入 Swift 后，如果其 getter 或 setter 方法标记了 `NS_REFINED_FOR_SWIFT`，则会作为方法导入，并在其基名称前加上双下划线（`__`）前缀，而不是作为 Swift subscript 导入。
- 其他方法在导入时，会将其基名称前加上双下划线（`__`）前缀。

### 重用现有实现

在 Swift 中实现新 API 时，你可以使用现有 API 的新名称来调用它，从而重用现有 API。

新的 `rgba` 属性的实现重用了现有的 `__getRed(red:green:blue:alpha:)` 方法，以确保功能在 Swift 和 Objective-C 之间保持一致：

```swift
extension Color {
    var rgba: (red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) {
        var r: CGFloat = 0.0
        var g: CGFloat = 0.0
        var b: CGFloat = 0.0
        var a: CGFloat = 0.0
        __getRed(red: &r, green: &g, blue: &b, alpha: &a)
        return (red: r, green: g, blue: b, alpha: a)
    }
}
```

## 另请参阅

### 自定义 Objective-C API

- [在 Objective-C API 中指定空值性](designating-nullability-in-objective-c-apis.md) — 使用空值性标注或标记区域为已标注，以控制 Objective-C 声明如何导入 Swift。
- [为 Swift 重命名 Objective-C API](renaming-objective-c-apis-for-swift.md) — 使用 `NS_SWIFT_NAME` 宏来为 Swift 定制 API 名称。
- [对相关的 Objective-C 常量进行分组](grouping-related-objective-c-constants.md) — 向你的 Objective-C 类型添加宏，以便在 Swift 中对其值进行分组。
- [在 Objective-C 中标记 API 可用性](marking-api-availability-in-objective-c.md) — 使用宏来表示 Objective-C API 的可用性。
- [使 Objective-C API 在 Swift 中不可用](making-objective-c-apis-unavailable-in-swift.md) — 使用 `NS_SWIFT_UNAVAILABLE` 宏来阻止某个 API 在 Swift 中使用。
