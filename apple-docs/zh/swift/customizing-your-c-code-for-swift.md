---
title: 为 Swift 定制你的 C 代码
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customizing-your-c-code-for-swift
source_url: 'https://developer.apple.com/documentation/swift/customizing-your-c-code-for-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customizing-your-c-code-for-swift.json'
content_hash: 'sha256:1fb8dda2c637b6a0'
translated: true
---

> 导航： [技术](../technologies.md) · [Swift](../swift.md) · [Objective-C 与 C 代码定制](objective-c-and-c-code-customization.md)

# 为 Swift 定制你的 C 代码

<sub>文章</sub>

使用 `CF_SWIFT_NAME` 宏，将行为相关的函数分组。

## 概述

因为 C 语言中的结构体不能拥有方法、属性存取方法或自定义初始化方法，你通常需要使用全局函数来编写这类功能。而 Swift 中的结构体可以声明方法、属性存取方法和初始化方法。你可以使用 `CF_SWIFT_NAME` 宏，把相关的全局函数组合成一个被导入到 Swift 中的单一结构体类型。

### 将 CF_SWIFT_NAME 应用于相关函数

下面的示例展示了几个都与 `Color` 类型相关的函数。`CF_SWIFT_NAME` 宏被应用到每个函数上，为它们分别指定一个在 Swift 中的新名称，这些新名称都嵌套在 `Color` 类型之下：

```occ
Color ColorCreateWithCMYK(float c, float m, float y, float k) CF_SWIFT_NAME(Color.init(c:m:y:k:));

float ColorGetHue(Color color) CF_SWIFT_NAME(getter:Color.hue(self:));
void ColorSetHue(Color color, float hue) CF_SWIFT_NAME(setter:Color.hue(self:newValue:));

Color ColorDarkenColor(Color color, float amount) CF_SWIFT_NAME(Color.darken(self:amount:));

extern const Color ColorBondiBlue CF_SWIFT_NAME(Color.bondiBlue);

Color ColorGetCalibrationColor(void) CF_SWIFT_NAME(getter:Color.calibration());
Color ColorSetCalibrationColor(Color color) CF_SWIFT_NAME(setter:Color.calibration(newValue:));
```

你传给 `CF_SWIFT_NAME` 宏的参数使用的语法与 `#selector` 表达式相同。你可以在 `CF_SWIFT_NAME` 参数中使用 `self` 来指代该方法所属的实例。

### 将相关函数导入 Swift

下面是 Swift 如何将上面这些相关函数导入到单一类型中的：

```swift
extension Color {
    init(c: Float, m: Float, y: Float, k: Float)

    var hue: Float { get set }

    func darken(amount: Float) -> Color

    static var bondiBlue: Color

    static var calibration: Color
}
```

> [!note] 注意
> 对于使用 `CF_SWIFT_NAME` 宏导入的类型成员，你不能重新排列或更改其参数的数量。
