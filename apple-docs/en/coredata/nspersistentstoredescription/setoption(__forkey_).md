---
title: 'setOption(_:forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstoredescription/setoption(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/setoption(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/setoption%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:3459765742d199a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# setOption(_:forKey:)

<sub>Instance Method</sub>

Sets an option on the store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setOption(_ option: NSObject?, forKey key: String)
```

## Parameters

- `option` — The value to be set for an option on the store.

- `key` — The key of the value to be set for an option on the store.

## Discussion

If a value was previously set for the given option, that value is replaced with the given value. Note that the keys are case-sensitive. For a list of the available options, see [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md).

## See Also

### Configuring a Persistent Store Description

- [URL](url.md) — The URL that the store will use for its location.
- [configuration](configuration.md) — The name of the configuration used by this store.
- [timeout](timeout.md) — The connection timeout for the associated store.
- [type](type.md) — The type of store this description represents.
- [readOnly](isreadonly.md) — A flag that indicates whether this store will be read-only.
- [shouldAddStoreAsynchronously](shouldaddstoreasynchronously.md) — A flag that determines whether the store is added asynchronously.
- [shouldInferMappingModelAutomatically](shouldinfermappingmodelautomatically.md) — A flag indicating whether a mapping model should be created automatically.
- [shouldMigrateStoreAutomatically](shouldmigratestoreautomatically.md) — A flag indicating whether the associated persistent store should be migrated automatically.
- [- setValue:forPragmaNamed:](<setvalue(__forpragmanamed_).md>) — Allows you to set pragmas for the SQLite store.
