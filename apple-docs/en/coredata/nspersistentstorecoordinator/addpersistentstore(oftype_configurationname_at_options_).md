---
title: 'addPersistentStore(ofType:configurationName:at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/addpersistentstore%28oftype%3Aconfigurationname%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:9e4585245bac0150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# addPersistentStore(ofType:configurationName:at:options:)

<sub>Instance Method</sub>

Adds a specific type of persistent store at the provided location.

> [!warning] Deprecated
> Use [addPersistentStore(type:configuration:at:options:)](<addpersistentstore(type_configuration_at_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addPersistentStore(ofType storeType: String, configurationName configuration: String?, at storeURL: URL?, options: [AnyHashable : Any]? = nil) throws -> NSPersistentStore
```

## Parameters

- `storeType` — A string constant (such as `NSSQLiteStoreType`) that specifies the store type—see [Persistent Store Types](../persistent-store-types.md) for possible values.

- `configuration` — The name of a configuration in the receiver’s managed object model that will be used by the new store. The configuration can be `nil`, in which case no other configurations are allowed.

- `storeURL` — The file location of the persistent store.

- `options` — A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see [Store options](../store-options.md) and [Migration options](../migration-options.md). This value may be `nil`.

## Return Value

The newly created store or, if an error occurs, `nil`.

## See Also

### Related Documentation

- [- removePersistentStore:error:](<remove(__).md>) — Removes the specified persistent store from the coordinator.
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:](<importstore(withidentifier_fromexternalrecordsdirectoryat_to_options_oftype_).md>) — Creates and populates a store with the external records found at a given URL. _(deprecated)_

### Adding or removing a store

- [addPersistentStore(type:configuration:at:options:)](<addpersistentstore(type_configuration_at_options_).md>) — Adds a specific type of persistent store at the provided location.
- [- addPersistentStoreWithDescription:completionHandler:](<addpersistentstore(with_completionhandler_).md>) — Adds a persistent store using the provided description.
- [- removePersistentStore:error:](<remove(__).md>) — Removes the specified persistent store from the coordinator.
