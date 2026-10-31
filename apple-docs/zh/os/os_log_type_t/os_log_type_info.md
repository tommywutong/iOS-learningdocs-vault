---
title: OS_LOG_TYPE_INFO
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_info
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_info.json'
content_hash: 'sha256:4b87c97dd5d4bcea'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_INFO

<sub>枚举 case</sub>

Info 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_INFO
```

## 讨论

记录此类型的消息等效于调用 [os_log_info](../os_log_info.md) 函数。使用此级别可捕获对排查错误有帮助、但非必需的信息。

Info 级别的消息最初存储在内存缓冲区中。在未更改配置的情况下，随着内存缓冲区填满，它们会被清除。不过，在发生 fault 时（以及可选地在发生 error 时），它们会被捕获到数据存储区。当 info 级别的消息被添加到数据存储区后，它们会一直保留在那里，直到超出存储配额，此时最旧的消息会被清除。
