---
title: OSLog.Category
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog/category
source_url: 'https://developer.apple.com/documentation/os/oslog/category'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/category.json'
content_hash: 'sha256:02c961390bc06b3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# OSLog.Category

<sub>Structure</sub>

System-defined categories that identify well-known parts of your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Category
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Logging Signposts

- [pointsOfInterest](category/pointsofinterest.md) — The category you use to log signposts.
- [dynamicStackTracing](category/dynamicstacktracing.md) — The category for dynamic stack tracing.
- [dynamicTracing](category/dynamictracing.md) — The category for dynamic tracing.

### Inspecting Log Categories

- [rawValue](category/rawvalue.md) — A string that uniquely identifies a logging category.

## See Also

### Creating a Log

- [init(subsystem:category:)](<init(subsystem_category_)-17gyy.md>) — Creates a log using the specified subsystem and category.
- [init(subsystem:category:)](<init(subsystem_category_)-72ghw.md>) — Creates a log using the specified subsystem and system-defined category.
