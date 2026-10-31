---
title: OS_LOG_DISABLED
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_disabled
source_url: 'https://developer.apple.com/documentation/os/os_log_disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_disabled.json'
content_hash: 'sha256:03fb5cf7f6213566'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OS_LOG_DISABLED

<sub>宏</sub>

共享的已禁用日志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_LOG_DISABLED
```

## 讨论

将此常量传给某个 `os_log` 函数（例如 `os_log`、`os_log_info`、`os_log_debug`、`os_log_error` 或 `os_log_fault`），可阻止系统记录消息。

## 另请参阅

### 获取标准日志对象

- [OS_LOG_DEFAULT](os_log_default.md) — 共享的默认日志。
