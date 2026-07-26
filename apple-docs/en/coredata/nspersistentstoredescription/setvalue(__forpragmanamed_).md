---
title: 'setValue(_:forPragmaNamed:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstoredescription/setvalue(_:forpragmanamed:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/setvalue(_:forpragmanamed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/setvalue%28_%3Aforpragmanamed%3A%29.json'
content_hash: 'sha256:584e6fe26c52247c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# setValue(_:forPragmaNamed:)

<sub>Instance Method</sub>

Allows you to set pragmas for the SQLite store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: NSObject?, forPragmaNamed name: String)
```

## Parameters

- `value` — The value of the pragma to be set.

- `name` — The name of the pragma to be set.

## Discussion

Pragma options are for SQLite stores only. All pragma values must be specified as [NSString](../../foundation/nsstring.md)objects. The `fullfsync` and `synchronous` pragmas control the tradeoff between write performance (write to disk speed and cache utilization) and durability (data loss/corruption sensitivity to power interruption). For more information on pragma settings, see [http://sqlite.org/pragma.html](http://sqlite.org/pragma.html).

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
- [- setOption:forKey:](<setoption(__forkey_).md>) — Sets an option on the store.
