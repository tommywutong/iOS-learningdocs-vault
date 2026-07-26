---
title: willMigrateHandler
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+, Swift 5.8+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscustommigrationstage/willmigratehandler-5wead
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/willmigratehandler-5wead'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/willmigratehandler-5wead.json'
content_hash: 'sha256:5a0f64610bd625ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# willMigrateHandler

<sub>Instance Property</sub>

The handler to execute before the stage runs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var willMigrateHandler: ((NSStagedMigrationManager, NSCustomMigrationStage) throws -> Void)? { get set }
```

## Discussion

Use this handler to prepare the persistent store’s data for the pending migration. Access the store using the [container](../nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

### Assigning event handlers

- [didMigrateHandler](didmigratehandler-2zbss.md) — The handler to execute after the stage runs.
