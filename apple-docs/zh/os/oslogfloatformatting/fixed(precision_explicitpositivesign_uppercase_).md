---
title: 'fixed(precision:explicitPositiveSign:uppercase:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogfloatformatting/fixed(precision:explicitpositivesign:uppercase:)'
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting/fixed(precision:explicitpositivesign:uppercase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting/fixed%28precision%3Aexplicitpositivesign%3Auppercase%3A%29.json'
content_hash: 'sha256:01f5aca9bc44c45a'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogFloatFormatting](../oslogfloatformatting.md)

# fixed(precision:explicitPositiveSign:uppercase:)

<sub>类型方法</sub>

创建具有指定精度值的自定义定点格式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fixed(precision: @autoclosure @escaping () -> Int, explicitPositiveSign: Bool = false, uppercase: Bool = false) -> OSLogFloatFormatting
```

## 参数

- `precision` — 小数点右侧最多显示的位数。

- `explicitPositiveSign` — 一个布尔值，指示是否在正数前面显示加号（`+`）。

- `uppercase` — 一个布尔值，指示是否将浮点数中的字母转为大写。例如，它决定数字 `1.0e9` 中指数指示符 `e` 的大小写，以及 `NaN` 和 `Inf` 等特殊值中字母的大小写。

## 返回值

浮点数的自定义定点格式。

## 另请参阅

### 创建自定义格式化对象

- [exponential(explicitPositiveSign:uppercase:)](<exponential(explicitpositivesign_uppercase_).md>) — 创建具有系统确定精度值的自定义指数格式。
- [exponential(precision:explicitPositiveSign:uppercase:)](<exponential(precision_explicitpositivesign_uppercase_).md>) — 创建具有指定精度值的自定义指数格式。
- [fixed(explicitPositiveSign:uppercase:)](<fixed(explicitpositivesign_uppercase_).md>) — 创建具有系统确定精度值的自定义定点格式。
- [hex(explicitPositiveSign:uppercase:)](<hex(explicitpositivesign_uppercase_).md>) — 创建自定义十六进制格式。
- [hybrid(explicitPositiveSign:uppercase:)](<hybrid(explicitpositivesign_uppercase_).md>) — 创建具有系统确定精度值的自定义混合格式。
- [hybrid(precision:explicitPositiveSign:uppercase:)](<hybrid(precision_explicitpositivesign_uppercase_).md>) — 创建具有该精度值的自定义混合格式。
