---
title: 'addPersistentStore(type:configuration:at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(type:configuration:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(type:configuration:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/addpersistentstore%28type%3Aconfiguration%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:bcbca779543c0167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# addPersistentStore(type:configuration:at:options:)

<sub>Instance Method</sub>

Adds a specific type of persistent store at the provided location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String? = nil, at storeURL: URL, options: [AnyHashable : Any]? = nil) throws -> NSPersistentStore
```

## Parameters

- `type` — The store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `configuration` — The name of the configuration to use. You must define this configuration in the coordinator’s managed object model.

- `storeURL` — The store’s location.

- `options` — A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Adding or removing a store

- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- addPersistentStoreWithDescription:completionHandler:](<addpersistentstore(with_completionhandler_).md>) — Adds a persistent store using the provided description.
- [- removePersistentStore:error:](<remove(__).md>) — Removes the specified persistent store from the coordinator.
