---
title: OS_LOG_TYPE_ERROR
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_error
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_error.json'
content_hash: 'sha256:f819d23de61ae45a'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_ERROR

<sub>枚举 case</sub>

Error 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_ERROR
```

## 讨论

记录此类型的消息等效于调用 [os_log_error](../os_log_error.md) 函数。使用此日志级别报告进程级错误。

Error 级别的消息始终保存到数据存储区。它们会一直保留在那里，直到超出存储配额，此时最旧的消息会被清除。如果存在活动对象，以此级别记录日志会捕获整个进程链的信息。
