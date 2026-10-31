---
title: os_log_error
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_error
source_url: 'https://developer.apple.com/documentation/os/os_log_error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_error.json'
content_hash: 'sha256:46a0e6ecf1506871'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_log_error

<sub>宏</sub>

向日志系统发送一条 error 级别的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log_error(log, format, ...)
```

## 参数

- `log` — [OS_LOG_DEFAULT](os_log_default.md) 常量，或之前由 [os_log_create](os_log_create.md) 函数创建的自定义日志对象。

- `format` — 产生人类可读日志消息的常量字符串或格式字符串。参见 [字符串格式说明符](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265)。

## 讨论

调用此函数等效于调用 [os_log_with_type](os_log_with_type.md) 函数，并将日志类型指定为 [OS_LOG_TYPE_ERROR](../kernel/os_log_type_t/os_log_type_error.md)。

## 另请参阅

### 相关文档

- [OS_LOG_TYPE_ERROR](../kernel/os_log_type_t/os_log_type_error.md) — Error 级别的消息总会保存到数据存储中。它们会一直保留，直到超出存储配额；此时会清除最旧的消息。Error 级别的消息用于报告进程级错误。如果存在活动对象，在此级别进行日志记录会捕获整个进程链的信息。记录此类型的消息等效于调用  函数。

### 日志消息

- [Message Argument Formatters](message-argument-formatters.md) — 使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。
- [Legacy Logging Symbols](legacy-logging-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [os_log_t](os-log-t.md) — 一个日志对象，你将其传给日志记录函数，以便向该日志发送消息。
- [os_log_with_type](os_log_with_type.md) — 以特定日志级别（例如 default、info、debug、error 或 fault）向日志系统发送一条消息。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
- [os_log](os_log.md) — 向日志系统发送一条 default 级别的消息。
- [os_log_info](os_log_info.md) — 向日志系统发送一条 info 级别的消息。
- [os_log_debug](os_log_debug.md) — 向日志系统发送一条 debug 级别的消息。
- [os_log_fault](os_log_fault.md) — 向日志系统发送一条 fault 级别的消息。
