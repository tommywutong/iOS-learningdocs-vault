---
title: 'migrateStore(from:type:options:mapping:to:type:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/migratestore(from:type:options:mapping:to:type:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/migratestore(from:type:options:mapping:to:type:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/migratestore%28from%3Atype%3Aoptions%3Amapping%3Ato%3Atype%3Aoptions%3A%29.json'
content_hash: 'sha256:c8a36ed9d914462f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# migrateStore(from:type:options:mapping:to:type:options:)

<sub>Instance Method</sub>

Migrates the source store to the destination using the specified mapping model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func migrateStore(from sourceURL: URL, type sourceType: NSPersistentStore.StoreType, options sourceOptions: [AnyHashable : Any]? = nil, mapping: NSMappingModel, to destinationURL: URL, type destinationType: NSPersistentStore.StoreType, options destinationOptions: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `sourceURL` — The location of the store to migrate.

- `sourceType` — The persistent store type of the store you’re migrating from. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `sourceOptions` — A dictionary of options to apply to the source store. For possible values, see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md).

- `mapping` — The mapping model that converts the entities in the source store to those in the destination store.

- `destinationURL` — The location of the destination store.

- `destinationType` — The persistent store type of the store you’re migrating to. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `destinationOptions` — A dictionary of options to apply to the destination store. For possible values, see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md).

## Discussion

A store must exist at `sourceURL`; otherwise, the migration fails. Before the migration occurs, the method ensures compatibility between the source model, the destination model, and the mapping model. If a store doesn’t exist at `destinationURL`, Core Data creates one as part of the migration; otherwise, the migration updates the existing store.

## See Also

### Performing a Migration

- [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>) — Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model. _(deprecated)_
