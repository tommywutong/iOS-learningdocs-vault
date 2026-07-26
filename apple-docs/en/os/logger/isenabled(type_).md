---
title: 'isEnabled(type:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/isenabled(type:)'
source_url: 'https://developer.apple.com/documentation/os/logger/isenabled(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/isenabled%28type%3A%29.json'
content_hash: 'sha256:f5441e7d6d6654ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# isEnabled(type:)

<sub>Instance Method</sub>

Checks if the Logger can emit log messages for a given log type. This allows for more granular control over logging based on the log level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEnabled(type: OSLogType) -> Bool
```

## Parameters

- `type` — The log type to check (e.g., .default, .info, .debug, .error, .fault)

## Return Value

True if logging is enabled for the specified log type, false otherwise
