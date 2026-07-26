---
title: 'replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:ofType:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore%28at%3Adestinationoptions%3Awithpersistentstorefrom%3Asourceoptions%3Aoftype%3A%29.json'
content_hash: 'sha256:0039e32db21bf428'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:ofType:)

<sub>Instance Method</sub>

Replaces one persistent store with another.

> [!warning] Deprecated
> Use [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacePersistentStore(at destinationURL: URL, destinationOptions: [AnyHashable : Any]? = nil, withPersistentStoreFrom sourceURL: URL, sourceOptions: [AnyHashable : Any]? = nil, ofType storeType: String) throws
```

## Parameters

- `destinationURL` — The location of the store to replace.

- `destinationOptions` — A dictionary containing key-value pairs that specify the behavior and characteristics of the store to replace. For more information, see [Store options](../store-options.md).

- `sourceURL` — The location of the store to use as the replacement.

- `sourceOptions` — A dictionary containing key-value pairs that specify the behavior and characteristics of the replacement store. For more information, see [Store options](../store-options.md).

- `storeType` — The store type of the replacement store. For possible values, see [StoreType](../nspersistentstore/storetype.md).

## See Also

### Modifying a store

- [destroyPersistentStore(at:type:options:)](<destroypersistentstore(at_type_options_).md>) — Deletes a specific type of persistent store at the provided location.
- [migratePersistentStore(_:to:options:type:)](<migratepersistentstore(__to_options_type_).md>) — Changes the location and, if necessary, the store type of the specified persistent store.
- [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) — Replaces one persistent store with another.
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
