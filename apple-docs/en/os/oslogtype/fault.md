---
title: fault
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/fault
source_url: 'https://developer.apple.com/documentation/os/oslogtype/fault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/fault.json'
content_hash: 'sha256:f0b8f3e97d0b0a6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# fault

<sub>Type Property</sub>

The fault log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let fault: OSLogType
```

## Discussion

Logging a message at this level is equivalent to calling the [os_log_fault](../os_log_fault.md) function. Use this level only to capture system-level or multiprocess information when reporting system errors.

The system always writes fault-level messages to the data store. They remain in the store until its size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space. If an activity object exists, logging at this level captures information for the entire process chain.

## See Also

### Getting Log Types

- [debug](debug.md) — The debug log level.
- [info](info.md) — The informative log level.
- [default](default.md) — The default log level.
- [error](error.md) — The error log level.
