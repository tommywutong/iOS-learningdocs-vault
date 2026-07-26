---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/init(subsystem:category:)'
source_url: 'https://developer.apple.com/documentation/os/logger/init(subsystem:category:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/init%28subsystem%3Acategory%3A%29.json'
content_hash: 'sha256:9eb2e624a575879f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# init(subsystem:category:)

<sub>Initializer</sub>

Creates a logger using the specified subsystem and category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(subsystem: String, category: String)
```

## Parameters

- `subsystem` — The string that identifies the subsystem that emits signposts. Typically, you use the same value as your app’s _bundle ID_. For more information, see [CFBundleIdentifier](../../bundleresources/information-property-list/cfbundleidentifier.md).

- `category` — The string that the system uses to categorize emitted signposts.

## See Also

### Creating a Logger

- [init()](<init().md>) — Creates a logger that writes to the default subsystem.
- [init(_:)](<init(__).md>) — Creates a logger that writes to the specified log.
- [OSLog](../oslog.md) — A container of related log messages.
