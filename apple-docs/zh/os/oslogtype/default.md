---
title: default
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/default
source_url: 'https://developer.apple.com/documentation/os/oslogtype/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/default.json'
content_hash: 'sha256:f9c0b4d5b7772d7c'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# default

<sub>类型属性</sub>

default 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: OSLogType
```

## 讨论

记录此类型的消息等效于调用 [os_log](../os_log.md) 函数。使用此级别捕获关于可能导致失败的情况的信息。

系统将 default 级别的消息存储在内存缓冲区中，并且在未更改配置的情况下，随着这些缓冲区填满，会压缩消息并将它们写入数据存储区。它们会一直保留在数据存储区中，直到存储区大小超出其存储配额；此时，系统会清除存储区中最旧的消息以释放空间。

## 另请参阅

### 获取日志类型

- [debug](debug.md) — debug 日志级别。
- [info](info.md) — info 日志级别。
- [error](error.md) — error 日志级别。
- [fault](fault.md) — fault 日志级别。
