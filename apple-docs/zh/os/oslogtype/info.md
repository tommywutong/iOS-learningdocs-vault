---
title: info
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/info
source_url: 'https://developer.apple.com/documentation/os/oslogtype/info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/info.json'
content_hash: 'sha256:7093f1f37ccba2c6'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# info

<sub>类型属性</sub>

info 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let info: OSLogType
```

## 讨论

记录此类型的消息等效于调用 [os_log_info](../os_log_info.md) 函数。使用此级别捕获对排查错误有帮助、但非必需的信息。

系统将 info 级别的消息存储在内存缓冲区中，并且在未更改配置的情况下，随着这些缓冲区填满，会清除最旧的消息。不过，在发生 fault 时，以及可选地在发生 error 时，系统会将这些消息写入数据存储区。info 级别的消息会一直保留在数据存储区中，直到存储区大小超出其存储配额；此时，系统会清除数据存储区中最旧的消息以释放空间。

## 另请参阅

### 获取日志类型

- [debug](debug.md) — debug 日志级别。
- [default](default.md) — default 日志级别。
- [error](error.md) — error 日志级别。
- [fault](fault.md) — fault 日志级别。
