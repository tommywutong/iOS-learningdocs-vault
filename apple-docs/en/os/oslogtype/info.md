---
title: info
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/info
source_url: 'https://developer.apple.com/documentation/os/oslogtype/info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/info.json'
content_hash: 'sha256:7093f1f37ccba2c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# info

<sub>Type Property</sub>

The informative log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let info: OSLogType
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log_info](../os_log_info.md) function. Use this level to capture information that may be helpful, but not essential, for troubleshooting errors.

The system stores info-level messages in memory buffers and, without a configuration change, purges the oldest messages as those buffers fill up. However, the system writes the messages to the data store when faults and, optionally, errors occur. Info-level messages remain in the data store until the store’s size exceeds its storage quota, at which point, the system purges the oldest messages in the data store to free up space.

## See Also

### Getting Log Types

- [debug](debug.md) — The debug log level.
- [default](default.md) — The default log level.
- [error](error.md) — The error log level.
- [fault](fault.md) — The fault log level.
