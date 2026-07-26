---
title: OS_LOG_TYPE_INFO
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_info
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_info.json'
content_hash: 'sha256:4b87c97dd5d4bcea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_INFO

<sub>Enumeration Case</sub>

The informational log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_INFO
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log_info](../os_log_info.md) function. Use this level to capture information that may be helpful, but not essential, for troubleshooting errors.

Info-level messages are initially stored in memory buffers. Without a configuration change, they are purged as memory buffers fill. They are, however, captured in the data store when faults and, optionally, errors occur. When info-level messages are added to the data store, they remain there until a storage quota is exceeded, at which point, the oldest messages are purged.
