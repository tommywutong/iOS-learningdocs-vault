---
title: os_log_debug
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_debug
source_url: 'https://developer.apple.com/documentation/os/os_log_debug'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_debug.json'
content_hash: 'sha256:b8109b3ef0e9911f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_log_debug

<sub>Macro</sub>

Sends a debug-level message to the logging system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log_debug(log, format, ...)
```

## Parameters

- `log` — The [OS_LOG_DEFAULT](os_log_default.md) constant or a custom log object previously created by the [os_log_create](os_log_create.md) function.

- `format` — A constant string or format string that produces a human-readable log message. See [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

## Discussion

Calling this function is equivalent to calling the `os_log_with_type` function and specifying a log type of [OS_LOG_TYPE_DEBUG](../kernel/os_log_type_t/os_log_type_debug.md).

## See Also

### Related Documentation

- [OS_LOG_TYPE_DEBUG](../kernel/os_log_type_t/os_log_type_debug.md) — Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting. Messages logged at this level contain information that may be useful during development or while troubleshooting a specific problem. Debug logging is intended for use in a development environment and not in shipping software. Logging a message of this type is equivalent to calling the  function.

### Log Messages

- [Message Argument Formatters](message-argument-formatters.md) — Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [Legacy Logging Symbols](legacy-logging-symbols.md) — Migrate your code away from using these legacy symbols.
- [os_log_t](os-log-t.md) — A log object that you pass to logging functions to send messages to that log.
- [os_log_with_type](os_log_with_type.md) — Sends a message at a specific logging level, such as default, info, debug, error, or fault, to the logging system.
- [OSLogType](oslogtype.md) — The various log levels that the unified logging system provides.
- [os_log](os_log.md) — Sends a default-level message to the logging system.
- [os_log_info](os_log_info.md) — Sends an info-level message to the logging system.
- [os_log_error](os_log_error.md) — Sends an error-level message to the logging system.
- [os_log_fault](os_log_fault.md) — Sends a fault-level message to the logging system.
