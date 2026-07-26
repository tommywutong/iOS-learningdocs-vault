---
title: 'init(sourceModel:destinationModel:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/init(sourcemodel:destinationmodel:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/init(sourcemodel:destinationmodel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/init%28sourcemodel%3Adestinationmodel%3A%29.json'
content_hash: 'sha256:a4ae393cf55bc7aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# init(sourceModel:destinationModel:)

<sub>Initializer</sub>

Initializes a migration manager instance with given source and destination models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel)
```

## Parameters

- `sourceModel` — The source managed object model for the migration manager.

- `destinationModel` — The destination managed object model for the migration manager.

## Return Value

A migration manager instance initialized to migrate data in a store that uses `sourceModel` to a store that uses `destinationModel`.

## Discussion

You specify the mapping model in the migration method,  [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>).

### Special Considerations

This is the designated initializer for `NSMigrationManager`.

Although validation of the models is performed during [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>), as with `NSPersistentStoreCoordinator` once models are added to the migration manager they are immutable and cannot be altered.

## See Also

### Related Documentation

- [destinationModel](destinationmodel.md) — The destination model for the migration manager.
- [mappingModel](mappingmodel.md) — The mapping model for the migration manager.
- [sourceModel](sourcemodel.md) — The source model for the migration manager.
- [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>) — Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model. _(deprecated)_
- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
