---
title: os_log
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log
source_url: 'https://developer.apple.com/documentation/os/os_log'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log.json'
content_hash: 'sha256:a561c993a05512fc'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_log

<sub>宏</sub>

向日志系统发送一条默认级别的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log(log, format, ...)
```

## 参数

- `log` — [OS_LOG_DEFAULT](os_log_default.md) 常量，或之前由 [os_log_create](os_log_create.md) 函数创建的自定义日志对象。

- `format` — 产生人类可读日志消息的常量字符串或格式字符串。参见 [字符串格式说明符](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265)。

## 讨论

调用此函数等效于调用 [os_log_with_type](os_log_with_type.md) 函数，并将日志类型指定为 [OS_LOG_TYPE_DEFAULT](../kernel/os_log_type_t/os_log_type_default.md)。

## 另请参阅

### 日志消息

- [Message Argument Formatters](message-argument-formatters.md) — 使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。
- [Legacy Logging Symbols](legacy-logging-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [os_log_t](os-log-t.md) — 一个日志对象，你将其传给日志记录函数，以便向该日志发送消息。
- [os_log_with_type](os_log_with_type.md) — 以特定日志级别（例如 default、info、debug、error 或 fault）向日志系统发送一条消息。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
- [os_log_info](os_log_info.md) — 向日志系统发送一条 info 级别的消息。
- [os_log_debug](os_log_debug.md) — 向日志系统发送一条 debug 级别的消息。
- [os_log_error](os_log_error.md) — 向日志系统发送一条 error 级别的消息。
- [os_log_fault](os_log_fault.md) — 向日志系统发送一条 fault 级别的消息。
