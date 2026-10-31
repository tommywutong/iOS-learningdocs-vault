---
title: OSLogPrivacy.Mask
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/mask
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/mask.json'
content_hash: 'sha256:da4c73f9a9d46ac1'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# OSLogPrivacy.Mask

<sub>枚举</sub>

用于确定系统如何在日志消息中显示被隐去值的掩码。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Mask
```

## 关系

- **遵循**： [Equatable](../../swift/equatable.md)、[Hashable](../../swift/hashable.md)

## 主题

### 隐私掩码选项

- [OSLogPrivacy.Mask.hash](mask/hash.md) — 将被隐去的值替换为包含原值哈希版本的字符串的选项。
- [OSLogPrivacy.Mask.none](mask/none.md) — 将被隐去的值替换为通用字符串的选项。

## 另请参阅

### 创建自定义隐私掩码

- [auto(mask:)](<auto(mask_).md>) — 返回一个隐私结构体，按值的类型决定是隐去还是显示，并自定义被隐去值的显示方式。
- [private(mask:)](<private(mask_).md>) — 返回一个将插值标记为私有，并自定义被隐去值显示方式的隐私结构体。
- [sensitive(mask:)](<sensitive(mask_).md>) — 返回一个将插值标记为敏感，并自定义被隐去值显示方式的隐私结构体。
