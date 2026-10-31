---
title: 'sensitive(mask:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogprivacy/sensitive(mask:)'
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/sensitive(mask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/sensitive%28mask%3A%29.json'
content_hash: 'sha256:412327d58d19e9ba'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# sensitive(mask:)

<sub>类型方法</sub>

返回一个将插值标记为敏感，并自定义被隐去值显示方式的隐私结构体。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func sensitive(mask: OSLogPrivacy.Mask) -> OSLogPrivacy
```

## 参数

- `mask` — 一个掩码，用于决定系统是用通用字符串，还是用被隐去值的哈希字符串来替换被隐去的值。

## 返回值

一个会隐去敏感值的隐私对象。

## 另请参阅

### 创建自定义隐私掩码

- [auto(mask:)](<auto(mask_).md>) — 返回一个按类型决定是隐去还是显示值，并自定义被隐去值显示方式的隐私结构体。
- [private(mask:)](<private(mask_).md>) — 返回一个将插值标记为私有，并自定义被隐去值显示方式的隐私结构体。
- [Mask](mask.md) — 规定系统如何在日志消息中显示被隐去值的掩码。
