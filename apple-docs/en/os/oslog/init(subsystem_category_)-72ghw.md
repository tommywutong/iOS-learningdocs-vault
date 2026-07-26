---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslog/init(subsystem:category:)-72ghw'
source_url: 'https://developer.apple.com/documentation/os/oslog/init(subsystem:category:)-72ghw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/init%28subsystem%3Acategory%3A%29-72ghw.json'
content_hash: 'sha256:cde7a60cab768fbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# init(subsystem:category:)

<sub>Initializer</sub>

Creates a log using the specified subsystem and system-defined category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(subsystem: String, category: OSLog.Category)
```

## Parameters

- `subsystem` — An identifier string, in reverse DNS notation, that represents the subsystem that’s performing logging, such as `com.your_company.your_subsystem_name`. The logging system uses this information to categorize and filter related log messages.

- `category` — A system-defined category within the specified subsystem. The system uses this value to categorize and filter related log messages. A category’s logging settings override those of the containing subsystem.

## Return Value

A custom log object that you can pass to other logging functions to perform logging and to determine whether a specific level of logging is in an enabled state.

## See Also

### Creating a Log

- [init(subsystem:category:)](<init(subsystem_category_)-17gyy.md>) — Creates a log using the specified subsystem and category.
- [Category](category.md) — System-defined categories that identify well-known parts of your app.
