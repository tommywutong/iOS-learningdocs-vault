---
title: OSLogPrivacy.Mask.none
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/mask/none
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/mask/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/mask/none.json'
content_hash: 'sha256:77ddd6cddc4e5c51'
translated: true
---

> 导航：[技术](../../../technologies.md) · [os](../../../os.md) · [OSLogPrivacy](../../oslogprivacy.md) · [Mask](../mask.md)

# OSLogPrivacy.Mask.none

<sub>Case</sub>

将被隐去的值替换为通用字符串的选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case none
```

## 讨论

当你不想关联具有相同被隐去值的日志消息时，请使用此选项。

## 另请参阅

### 隐私掩码选项

- [OSLogPrivacy.Mask.hash](hash.md) — 将被隐去的值替换为包含原值哈希版本的字符串的选项。
