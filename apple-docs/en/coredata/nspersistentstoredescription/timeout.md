---
title: timeout
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/timeout
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/timeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/timeout.json'
content_hash: 'sha256:7f4ecebb78a9b9bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# timeout

<sub>Instance Property</sub>

The connection timeout for the associated store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeout: TimeInterval { get set }
```

## Discussion

This is a convenience method for setting the [NSPersistentStoreTimeoutOption](../nspersistentstoretimeoutoption.md) on the associated store.

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [configuration](configuration.md) — The name of the configuration used by this store.
- [type](type.md) — The type of store this description represents.
- [readOnly](isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldAddStoreAsynchronously](shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldInferMappingModelAutomatically](shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
