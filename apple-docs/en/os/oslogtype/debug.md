---
title: debug
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype/debug
source_url: 'https://developer.apple.com/documentation/os/oslogtype/debug'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype/debug.json'
content_hash: 'sha256:4505697207c73845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogType](../oslogtype.md)

# debug

<sub>Type Property</sub>

The debug log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let debug: OSLogType
```

## Discussion

Logging a message of this type is equivalent to calling the [os_log_debug](../os_log_debug.md) function. Use this level to capture information that may be useful during development or while troubleshooting a specific problem.

The system only captures debug-level messages in memory when you enable debug logging through a configuration change, and purges them in accordance with the configuration’s persistence setting.

## See Also

### Getting Log Types

- [info](info.md) — The informative log level.
- [default](default.md) — The default log level.
- [error](error.md) — The error log level.
- [fault](fault.md) — The fault log level.
