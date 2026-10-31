---
title: 'auto(mask:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogprivacy/auto(mask:)'
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/auto(mask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/auto%28mask%3A%29.json'
content_hash: 'sha256:5e8dbf71dab1a94f'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# auto(mask:)

<sub>类型方法</sub>

返回一个隐私结构体，按值的类型决定是隐去还是显示，并自定义被隐去值的显示方式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func auto(mask: OSLogPrivacy.Mask) -> OSLogPrivacy
```

## 参数

- `mask` — 一个掩码，用于决定系统将被隐去的值替换为通用字符串，还是替换为由被隐去值的哈希生成的字符串。

## 返回值

应用默认隐去规则的隐私对象。

## 另请参阅

### 创建自定义隐私掩码

- [private(mask:)](<private(mask_).md>) — 返回一个将插值标记为私有，并自定义被隐去值显示方式的隐私结构体。
- [sensitive(mask:)](<sensitive(mask_).md>) — 返回一个将插值标记为敏感，并自定义被隐去值显示方式的隐私结构体。
- [Mask](mask.md) — 用于确定系统如何在日志消息中显示被隐去值的掩码。
