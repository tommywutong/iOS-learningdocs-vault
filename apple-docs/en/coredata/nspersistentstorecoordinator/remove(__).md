---
title: 'remove(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/remove(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/remove%28_%3A%29.json'
content_hash: 'sha256:01331e801e5ba30c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# remove(_:)

<sub>Instance Method</sub>

Removes the specified persistent store from the coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ store: NSPersistentStore) throws
```

## Parameters

- `store` — A persistent store.

## See Also

### Related Documentation

- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_

### Adding or removing a store

- [addPersistentStore(type:configuration:at:options:)](<addpersistentstore(type_configuration_at_options_).md>) — Adds a specific type of persistent store at the provided location.
- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- addPersistentStoreWithDescription:completionHandler:](<addpersistentstore(with_completionhandler_).md>) — Adds a persistent store using the provided description.
