---
title: disabled
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog/disabled
source_url: 'https://developer.apple.com/documentation/os/oslog/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/disabled.json'
content_hash: 'sha256:c92cf668fd221129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# disabled

<sub>Type Property</sub>

The shared disabled log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let disabled: OSLog
```

## Discussion

Passing this constant to an `os_log` function prevents the system from logging a message.

## See Also

### Getting the Shared Logs

- [default](default.md) — The shared default log.
