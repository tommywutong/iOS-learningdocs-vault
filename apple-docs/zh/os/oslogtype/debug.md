---
title: debug
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/debug
source_url: 'https://developer.apple.com/documentation/os/oslogtype/debug'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/debug.json'
content_hash: 'sha256:4505697207c73845'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# debug

<sub>类型属性</sub>

debug 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let debug: OSLogType
```

## 讨论

记录此类型的消息等效于调用 [os_log_debug](../os_log_debug.md) 函数。使用此级别捕获在开发期间或排查特定问题时可能有用的信息。

仅当你通过配置更改启用 debug 日志记录时，系统才会把 debug 级别的消息捕获到内存中，并按配置的持久化设置清除它们。

## 另请参阅

### 获取日志类型

- [info](info.md) — info 日志级别。
- [default](default.md) — default 日志级别。
- [error](error.md) — error 日志级别。
- [fault](fault.md) — fault 日志级别。
