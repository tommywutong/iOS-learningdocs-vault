---
title: OSLogPrivacy
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy.json'
content_hash: 'sha256:b64cefc058e015e8'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogPrivacy

<sub>结构体</sub>

决定何时在日志消息中隐去或显示值的隐私选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogPrivacy
```

## 概述

[OSLogPrivacy](oslogprivacy.md) 结构体决定了日志消息中插值的可见性。因为人们可以访问你的 App 生成的日志消息，请使用隐私选项来隐藏可能敏感的信息。例如，你可能会用它来隐藏账户信息或个人数据。

使用可用的属性和方法获取适当配置的此结构体版本，并在日志消息中与插值一起传入。下面的示例展示了如何将包含用户银行账户信息的变量标记为私有：

```swift
Logger().info("User bank account number: \(accountNumber, privacy: .private)")
```

当你想用原始值的哈希版本替换通用的隐去字符串时，请使用 [auto(mask:)](<oslogprivacy/auto(mask_).md>)、[private(mask:)](<oslogprivacy/private(mask_).md>) 和 [sensitive(mask:)](<oslogprivacy/sensitive(mask_).md>) 方法来指定隐私选项。使用哈希字符串可以关联包含相同原始值的日志消息，这有助于你保护用户隐私，同时仍能诊断与特定值相关的问题。

## 主题

### 获取隐私选项

- [auto](oslogprivacy/auto.md) — 让系统决定是隐去还是显示值的标准选项。
- [private](oslogprivacy/private.md) — 始终隐去插值的标准选项。
- [public](oslogprivacy/public.md) — 始终显示插值的标准选项。
- [sensitive](oslogprivacy/sensitive.md) — 始终隐去包含敏感信息的插值的选项。

### 创建自定义隐私掩码

- [auto(mask:)](<oslogprivacy/auto(mask_).md>) — 返回一个按类型决定是隐去还是显示值，并自定义被隐去值显示方式的隐私结构体。
- [private(mask:)](<oslogprivacy/private(mask_).md>) — 返回一个将插值标记为私有，并自定义被隐去值显示方式的隐私结构体。
- [sensitive(mask:)](<oslogprivacy/sensitive(mask_).md>) — 返回一个将插值标记为敏感，并自定义被隐去值显示方式的隐私结构体。
- [Mask](oslogprivacy/mask.md) — 规定系统如何在日志消息中显示被隐去值的掩码。
