---
title: OS_LOG_TYPE_DEFAULT
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_default
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_default.json'
content_hash: 'sha256:d3eafc4d6a7e8e11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_DEFAULT

<sub>Enumeration Case</sub>

The default log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_DEFAULT
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log](../os_log.md) function. Use this level to capture information about things that might result in a failure.

Default-level messages are initially stored in memory buffers. Without a configuration change, they are compressed and moved to the data store as memory buffers fill. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged.
