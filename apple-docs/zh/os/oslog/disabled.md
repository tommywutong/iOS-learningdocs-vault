---
title: disabled
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog/disabled
source_url: 'https://developer.apple.com/documentation/os/oslog/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/disabled.json'
content_hash: 'sha256:c92cf668fd221129'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# disabled

<sub>类型属性</sub>

共享的已禁用日志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let disabled: OSLog
```

## 讨论

将此常量传给某个 `os_log` 函数，可阻止系统记录消息。

## 另请参阅

### 获取共享日志

- [default](default.md) — 共享的默认日志。
