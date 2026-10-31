---
title: default
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog/default
source_url: 'https://developer.apple.com/documentation/os/oslog/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/default.json'
content_hash: 'sha256:58be0f19c43bba0e'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# default

<sub>类型属性</sub>

共享的默认日志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: OSLog
```

## 讨论

将此常量传给某个 `os_log` 函数，会使系统按标准行为记录一条消息。

## 另请参阅

### 获取共享日志

- [disabled](disabled.md) — 共享的已禁用日志。
