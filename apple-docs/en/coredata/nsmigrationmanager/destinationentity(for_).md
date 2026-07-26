---
title: 'destinationEntity(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/destinationentity(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationentity(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/destinationentity%28for%3A%29.json'
content_hash: 'sha256:47af3659c809b41e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# destinationEntity(for:)

<sub>Instance Method</sub>

Returns the entity description for the destination entity of a given entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func destinationEntity(for mEntity: NSEntityMapping) -> NSEntityDescription?
```

## Parameters

- `mEntity` — An entity mapping.

## Return Value

The entity description for the destination entity of `mEntity`.

## Discussion

Entity mappings do not store the actual description objects, but rather the name and version information of the entity.

## See Also

### Getting the Manager’s Configuration

- [destinationContext](destinationcontext.md) — The managed object context the migration manager uses for writing the destination persistent store.
- [destinationModel](destinationmodel.md) — The destination model for the migration manager.
- [mappingModel](mappingmodel.md) — The mapping model for the migration manager.
- [sourceContext](sourcecontext.md) — The managed object context the migration manager uses for reading the source persistent store.
- [sourceModel](sourcemodel.md) — The source model for the migration manager.
- [- sourceEntityForEntityMapping:](<sourceentity(for_).md>) — Returns the entity description for the source entity of a given entity mapping.
