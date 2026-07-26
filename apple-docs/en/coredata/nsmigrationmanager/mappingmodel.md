---
title: mappingModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/mappingmodel
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/mappingmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/mappingmodel.json'
content_hash: 'sha256:51f5e7afcd2e09d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# mappingModel

<sub>Instance Property</sub>

The mapping model for the migration manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mappingModel: NSMappingModel { get }
```

## See Also

### Related Documentation

- [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>) — Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model. _(deprecated)_

### Getting the Manager’s Configuration

- [destinationContext](destinationcontext.md) — The managed object context the migration manager uses for writing the destination persistent store.
- [destinationModel](destinationmodel.md) — The destination model for the migration manager.
- [sourceContext](sourcecontext.md) — The managed object context the migration manager uses for reading the source persistent store.
- [sourceModel](sourcemodel.md) — The source model for the migration manager.
- [- destinationEntityForEntityMapping:](<destinationentity(for_).md>) — Returns the entity description for the destination entity of a given entity mapping.
- [- sourceEntityForEntityMapping:](<sourceentity(for_).md>) — Returns the entity description for the source entity of a given entity mapping.
