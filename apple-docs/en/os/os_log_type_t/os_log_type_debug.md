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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_DEBUG

<sub>Enumeration Case</sub>

The debug log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_DEBUG
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log_debug](../os_log_debug.md) function. Use this level to capture information that may be useful during development or while troubleshooting a specific problem.

Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting.
