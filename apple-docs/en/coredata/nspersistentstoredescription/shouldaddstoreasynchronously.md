---
title: shouldAddStoreAsynchronously
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/shouldaddstoreasynchronously
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/shouldaddstoreasynchronously'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/shouldaddstoreasynchronously.json'
content_hash: 'sha256:34bfa716ac6b8446'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# shouldAddStoreAsynchronously

<sub>Instance Property</sub>

A flag that determines whether the store is added asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldAddStoreAsynchronously: Bool { get set }
```

## Discussion

By default, the store is added to the [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) synchronously on the calling thread. If this flag is set to [true](../../swift/true.md), the store is added asynchronously on a background queue. The default for this flag is [false](../../swift/false.md).

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [configuration](configuration.md) — The name of the configuration used by this store.
- [timeout](timeout.md) — The connection timeout for the associated store.
- [type](type.md) — The type of store this description represents.
- [readOnly](isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldInferMappingModelAutomatically](shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
