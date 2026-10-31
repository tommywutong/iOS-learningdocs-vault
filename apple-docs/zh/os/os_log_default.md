---
title: OS_LOG_DEFAULT
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_default
source_url: 'https://developer.apple.com/documentation/os/os_log_default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_default.json'
content_hash: 'sha256:94dbcdc6c50d945d'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OS_LOG_DEFAULT

<sub>宏</sub>

共享的默认日志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_LOG_DEFAULT
```

## 讨论

将此常量传给某个 `os_log` 函数（例如 [os_log](os_log.md)、[os_log_info](os_log_info.md)、[os_log_debug](os_log_debug.md)、[os_log_error](os_log_error.md) 或 [os_log_fault](os_log_fault.md)），会使系统按标准行为记录一条消息。

## 另请参阅

### 获取标准日志对象

- [OS_LOG_DISABLED](os_log_disabled.md) — 共享的已禁用日志。
