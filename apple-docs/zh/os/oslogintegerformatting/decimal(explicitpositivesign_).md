---
title: 'decimal(explicitPositiveSign:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogintegerformatting/decimal(explicitpositivesign:)'
source_url: 'https://developer.apple.com/documentation/os/oslogintegerformatting/decimal(explicitpositivesign:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogintegerformatting/decimal%28explicitpositivesign%3A%29.json'
content_hash: 'sha256:a0d09ff6b8a10805'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogIntegerFormatting](../oslogintegerformatting.md)

# decimal(explicitPositiveSign:)

<sub>类型方法</sub>

创建对数值符号有自定义处理的十进制格式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decimal(explicitPositiveSign: Bool = false) -> OSLogIntegerFormatting
```

## 参数

- `explicitPositiveSign` — 一个布尔值，指示是否在正整数前面显示加号（`+`）。

## 返回值

整数的自定义十进制格式。

## 另请参阅

### 创建自定义整数格式

- [decimal(explicitPositiveSign:minDigits:)](<decimal(explicitpositivesign_mindigits_).md>) — 创建对数值符号和最少位数有自定义处理的十进制格式。
- [hex(explicitPositiveSign:includePrefix:uppercase:)](<hex(explicitpositivesign_includeprefix_uppercase_).md>) — 创建显示数字精确位数的自定义十六进制格式。
- [hex(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<hex(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — 创建包含最少位数的自定义十六进制格式。
- [octal(explicitPositiveSign:includePrefix:uppercase:)](<octal(explicitpositivesign_includeprefix_uppercase_).md>) — 创建显示数字精确位数的自定义八进制格式。
- [octal(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<octal(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — 创建包含最少位数的自定义八进制格式。
