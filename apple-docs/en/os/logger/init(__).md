---
title: 'init(_:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/init(_:)'
source_url: 'https://developer.apple.com/documentation/os/logger/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/init%28_%3A%29.json'
content_hash: 'sha256:d4333b02a05d6286'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# init(_:)

<sub>Initializer</sub>

Creates a logger that writes to the specified log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ logObj: OSLog)
```

## Parameters

- `logObj` — The log to write messages to.

## See Also

### Creating a Logger

- [init()](<init().md>) — Creates a logger that writes to the default subsystem.
- [init(subsystem:category:)](<init(subsystem_category_).md>) — Creates a logger using the specified subsystem and category.
- [OSLog](../oslog.md) — A container of related log messages.
