---
title: OS_LOG_TYPE_DEFAULT
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_default
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_default.json'
content_hash: 'sha256:d3eafc4d6a7e8e11'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_DEFAULT

<sub>枚举 case</sub>

Default 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_DEFAULT
```

## 讨论

记录此类型的消息等效于调用 [os_log](../os_log.md) 函数。使用此级别可捕获关于可能导致失败的情况的信息。

Default 级别的消息最初存储在内存缓冲区中。在未更改配置的情况下，随着内存缓冲区填满，它们会被压缩并移至数据存储区。它们会一直保留在那里，直到超出存储配额，此时最旧的消息会被清除。
