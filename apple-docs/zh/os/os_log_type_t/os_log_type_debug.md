---
title: OS_LOG_TYPE_DEBUG
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_debug
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_debug'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_debug.json'
content_hash: 'sha256:ff8c9ef690769087'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_DEBUG

<sub>枚举 case</sub>

Debug 日志级别。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_DEBUG
```

## 讨论

记录此类型的消息等效于调用 [os_log_debug](../os_log_debug.md) 函数。使用此级别可捕获在开发期间或排查特定问题时可能有用的信息。

仅当通过配置更改启用了 debug 日志记录时，才会在内存中捕获 debug 级别的消息。它们会根据配置的持久化设置被清除。
