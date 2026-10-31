---
title: OSLogFloatFormatting
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogfloatformatting
source_url: 'https://developer.apple.com/documentation/os/oslogfloatformatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogfloatformatting.json'
content_hash: 'sha256:2d837f46850affad'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogFloatFormatting

<sub>结构体</sub>

double 和浮点数的格式化选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogFloatFormatting
```

## 概述

[OSLogFloatFormatting](oslogfloatformatting.md) 结构体封装了 `double` 和 `float` 值的格式化细节。使用静态的 [fixed](oslogfloatformatting/fixed.md)、[hex](oslogfloatformatting/hex.md)、[exponential](oslogfloatformatting/exponential.md) 和 [hybrid](oslogfloatformatting/hybrid.md) 结构体，可为浮点值应用默认格式。你也可以创建新的 [OSLogFloatFormatting](oslogfloatformatting.md) 结构体，自定义如何处理前导正号、精度信息等规则。

## 主题

### 获取标准格式

- [fixed](oslogfloatformatting/fixed.md) — 标准定点格式选项。
- [hex](oslogfloatformatting/hex.md) — 浮点值的标准十六进制格式。
- [exponential](oslogfloatformatting/exponential.md) — 标准指数格式选项。
- [hybrid](oslogfloatformatting/hybrid.md) — 根据数值大小切换格式的混合选项。

### 创建自定义格式化对象

- [exponential(explicitPositiveSign:uppercase:)](<oslogfloatformatting/exponential(explicitpositivesign_uppercase_).md>) — 创建具有系统确定精度值的自定义指数格式。
- [exponential(precision:explicitPositiveSign:uppercase:)](<oslogfloatformatting/exponential(precision_explicitpositivesign_uppercase_).md>) — 创建具有指定精度值的自定义指数格式。
- [fixed(explicitPositiveSign:uppercase:)](<oslogfloatformatting/fixed(explicitpositivesign_uppercase_).md>) — 创建具有系统确定精度值的自定义定点格式。
- [fixed(precision:explicitPositiveSign:uppercase:)](<oslogfloatformatting/fixed(precision_explicitpositivesign_uppercase_).md>) — 创建具有指定精度值的自定义定点格式。
- [hex(explicitPositiveSign:uppercase:)](<oslogfloatformatting/hex(explicitpositivesign_uppercase_).md>) — 创建自定义十六进制格式。
- [hybrid(explicitPositiveSign:uppercase:)](<oslogfloatformatting/hybrid(explicitpositivesign_uppercase_).md>) — 创建具有系统确定精度值的自定义混合格式。
- [hybrid(precision:explicitPositiveSign:uppercase:)](<oslogfloatformatting/hybrid(precision_explicitpositivesign_uppercase_).md>) — 创建具有该精度值的自定义混合格式。

## 另请参阅

### 值格式化器

- [OSLogBoolFormat](oslogboolformat.md) — 布尔值的格式化选项。
- [OSLogIntegerFormatting](oslogintegerformatting.md) — 整数值的格式化选项。
- [OSLogInt32ExtendedFormat](oslogint32extendedformat.md) — 32 位整数值的格式化选项。
- [OSLogPointerFormat](oslogpointerformat.md) — 指针数据的格式化选项。
