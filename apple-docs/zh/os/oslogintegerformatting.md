---
title: OSLogIntegerFormatting
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogintegerformatting
source_url: 'https://developer.apple.com/documentation/os/oslogintegerformatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogintegerformatting.json'
content_hash: 'sha256:0d8f00866e3d5c39'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogIntegerFormatting

<sub>结构体</sub>

整数值的格式化选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogIntegerFormatting
```

## 概述

[OSLogIntegerFormatting](oslogintegerformatting.md) 结构体封装了整数的格式化细节。使用静态的 [decimal](oslogintegerformatting/decimal.md)、[hex](oslogintegerformatting/hex.md) 和 [octal](oslogintegerformatting/octal.md) 结构体，可为整数值应用默认格式。你也可以创建新的 [OSLogIntegerFormatting](oslogintegerformatting.md) 结构体，自定义如何处理前导正号、特殊数值前缀、最少位数等规则。

## 主题

### 获取标准格式

- [decimal](oslogintegerformatting/decimal.md) — 标准十进制格式选项。
- [hex](oslogintegerformatting/hex.md) — 标准十六进制格式选项。
- [octal](oslogintegerformatting/octal.md) — 标准八进制格式选项。

### 创建自定义整数格式

- [decimal(explicitPositiveSign:)](<oslogintegerformatting/decimal(explicitpositivesign_).md>) — 创建对数值符号有自定义处理的十进制格式。
- [decimal(explicitPositiveSign:minDigits:)](<oslogintegerformatting/decimal(explicitpositivesign_mindigits_).md>) — 创建对数值符号和最少位数有自定义处理的十进制格式。
- [hex(explicitPositiveSign:includePrefix:uppercase:)](<oslogintegerformatting/hex(explicitpositivesign_includeprefix_uppercase_).md>) — 创建显示数字精确位数的自定义十六进制格式。
- [hex(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<oslogintegerformatting/hex(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — 创建包含最少位数的自定义十六进制格式。
- [octal(explicitPositiveSign:includePrefix:uppercase:)](<oslogintegerformatting/octal(explicitpositivesign_includeprefix_uppercase_).md>) — 创建显示数字精确位数的自定义八进制格式。
- [octal(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<oslogintegerformatting/octal(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — 创建包含最少位数的自定义八进制格式。

## 另请参阅

### 值格式化器

- [OSLogBoolFormat](oslogboolformat.md) — 布尔值的格式化选项。
- [OSLogInt32ExtendedFormat](oslogint32extendedformat.md) — 32 位整数值的格式化选项。
- [OSLogFloatFormatting](oslogfloatformatting.md) — double 和浮点数的格式化选项。
- [OSLogPointerFormat](oslogpointerformat.md) — 指针数据的格式化选项。
