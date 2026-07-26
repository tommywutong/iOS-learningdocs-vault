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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OS_LOG_DISABLED

<sub>Macro</sub>

The shared disabled log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_LOG_DISABLED
```

## Discussion

Passing this constant to an `os_log` function, such as `os_log`, `os_log_info`, `os_log_debug`, `os_log_error`, or `os_log_fault`, prevents the system from logging a message.

## See Also

### Getting the Standard Log Objects

- [OS_LOG_DEFAULT](os_log_default.md) — The shared default log.
