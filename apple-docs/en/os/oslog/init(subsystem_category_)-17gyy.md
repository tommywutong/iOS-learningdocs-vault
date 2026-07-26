---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslog/init(subsystem:category:)-17gyy'
source_url: 'https://developer.apple.com/documentation/os/oslog/init(subsystem:category:)-17gyy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/init%28subsystem%3Acategory%3A%29-17gyy.json'
content_hash: 'sha256:67fb35f027d25ae9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# init(subsystem:category:)

<sub>Initializer</sub>

Creates a log using the specified subsystem and category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(subsystem: String, category: String)
```

## Parameters

- `subsystem` — An identifier string, in reverse DNS notation, that represents the app subsystem that’s logging information, such as `com.your_company.your_subsystem_name`. The logging system uses this information to categorize and filter related log messages, and to group related logging settings.

- `category` — A category within the specified subsystem. The system uses this value to categorize and filter related log messages, and to group related logging settings within the subsystem. A category’s logging settings override those of the containing subsystem.

## Return Value

A custom log object that you can pass to other logging functions to perform logging and to determine whether a specific level of logging is in an enabled state.

## See Also

### Creating a Log

- [init(subsystem:category:)](<init(subsystem_category_)-72ghw.md>) — Creates a log using the specified subsystem and system-defined category.
- [Category](category.md) — System-defined categories that identify well-known parts of your app.
