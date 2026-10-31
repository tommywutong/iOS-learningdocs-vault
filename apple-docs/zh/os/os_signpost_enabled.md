---
title: os_signpost_enabled
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_enabled
source_url: 'https://developer.apple.com/documentation/os/os_signpost_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_enabled.json'
content_hash: 'sha256:a51a8657e6a0d466'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost_enabled

<sub>函数</sub>

返回一个布尔值，指示指定日志的 signpost 是否处于启用状态。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_signpost_enabled(os_log_t log);
```

## 参数

- `log` — [OS_LOG_DEFAULT](os_log_default.md) 常量，或你用 [os_log_create](os_log_create.md) 函数创建的自定义日志对象。

## 另请参阅

### 获取日志配置

- [os_log_info_enabled](os_log_info_enabled.md) — 返回一个布尔值，指示指定日志对象的 info 级别日志记录是否处于启用状态。
- [os_log_debug_enabled](os_log_debug_enabled.md) — 返回一个布尔值，指示指定日志对象的 debug 级别日志记录是否处于启用状态。
- [os_log_type_enabled](<oslog/isenabled(type_).md>) — 返回一个布尔值，指示该日志是否可以写入指定日志类型的消息。
