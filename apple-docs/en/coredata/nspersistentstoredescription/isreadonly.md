---
title: isReadOnly
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/isreadonly
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/isreadonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/isreadonly.json'
content_hash: 'sha256:a09c6a146b9a2021'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# isReadOnly

<sub>Instance Property</sub>

A flag that indicates whether this store will be read-only.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isReadOnly: Bool { get set }
```

## Discussion

This is a convenience method for setting the [NSReadOnlyPersistentStoreOption](../nsreadonlypersistentstoreoption.md) on the associated store.

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [configuration](configuration.md) — The name of the configuration used by this store.
- [timeout](timeout.md) — The connection timeout for the associated store.
- [type](type.md) — The type of store this description represents.
- [shouldAddStoreAsynchronously](shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldInferMappingModelAutomatically](shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
