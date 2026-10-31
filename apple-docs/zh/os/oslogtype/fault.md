---
title: fault
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/fault
source_url: 'https://developer.apple.com/documentation/os/oslogtype/fault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/fault.json'
content_hash: 'sha256:f0b8f3e97d0b0a6f'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# fault

<sub>类型属性</sub>

fault 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let fault: OSLogType
```

## 讨论

以此级别记录消息等效于调用 [os_log_fault](../os_log_fault.md) 函数。仅在报告系统错误时使用此级别，以捕获系统级或多进程信息。

系统始终将 fault 级别的消息写入数据存储区。它们会一直保留在存储区中，直到其大小超出存储配额；此时，系统会清除存储区中最旧的消息以释放空间。如果存在活动对象，以此级别记录日志会捕获整个进程链的信息。

## 另请参阅

### 获取日志类型

- [debug](debug.md) — debug 日志级别。
- [info](info.md) — info 日志级别。
- [default](default.md) — default 日志级别。
- [error](error.md) — error 日志级别。
