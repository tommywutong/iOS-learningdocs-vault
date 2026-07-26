---
title: 'addPersistentStore(with:completionHandler:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(with:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/addpersistentstore(with:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/addpersistentstore%28with%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3627f40999cff0ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# addPersistentStore(with:completionHandler:)

<sub>Instance Method</sub>

Adds a persistent store using the provided description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addPersistentStore(with storeDescription: NSPersistentStoreDescription, completionHandler block: @escaping (NSPersistentStoreDescription, (any Error)?) -> Void)
```

## Parameters

- `storeDescription` — A description object used to create and load a persistent store.

- `block` — The completion handler block that’s invoked after the store is added.

## See Also

### Adding or removing a store

- [addPersistentStore(type:configuration:at:options:)](<addpersistentstore(type_configuration_at_options_).md>) — Adds a specific type of persistent store at the provided location.
- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- removePersistentStore:error:](<remove(__).md>) — Removes the specified persistent store from the coordinator.
