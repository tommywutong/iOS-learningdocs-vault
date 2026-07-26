---
title: 'destroyPersistentStore(at:ofType:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore%28at%3Aoftype%3Aoptions%3A%29.json'
content_hash: 'sha256:9be85bec2b809fdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# destroyPersistentStore(at:ofType:options:)

<sub>Instance Method</sub>

Deletes a specific type of persistent store at the provided location.

> [!warning] Deprecated
> Use [destroyPersistentStore(at:type:options:)](<destroypersistentstore(at_type_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func destroyPersistentStore(at url: URL, ofType storeType: String, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `url` — The store’s location.

- `storeType` — The store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `options` — A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Modifying a store

- [destroyPersistentStore(at:type:options:)](<destroypersistentstore(at_type_options_).md>) — Deletes a specific type of persistent store at the provided location.
- [migratePersistentStore(_:to:options:type:)](<migratepersistentstore(__to_options_type_).md>) — Changes the location and, if necessary, the store type of the specified persistent store.
- [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) — Replaces one persistent store with another.
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
