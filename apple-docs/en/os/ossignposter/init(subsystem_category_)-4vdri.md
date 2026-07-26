---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/init(subsystem:category:)-4vdri'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/init(subsystem:category:)-4vdri'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/init%28subsystem%3Acategory%3A%29-4vdri.json'
content_hash: 'sha256:881b7c8587900c65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# init(subsystem:category:)

<sub>Initializer</sub>

Creates a signposter that uses the specified subsystem and system-defined log category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(subsystem: String, category: OSLog.Category)
```

## Parameters

- `subsystem` — The string that identifies the subsystem that emits signposts. Typically, you use the same value as your app’s _bundle ID_. For more information, see [CFBundleIdentifier](../../bundleresources/information-property-list/cfbundleidentifier.md).

- `category` — The system-defined category, which the system uses to categorize emitted signposts. For possible values, see [Category](../oslog/category.md).

## See Also

### Creating a Signposter

- [init()](<init().md>) — Creates a signposter that uses the default subsystem.
- [init(subsystem:category:)](<init(subsystem_category_)-94xpb.md>) — Creates a signposter that uses the specified subsystem and category.
- [init(logger:)](<init(logger_).md>) — Creates a signposter that uses the subsystem and category of an existing logger.
- [init(logHandle:)](<init(loghandle_).md>) — Creates a signposter that uses the subsystem and category of an existing log.
- [disabled](disabled.md) — A shared signposter that doesn’t emit signposts at runtime.
