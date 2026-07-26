---
title: 'migratePersistentStore(_:to:options:withType:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore%28_%3Ato%3Aoptions%3Awithtype%3A%29.json'
content_hash: 'sha256:0f4399a2065bfc54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# migratePersistentStore(_:to:options:withType:)

<sub>Instance Method</sub>

Changes the location and, if necessary, the store type of the specified persistent store.

> [!warning] Deprecated
> Use [migratePersistentStore(_:to:options:type:)](<migratepersistentstore(__to_options_type_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func migratePersistentStore(_ store: NSPersistentStore, to URL: URL, options: [AnyHashable : Any]? = nil, withType storeType: String) throws -> NSPersistentStore
```

## Parameters

- `store` — A persistent store.

- `URL` — An URL object that specifies the location for the new store.

- `options` — A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see [Store options](../store-options.md).

- `storeType` — A string constant (such as `NSSQLiteStoreType`) that specifies the type of the new store—see [Persistent Store Types](../persistent-store-types.md).

## Return Value

If the migration is successful, the new store, otherwise `nil`.

## Discussion

This method is typically used for “Save As” operations. Performance may vary depending on the type of old and new store. For more details of the action of this method, see Persistent Store Features in [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075).

> [!important] Important
> After invocation of this method, the specified store is removed from the coordinator thus `store` is no longer a useful reference.

## See Also

### Related Documentation

- [- removePersistentStore:error:](<remove(__).md>) — Removes the specified persistent store from the coordinator.
- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_

### Modifying a store

- [destroyPersistentStore(at:type:options:)](<destroypersistentstore(at_type_options_).md>) — Deletes a specific type of persistent store at the provided location.
- [migratePersistentStore(_:to:options:type:)](<migratepersistentstore(__to_options_type_).md>) — Changes the location and, if necessary, the store type of the specified persistent store.
- [replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_type_).md>) — Replaces one persistent store with another.
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
