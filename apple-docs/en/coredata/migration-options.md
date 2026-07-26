---
title: Migration options
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/migration-options
source_url: 'https://developer.apple.com/documentation/coredata/migration-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/migration-options.json'
content_hash: 'sha256:09116cf9ea96cea7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Core Data stack](core-data-stack.md) · [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)

# Migration options

<sub>API Collection</sub>

The options keys that configure the migration behavior of a persistent store.

## Topics

### Constants

- [NSIgnorePersistentStoreVersioningOption](nsignorepersistentstoreversioningoption.md) — Key to ignore the built-in versioning provided by Core Data.
- [NSMigratePersistentStoresAutomaticallyOption](nsmigratepersistentstoresautomaticallyoption.md) — Key to automatically attempt to migrate versioned stores.
- [NSInferMappingModelAutomaticallyOption](nsinfermappingmodelautomaticallyoption.md) — Key to attempt to create the mapping model automatically.

## See Also

### Creating a persistent store coordinator

- [- initWithManagedObjectModel:](<nspersistentstorecoordinator/init(managedobjectmodel_).md>) — Creates a persistent store coordinator with the specified managed object model.
- [Store options](store-options.md) — The options keys that configure the behavior and characteristics of a persistent store.
- [Store versions](store-versions.md) — The metadata keys you use when comparing store versions.
