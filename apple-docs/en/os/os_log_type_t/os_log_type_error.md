---
title: OS_LOG_TYPE_ERROR
framework: os
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_type_t/os_log_type_error
source_url: 'https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_type_t/os_log_type_error.json'
content_hash: 'sha256:f819d23de61ae45a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# OS_LOG_TYPE_ERROR

<sub>Enumeration Case</sub>

The error log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
OS_LOG_TYPE_ERROR
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log_error](../os_log_error.md) function. Use this log level to report process-level errors.

Error-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. If an activity object exists, logging at this level captures information for the entire process chain.
