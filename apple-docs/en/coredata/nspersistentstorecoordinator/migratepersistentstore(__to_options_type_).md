---
title: 'migratePersistentStore(_:to:options:type:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore%28_%3Ato%3Aoptions%3Atype%3A%29.json'
content_hash: 'sha256:4a91a60692c37837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# migratePersistentStore(_:to:options:type:)

<sub>Instance Method</sub>

Changes the location and, if necessary, the store type of the specified persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func migratePersistentStore(_ store: NSPersistentStore, to storeURL: URL, options: [AnyHashable : Any]? = nil, type storeType: NSPersistentStore.StoreType) throws -> NSPersistentStore
```

## Parameters

- `store` — The peristent store to migrate.

- `storeURL` — The location of the new persistent store.

- `options` — A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

- `storeType` — The new store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

## Discussion

Performance may vary depending on the store types of the old and new stores. Invoking this method removes the specified store from the coordinator.

## See Also

### Modifying a store

- [destroyPersistentStore(at:type:options:)](<destroypersistentstore(at_type_options_).md>) — Deletes a specific type of persistent store at the provided location.
- [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) — Replaces one persistent store with another.
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
