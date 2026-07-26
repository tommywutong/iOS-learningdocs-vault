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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OS_LOG_DEFAULT

<sub>Macro</sub>

The shared default log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OS_LOG_DEFAULT
```

## Discussion

Passing this constant to an `os_log` function, such as [os_log](os_log.md), [os_log_info](os_log_info.md), [os_log_debug](os_log_debug.md), [os_log_error](os_log_error.md), or [os_log_fault](os_log_fault.md), causes the system to log a message with the system’s standard behavior.

## See Also

### Getting the Standard Log Objects

- [OS_LOG_DISABLED](os_log_disabled.md) — The shared disabled log.
