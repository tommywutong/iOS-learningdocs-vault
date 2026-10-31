---
title: os_log_with_type
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_with_type
source_url: 'https://developer.apple.com/documentation/os/os_log_with_type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_with_type.json'
content_hash: 'sha256:c45a2d8ee2249115'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_log_with_type

<sub>宏</sub>

以特定日志级别（例如 default、info、debug、error 或 fault）向日志系统发送一条消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log_with_type(log, type, format, ...)
```

## 参数

- `log` — [OS_LOG_DEFAULT](os_log_default.md) 常量，或之前由 [os_log_create](os_log_create.md) 函数创建的自定义日志对象。

- `type` — 日志类型常量，例如 [OS_LOG_TYPE_DEFAULT](os_log_type_t/os_log_type_default.md)、[OS_LOG_TYPE_INFO](os_log_type_t/os_log_type_info.md)、[OS_LOG_TYPE_DEBUG](os_log_type_t/os_log_type_debug.md)、[OS_LOG_TYPE_ERROR](os_log_type_t/os_log_type_error.md) 或 [OS_LOG_TYPE_FAULT](os_log_type_t/os_log_type_fault.md)，用于指定要执行的日志记录级别。

- `format` — 产生人类可读日志消息的常量字符串或格式字符串。参见 [字符串格式说明符](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265)。

## 讨论

调用此函数并不能确保系统会记录一条消息。日志记录始终按照所提供日志对象和日志类型的行为设置进行。请注意，日志系统在存储冗长的日志消息时可能会对其进行截断。

## 另请参阅

### 相关文档

- [os_log_type_t](../kernel/os_log_type_t.md)

### 日志消息

- [消息参数格式化器](message-argument-formatters.md) — 使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。
- [遗留的日志记录符号](legacy-logging-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [os_log_t](os-log-t.md) — 一个日志对象，你将其传给日志记录函数，以便向该日志发送消息。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
- [os_log](os_log.md) — 向日志系统发送一条默认级别的消息。
- [os_log_info](os_log_info.md) — 向日志系统发送一条 info 级别的消息。
- [os_log_debug](os_log_debug.md) — 向日志系统发送一条 debug 级别的消息。
- [os_log_error](os_log_error.md) — 向日志系统发送一条 error 级别的消息。
- [os_log_fault](os_log_fault.md) — 向日志系统发送一条 fault 级别的消息。
