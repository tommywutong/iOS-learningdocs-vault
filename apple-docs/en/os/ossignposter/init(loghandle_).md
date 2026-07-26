---
title: 'init(logHandle:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/init(loghandle:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/init(loghandle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/init%28loghandle%3A%29.json'
content_hash: 'sha256:f0d42375b61d331f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# init(logHandle:)

<sub>Initializer</sub>

Creates a signposter that uses the subsystem and category of an existing log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(logHandle: OSLog)
```

## Parameters

- `logHandle` — The log that provides a subsystem and category for the signposter to use. For more information, see [OSLog](../oslog.md).

## See Also

### Creating a Signposter

- [init()](<init().md>) — Creates a signposter that uses the default subsystem.
- [init(subsystem:category:)](<init(subsystem_category_)-94xpb.md>) — Creates a signposter that uses the specified subsystem and category.
- [init(subsystem:category:)](<init(subsystem_category_)-4vdri.md>) — Creates a signposter that uses the specified subsystem and system-defined log category.
- [init(logger:)](<init(logger_).md>) — Creates a signposter that uses the subsystem and category of an existing logger.
- [disabled](disabled.md) — A shared signposter that doesn’t emit signposts at runtime.
