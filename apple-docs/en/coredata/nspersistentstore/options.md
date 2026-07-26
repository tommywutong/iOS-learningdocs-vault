---
title: options
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/options
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/options.json'
content_hash: 'sha256:bce141abdf19677e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# options

<sub>Instance Property</sub>

The options that Core Data uses to create the store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [AnyHashable : Any]? { get }
```

## Discussion

See [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) for a list of key names for options in this dictionary.

## See Also

### Getting Store Configuration

- [configurationName](configurationname.md) — The name of the managed object model configuration that creates the persistent store.
- [persistentStoreCoordinator](persistentstorecoordinator.md) — The persistent store coordinator that loads the persistent store.
- [type](type.md) — The type string of the persistent store.
- [StoreType](storetype.md) — The types of persistent stores that Core Data supports.
- [Persistent Store Types](../persistent-store-types.md) — Persist data through the available store types.
