---
title: os_log_debug_enabled
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_debug_enabled
source_url: 'https://developer.apple.com/documentation/os/os_log_debug_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_debug_enabled.json'
content_hash: 'sha256:8404d10dac90ac37'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_log_debug_enabled

<sub>宏</sub>

返回一个布尔值，指示指定日志对象的 debug 级别日志记录是否处于启用状态。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log_debug_enabled(log)
```

## 参数

- `log` — [OS_LOG_DEFAULT](os_log_default.md) 常量，或你用 [os_log_create](os_log_create.md) 函数创建的自定义日志对象。

## 返回值

若 debug 级别日志记录处于启用状态，则为 [true](../swift/true.md)；否则为 [false](../swift/false.md)。

## 另请参阅

### 相关文档

- [OS_LOG_TYPE_DEBUG](../kernel/os_log_type_t/os_log_type_debug.md) — debug 级别的消息仅在通过配置更改启用 debug 日志记录时才会捕获到内存中。它们会按配置的持久化设置被清除。此级别记录的消息包含在开发期间或排查特定问题时可能有用的信息。debug 日志记录旨在用于开发环境，而非交付软件。记录此类型的消息等效于调用该函数。

### 获取日志配置

- [os_log_info_enabled](os_log_info_enabled.md) — 返回一个布尔值，指示指定日志对象的 info 级别日志记录是否处于启用状态。
- [os_log_type_enabled](<oslog/isenabled(type_).md>) — 返回一个布尔值，指示该日志是否可以写入指定日志类型的消息。
- [os_signpost_enabled](os_signpost_enabled.md) — 返回一个布尔值，指示指定日志的 signpost 是否处于启用状态。
