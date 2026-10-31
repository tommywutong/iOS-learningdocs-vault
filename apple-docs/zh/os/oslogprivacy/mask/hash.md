---
title: OSLogPrivacy.Mask.hash
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/mask/hash
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/mask/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/mask/hash.json'
content_hash: 'sha256:18b1ebe20bfe84fb'
translated: true
---

> 导航：[技术](../../../technologies.md) · [os](../../../os.md) · [OSLogPrivacy](../../oslogprivacy.md) · [Mask](../mask.md)

# OSLogPrivacy.Mask.hash

<sub>Case</sub>

将被隐去的值替换为包含原值哈希版本的字符串的选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case hash
```

## 讨论

当你希望在日志消息中隐藏可能敏感的数据，但仍想知道两条或多条日志消息是否包含相同的隐藏值时，请使用此选项。带有此选项的 [OSLogPrivacy](../../oslogprivacy.md) 结构体会为被隐去的值生成一个哈希字符串。系统会将该哈希字符串作为日志消息的一部分显示，从而让你可以比较具有相同值的日志消息。

## 另请参阅

### 隐私掩码选项

- [OSLogPrivacy.Mask.none](none.md) — 将被隐去的值替换为通用字符串的选项。
