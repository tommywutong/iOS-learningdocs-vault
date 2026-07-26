---
title: 'destroyPersistentStore(at:type:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:type:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:type:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore%28at%3Atype%3Aoptions%3A%29.json'
content_hash: 'sha256:ded6bedbadc0cee8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# destroyPersistentStore(at:type:options:)

<sub>Instance Method</sub>

Deletes a specific type of persistent store at the provided location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func destroyPersistentStore(at url: URL, type storeType: NSPersistentStore.StoreType, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `url` — The store’s location.

- `storeType` — The store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `options` — A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Modifying a store

- [migratePersistentStore(_:to:options:type:)](<migratepersistentstore(__to_options_type_).md>) — Changes the location and, if necessary, the store type of the specified persistent store.
- [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) — Replaces one persistent store with another.
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
