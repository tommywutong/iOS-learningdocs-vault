---
title: 'migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nsmigrationmanager/migratestore(from:sourcetype:options:with:todestinationurl:destinationtype:destinationoptions:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/migratestore(from:sourcetype:options:with:todestinationurl:destinationtype:destinationoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/migratestore%28from%3Asourcetype%3Aoptions%3Awith%3Atodestinationurl%3Adestinationtype%3Adestinationoptions%3A%29.json'
content_hash: 'sha256:79f9f3ef234a02ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)

<sub>Instance Method</sub>

Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model.

> [!warning] Deprecated
> Use [migrateStore(from:type:options:mapping:to:type:options:)](<migratestore(from_type_options_mapping_to_type_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func migrateStore(from sourceURL: URL, sourceType sStoreType: String, options sOptions: [AnyHashable : Any]? = nil, with mappings: NSMappingModel?, toDestinationURL dURL: URL, destinationType dStoreType: String, destinationOptions dOptions: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `sourceURL` — The location of an existing persistent store. A store must exist at this URL.

- `sStoreType` — The type of store at `sourceURL` (see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) for possible values).

- `sOptions` — A dictionary of options for the source (see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) for possible values).

- `mappings` — The mapping model to use to effect the migration.

- `dURL` — The location of the destination store.

- `dStoreType` — The type of store at `dURL` (see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) for possible values).

- `dOptions` — A dictionary of options for the destination (see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) for possible values).

## Discussion

This method performs compatibility checks on the source and destination models and the mapping model.

### Special Considerations

If a store does not exist at the destination URL (`dURL`), one is created; otherwise, the migration appends to the existing store.

## See Also

### Related Documentation

- [- cancelMigrationWithError:](<cancelmigrationwitherror(__).md>) — Cancels the migration with a given error.

### Performing a Migration

- [migrateStore(from:type:options:mapping:to:type:options:)](<migratestore(from_type_options_mapping_to_type_options_).md>) — Migrates the source store to the destination using the specified mapping model.
