---
title: error
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/error
source_url: 'https://developer.apple.com/documentation/os/oslogtype/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/error.json'
content_hash: 'sha256:cd6441de4be7d54d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# error

<sub>Type Property</sub>

The error log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let error: OSLogType
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log_error](../os_log_error.md) function. Use this log level to report process-level errors.

The system always writes error-level messages to the data store. They remain in the store until its size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space. If an activity object exists, logging at this level captures information for the entire process chain.

## See Also

### Getting Log Types

- [debug](debug.md) — The debug log level.
- [info](info.md) — The informative log level.
- [default](default.md) — The default log level.
- [fault](fault.md) — The fault log level.
