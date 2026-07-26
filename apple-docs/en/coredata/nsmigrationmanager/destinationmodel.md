---
title: destinationModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/destinationmodel
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/destinationmodel.json'
content_hash: 'sha256:14d8102daad7081d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# destinationModel

<sub>Instance Property</sub>

The destination model for the migration manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var destinationModel: NSManagedObjectModel { get }
```

## See Also

### Related Documentation

- [- initWithSourceModel:destinationModel:](<init(sourcemodel_destinationmodel_).md>) — Initializes a migration manager instance with given source and destination models.

### Getting the Manager’s Configuration

- [destinationContext](destinationcontext.md) — The managed object context the migration manager uses for writing the destination persistent store.
- [mappingModel](mappingmodel.md) — The mapping model for the migration manager.
- [sourceContext](sourcecontext.md) — The managed object context the migration manager uses for reading the source persistent store.
- [sourceModel](sourcemodel.md) — The source model for the migration manager.
- [- destinationEntityForEntityMapping:](<destinationentity(for_).md>) — Returns the entity description for the destination entity of a given entity mapping.
- [- sourceEntityForEntityMapping:](<sourceentity(for_).md>) — Returns the entity description for the source entity of a given entity mapping.
