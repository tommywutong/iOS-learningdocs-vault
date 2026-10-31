---
title: 'octal(explicitPositiveSign:includePrefix:uppercase:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogintegerformatting/octal(explicitpositivesign:includeprefix:uppercase:)'
source_url: 'https://developer.apple.com/documentation/os/oslogintegerformatting/octal(explicitpositivesign:includeprefix:uppercase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogintegerformatting/octal%28explicitpositivesign%3Aincludeprefix%3Auppercase%3A%29.json'
content_hash: 'sha256:7b2d0a9dcfe6eea6'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogIntegerFormatting](../oslogintegerformatting.md)

# octal(explicitPositiveSign:includePrefix:uppercase:)

<sub>类型方法</sub>

创建自定义八进制格式，显示数字中的精确位数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func octal(explicitPositiveSign: Bool = false, includePrefix: Bool = false, uppercase: Bool = false) -> OSLogIntegerFormatting
```

## 参数

- `explicitPositiveSign` — 一个布尔值，指示是否在正整数前面显示加号（`+`）。

- `includePrefix` — 一个布尔值，指示是否为八进制数包含前导 `0o`。

- `uppercase` — 一个布尔值，指示是否将大于 9 的数码转为大写。

## 返回值

整数的自定义八进制格式。

## 另请参阅

### 创建自定义整数格式

- [decimal(explicitPositiveSign:)](<decimal(explicitpositivesign_).md>) — 创建对数值符号进行自定义处理的十进制格式。
- [decimal(explicitPositiveSign:minDigits:)](<decimal(explicitpositivesign_mindigits_).md>) — 创建对数值符号和最小位数进行自定义处理的十进制格式。
- [hex(explicitPositiveSign:includePrefix:uppercase:)](<hex(explicitpositivesign_includeprefix_uppercase_).md>) — 创建自定义十六进制格式，显示数字中的精确位数。
- [hex(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<hex(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — 创建包含最小位数的自定义十六进制格式。
- [octal(explicitPositiveSign:includePrefix:uppercase:minDigits:)](<octal(explicitpositivesign_includeprefix_uppercase_mindigits_).md>) — 创建包含最小位数的自定义八进制格式。
