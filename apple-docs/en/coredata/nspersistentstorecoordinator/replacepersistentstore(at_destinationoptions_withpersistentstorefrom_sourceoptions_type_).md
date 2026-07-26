---
title: 'replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore%28at%3Adestinationoptions%3Awithpersistentstorefrom%3Asourceoptions%3Atype%3A%29.json'
content_hash: 'sha256:238eed7816aa7a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)

<sub>Instance Method</sub>

Replaces one persistent store with another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacePersistentStore(at destinationURL: URL, destinationOptions: [AnyHashable : Any]? = nil, withPersistentStoreFrom sourceURL: URL, sourceOptions: [AnyHashable : Any]? = nil, type sourceType: NSPersistentStore.StoreType) throws
```

## Parameters

- `destinationURL` — The location of the store to replace.

- `destinationOptions` — A dictionary containing key-value pairs that specify the behavior and characteristics of the store to replace. For more information, see [Store options](../store-options.md).

- `sourceURL` — The location of the store to use as the replacement.

- `sourceOptions` — A dictionary containing key-value pairs that specify the behavior and characteristics of the replacement store. For more information, see [Store options](../store-options.md).

- `sourceType` — The store type of the replacement store. For possible values, see [StoreType](../nspersistentstore/storetype.md).

## See Also

### Modifying a store

- [destroyPersistentStore(at:type:options:)](<destroypersistentstore(at_type_options_).md>) — Deletes a specific type of persistent store at the provided location.
- [migratePersistentStore(_:to:options:type:)](<migratepersistentstore(__to_options_type_).md>) — Changes the location and, if necessary, the store type of the specified persistent store.
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
