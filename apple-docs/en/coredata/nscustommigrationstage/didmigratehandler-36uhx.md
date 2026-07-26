---
title: didMigrateHandler
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscustommigrationstage/didmigratehandler-36uhx
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/didmigratehandler-36uhx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/didmigratehandler-36uhx.json'
content_hash: 'sha256:fe473ca5211281ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# didMigrateHandler

<sub>Instance Property</sub>

The handler to execute after the stage runs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (copy, nullable) _Bool (^)(NSStagedMigrationManager *, NSCustomMigrationStage *, NSError **) didMigrateHandler;
```

## Discussion

Use this handler to perform any cleanup tasks on the persistent store’s data after the migration has run. Access the store using the [container](../nsstagedmigrationmanager/container.md) property of the handler’s `migrationManager` parameter.

## See Also

### Assigning event handlers

- [willMigrateHandler](willmigratehandler-72p73.md) — The handler to execute before the stage runs.
