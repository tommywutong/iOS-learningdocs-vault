---
title: shouldMigrateStoreAutomatically
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/shouldmigratestoreautomatically
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/shouldmigratestoreautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/shouldmigratestoreautomatically.json'
content_hash: 'sha256:2bdb2137d72a7b81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# shouldMigrateStoreAutomatically

<sub>Instance Property</sub>

A flag indicating whether the associated persistent store should be migrated automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldMigrateStoreAutomatically: Bool { get set }
```

## Discussion

If this is set to [false](../../swift/false.md) and the store is out of sync, attempting to load the store produces an error. If this is set to [true](../../swift/true.md) and the store is out of sync, attempting to load the store causes Core Data to attempt a migration. This flag is set to [true](../../swift/true.md) by default.

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [configuration](configuration.md) — The name of the configuration used by this store.
- [timeout](timeout.md) — The connection timeout for the associated store.
- [type](type.md) — The type of store this description represents.
- [readOnly](isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldAddStoreAsynchronously](shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldInferMappingModelAutomatically](shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
