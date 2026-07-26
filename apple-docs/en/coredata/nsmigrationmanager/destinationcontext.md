---
title: destinationContext
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/destinationcontext
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/destinationcontext.json'
content_hash: 'sha256:8392769a26419da1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# destinationContext

<sub>Instance Property</sub>

The managed object context the migration manager uses for writing the destination persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var destinationContext: NSManagedObjectContext { get }
```

## Discussion

This context is created on demand as part of the initialization of the Core Data stacks used for migration.

## See Also

### Getting the Manager’s Configuration

- [destinationModel](destinationmodel.md) — The destination model for the migration manager.
- [mappingModel](mappingmodel.md) — The mapping model for the migration manager.
- [sourceContext](sourcecontext.md) — The managed object context the migration manager uses for reading the source persistent store.
- [sourceModel](sourcemodel.md) — The source model for the migration manager.
- [- destinationEntityForEntityMapping:](<destinationentity(for_).md>) — Returns the entity description for the destination entity of a given entity mapping.
- [- sourceEntityForEntityMapping:](<sourceentity(for_).md>) — Returns the entity description for the source entity of a given entity mapping.
