---
title: default
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/default
source_url: 'https://developer.apple.com/documentation/os/oslogtype/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/default.json'
content_hash: 'sha256:f9c0b4d5b7772d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# default

<sub>Type Property</sub>

The default log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: OSLogType
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log](../os_log.md) function. Use this level to capture information about things that might result in a failure.

The system stores default-level messages in memory buffers and, without a configuration change, compresses the messages and writes them to the data store as those buffers fill up. They remain in the data store until the store’s size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space.

## See Also

### Getting Log Types

- [debug](debug.md) — The debug log level.
- [info](info.md) — The informative log level.
- [error](error.md) — The error log level.
- [fault](fault.md) — The fault log level.
