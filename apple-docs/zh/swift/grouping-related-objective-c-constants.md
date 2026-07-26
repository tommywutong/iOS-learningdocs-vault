---
title: 对相关的 Objective-C 常量进行分组
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/grouping-related-objective-c-constants
source_url: 'https://developer.apple.com/documentation/swift/grouping-related-objective-c-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/grouping-related-objective-c-constants.json'
content_hash: 'sha256:c653d1afdd40faf9'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Objective-C and C Code Customization](objective-c-and-c-code-customization.md)

# 对相关的 Objective-C 常量进行分组

<sub>文章</sub>

为你的 Objective-C 类型添加宏，以便在 Swift 中把它们的值分组。

## 概述

你可以使用下列宏中的一个，来声明若干个 Objective-C 常量彼此相关：

- `NS_ENUM` 用于简单的枚举
- `NS_CLOSED_ENUM` 用于永远不会新增 case 的简单枚举
- `NS_OPTIONS` 用于 case 可以被组合成选项集合的枚举
- `NS_TYPED_ENUM` 用于原始值类型由你自行指定的枚举
- `NS_TYPED_EXTENSIBLE_ENUM` 用于你预期以后可能会新增 case 的枚举

### 声明简单枚举

对于简单的常量分组，使用 `NS_ENUM` 宏。

下面的例子使用该宏声明了一个 `UITableViewCellStyle` 枚举，把表格视图的几种不同样式分为一组：

```occ
typedef NS_ENUM(NSInteger, UITableViewCellStyle) {
    UITableViewCellStyleDefault,
    UITableViewCellStyleValue1,
    UITableViewCellStyleValue2,
    UITableViewCellStyleSubtitle
};
```

在 Swift 中，`UITableViewCellStyle` 枚举会像这样被导入：

```swift
enum UITableViewCellStyle: Int {
    case `default`
    case value1
    case value2
    case subtitle
}
```

用 `NS_ENUM` 宏导入的枚举，即便用一个并不对应任何枚举 case 的原始值来初始化，也不会失败。这一特性有助于与 C 兼容——C 允许在枚举中存储任意值，包括仅在内部使用、并未在头文件中公开的值。

`NS_ENUM` 宏是唯一一个在导入 Swift 后会生成真正枚举类型的枚举宏。其他枚举宏生成的都是结构体。

### 声明封闭枚举

对于你永远不会再新增 case 的简单常量分组，使用 `NS_CLOSED_ENUM` 宏。封闭枚举适合用来表示一组有限的状态，你预期人们会用 switch 语句对其进行匹配。[ComparisonResult](../foundation/comparisonresult.md) 的三个 case——[ComparisonResult.orderedAscending](../foundation/comparisonresult/orderedascending.md)、[ComparisonResult.orderedSame](../foundation/comparisonresult/orderedsame.md) 和 [ComparisonResult.orderedDescending](../foundation/comparisonresult/ordereddescending.md)——就是这样一组有限集合的例子。在排序等任务中执行有序比较时，它们是仅有的几种合理 case。

在以下场景中，不要使用 `NS_CLOSED_ENUM` 宏：

- 你曾在枚举初次声明之后又为其新增过 case
- 你能想到以后可能会新增的其他 case
- 该枚举带有任何私有 case

在这些场景下，请改用 `NS_ENUM` 宏。

### 声明选项集合

当一组常量分组中有两个或更多常量可以组合使用时，就使用 `NS_OPTIONS` 宏。例如，[JSONEncoder](../foundation/jsonencoder.md) 实例的输出格式化既可以是排序过的，也可以同时使用充裕的空白，因此在一个选项集合中同时指定这两个选项是合法的：`[.sorted, .prettyPrinted]`。

下面的例子展示了如何应用 `NS_OPTIONS` 宏，并分配互斥的原始值：

```occ
typedef NS_OPTIONS(NSUInteger, UIViewAutoresizing) {
        UIViewAutoresizingNone                 = 0,
        UIViewAutoresizingFlexibleLeftMargin   = 1 << 0,
        UIViewAutoresizingFlexibleWidth        = 1 << 1,
        UIViewAutoresizingFlexibleRightMargin  = 1 << 2,
        UIViewAutoresizingFlexibleTopMargin    = 1 << 3,
        UIViewAutoresizingFlexibleHeight       = 1 << 4,
        UIViewAutoresizingFlexibleBottomMargin = 1 << 5
};
```

配合位左移运算符（`<<`）使用递增的非负整数序列，可以确保选项集合中的每个选项在原始值的二进制表示中都占用唯一的一个二进制位。

`UIViewAutoresizing` 类型会像这样被导入到 Swift：

```swift
public struct UIViewAutoresizing: OptionSet {
    public init(rawValue: UInt)

    public static var flexibleLeftMargin: UIViewAutoresizing { get }
    public static var flexibleWidth: UIViewAutoresizing { get }
    public static var flexibleRightMargin: UIViewAutoresizing { get }
    public static var flexibleTopMargin: UIViewAutoresizing { get }
    public static var flexibleHeight: UIViewAutoresizing { get }
    public static var flexibleBottomMargin: UIViewAutoresizing { get }
}
```

### 声明带类型的枚举

使用 `NS_TYPED_ENUM` 来对具有你自行指定的原始值类型的常量进行分组。对于逻辑上*不能*在 Swift 扩展中添加值的常量集合，使用 `NS_TYPED_ENUM`；对于*可以*在扩展中扩充的常量集合，使用 `NS_TYPED_EXTENSIBLE_ENUM`。

下面的例子使用 `NS_TYPED_ENUM` 宏声明了交通信号灯所使用的不同颜色：

```occ
// Store the three traffic light color options as 0, 1, and 2.
typedef long TrafficLightColor NS_TYPED_ENUM;

TrafficLightColor const TrafficLightColorRed;
TrafficLightColor const TrafficLightColorYellow;
TrafficLightColor const TrafficLightColorGreen;
```

交通信号灯所使用的颜色数量预期不会增长，因此没有把它声明为可扩展的。

`TrafficLightColor` 类型会像这样被导入到 Swift：

```swift
struct TrafficLightColor: RawRepresentable, Equatable, Hashable {
    typealias RawValue = Int

    init(rawValue: RawValue)
    var rawValue: RawValue { get }

    static var red: TrafficLightColor { get }
    static var yellow: TrafficLightColor { get }
    static var green: TrafficLightColor { get }
}
```

#### 声明带类型的可扩展枚举

可扩展枚举的导入方式与不可扩展枚举类似，只是它们会多得到一个初始化方法。

下面的例子展示了如何声明、导入并扩展一个 `FavoriteColor` 类型。第一个例子声明了 `FavoriteColor` 类型，并为蓝色添加了一个枚举 case：

```occ
typedef long FavoriteColor NS_TYPED_EXTENSIBLE_ENUM;
FavoriteColor const FavoriteColorBlue;
```

这个额外的初始化方法省去了对其第一个参数标签的要求：

```swift
struct FavoriteColor: RawRepresentable, Equatable, Hashable {
    typealias RawValue = Int

    init(_ rawValue: RawValue)
    init(rawValue: RawValue)
    var rawValue: RawValue { get }

    static var blue: FavoriteColor { get }
}
```

你可以在之后的 Swift 代码中为可扩展枚举添加扩展。

下面的例子新增了一种喜爱的颜色：

```swift
extension FavoriteColor {
    static var green: FavoriteColor {
        return FavoriteColor(1) // blue is 0, green is 1, and new favorite colors could follow
    }
}
```

> [!note] 注意
> 你可能会遇到使用较旧的 `NS_STRING_ENUM` 和 `NS_EXTENSIBLE_STRING_ENUM` 宏的 Objective-C 代码，这两个宏曾用于对字符串常量进行分组。在对任意类型（包括字符串常量）的相关常量进行分组时，请使用 `NS_TYPED_ENUM` 和 `NS_TYPED_EXTENSIBLE_ENUM`。

## 另请参阅

### 自定义 Objective-C API

- [Designating Nullability in Objective-C APIs](designating-nullability-in-objective-c-apis.md) — 使用可空性标注，或将某些区域标记为已标注，以控制 Objective-C 声明导入 Swift 的方式。
- [Renaming Objective-C APIs for Swift](renaming-objective-c-apis-for-swift.md) — 使用 `NS_SWIFT_NAME` 宏为 Swift 自定义 API 名称。
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md) — 使用 `NS_REFINED_FOR_SWIFT` 宏更改某个 API 导入 Swift 的方式。
- [Marking API Availability in Objective-C](marking-api-availability-in-objective-c.md) — 使用宏标示某个 Objective-C API 的可用性。
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md) — 使用 `NS_SWIFT_UNAVAILABLE` 宏阻止某个 API 在 Swift 中被使用。
