---
title: default
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog/default
source_url: 'https://developer.apple.com/documentation/os/oslog/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/default.json'
content_hash: 'sha256:58be0f19c43bba0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# default

<sub>Type Property</sub>

The shared default log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: OSLog
```

## Discussion

Passing this constant to an `os_log` function causes the system to log a message with the system’s standard behavior.

## See Also

### Getting the Shared Logs

- [disabled](disabled.md) — The shared disabled log.
