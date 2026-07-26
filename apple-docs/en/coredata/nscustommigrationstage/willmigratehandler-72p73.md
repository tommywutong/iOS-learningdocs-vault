---
title: willMigrateHandler
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscustommigrationstage/willmigratehandler-72p73
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/willmigratehandler-72p73'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/willmigratehandler-72p73.json'
content_hash: 'sha256:6dbf0409b2539a73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# willMigrateHandler

<sub>Instance Property</sub>

The handler to execute before the stage runs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (copy, nullable) _Bool (^)(NSStagedMigrationManager *, NSCustomMigrationStage *, NSError **) willMigrateHandler;
```

## Discussion

Use this handler to prepare the persistent store’s data for the pending migration. Access the store using the [container](../nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

### Assigning event handlers

- [didMigrateHandler](didmigratehandler-36uhx.md) — The handler to execute after the stage runs.
