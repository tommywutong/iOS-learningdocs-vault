---
title: shouldInferMappingModelAutomatically
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/shouldinfermappingmodelautomatically
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/shouldinfermappingmodelautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/shouldinfermappingmodelautomatically.json'
content_hash: 'sha256:ea9f30ef08c57d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# shouldInferMappingModelAutomatically

<sub>Instance Property</sub>

A flag indicating whether a mapping model should be created automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldInferMappingModelAutomatically: Bool { get set }
```

## Discussion

If this flag is set to [true](../../swift/true.md) and the value of the [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) is [true](../../swift/true.md), the coordinator attempts to infer a mapping model if none can be found. The default for this flag is [true](../../swift/true.md).

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [configuration](configuration.md) — The name of the configuration used by this store.
- [timeout](timeout.md) — The connection timeout for the associated store.
- [type](type.md) — The type of store this description represents.
- [readOnly](isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldAddStoreAsynchronously](shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
