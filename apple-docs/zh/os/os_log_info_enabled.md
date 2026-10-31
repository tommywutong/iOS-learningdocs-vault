---
title: os_log_info_enabled
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_info_enabled
source_url: 'https://developer.apple.com/documentation/os/os_log_info_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_info_enabled.json'
content_hash: 'sha256:0b9ded35928578f9'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_log_info_enabled

<sub>宏</sub>

返回一个布尔值，指示指定日志对象的 info 级别日志记录是否处于启用状态。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log_info_enabled(log)
```

## 参数

- `log` — [OS_LOG_DEFAULT](os_log_default.md) 常量，或你用 [os_log_create](os_log_create.md) 函数创建的自定义日志对象。

## 返回值

若 info 级别日志记录处于启用状态，则为 [true](../swift/true.md)；否则为 [false](../swift/false.md)。

## 另请参阅

### 相关文档

- [OS_LOG_TYPE_INFO](../kernel/os_log_type_t/os_log_type_info.md) — Info 级别的消息最初存放在内存缓冲区中。若不更改配置，它们不会移入数据存储，并会在内存缓冲区填满时被清除。不过，当发生 fault，以及（可选地）发生 error 时，它们会被捕获到数据存储中。当 info 级别的消息被加入数据存储后，它们会一直保留，直到超出存储配额；此时会清除最旧的消息。使用此级别来捕获可能有助于排查错误、但并非必需的信息。记录此类型的消息等效于调用  函数。

### 获取日志配置

- [os_log_debug_enabled](os_log_debug_enabled.md) — 返回一个布尔值，指示指定日志对象的 debug 级别日志记录是否处于启用状态。
- [os_log_type_enabled](<oslog/isenabled(type_).md>) — 返回一个布尔值，指示该日志是否可以写入指定日志类型的消息。
- [os_signpost_enabled](os_signpost_enabled.md) — 返回一个布尔值，指示指定日志的 signpost 是否处于启用状态。
