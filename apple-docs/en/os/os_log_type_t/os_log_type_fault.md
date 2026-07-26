---
title: OS_LOG_TYPE_FAULT
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_fault
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_fault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_fault.json'
content_hash: 'sha256:65db421f1758d9ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_FAULT

<sub>Enumeration Case</sub>

The fault log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_FAULT
```

## Discussion

Logging a message at this level is equivalent to calling the [os_log_fault](../os_log_fault.md) function. Use this level only to capture system-level or multi-process information when reporting system errors.

Fault-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. If an activity object exists, logging at this level captures information for the entire process chain.
