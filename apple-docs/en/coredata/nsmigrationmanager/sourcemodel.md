---
title: sourceModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/sourcemodel
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/sourcemodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/sourcemodel.json'
content_hash: 'sha256:bbdba9f78d1e8d93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# sourceModel

<sub>Instance Property</sub>

The source model for the migration manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceModel: NSManagedObjectModel { get }
```

## See Also

### Related Documentation

- [- initWithSourceModel:destinationModel:](<init(sourcemodel_destinationmodel_).md>) — Initializes a migration manager instance with given source and destination models.

### Getting the Manager’s Configuration

- [destinationContext](destinationcontext.md) — The managed object context the migration manager uses for writing the destination persistent store.
- [destinationModel](destinationmodel.md) — The destination model for the migration manager.
- [mappingModel](mappingmodel.md) — The mapping model for the migration manager.
- [sourceContext](sourcecontext.md) — The managed object context the migration manager uses for reading the source persistent store.
- [- destinationEntityForEntityMapping:](<destinationentity(for_).md>) — Returns the entity description for the destination entity of a given entity mapping.
- [- sourceEntityForEntityMapping:](<sourceentity(for_).md>) — Returns the entity description for the source entity of a given entity mapping.
