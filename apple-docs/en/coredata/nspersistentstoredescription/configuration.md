---
title: configuration
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredescription/configuration
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/configuration.json'
content_hash: 'sha256:2e180d72558fc8b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# configuration

<sub>Instance Property</sub>

The name of the configuration used by this store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var configuration: String? { get set }
```

## Discussion

This displays the name of a configuration in the receiver’s managed object model that will be used by the new store. The configuration can be `nil`, in which case no other configurations are allowed.

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [timeout](timeout.md) — The connection timeout for the associated store.
- [type](type.md) — The type of store this description represents.
- [readOnly](isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldAddStoreAsynchronously](shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldInferMappingModelAutomatically](shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
