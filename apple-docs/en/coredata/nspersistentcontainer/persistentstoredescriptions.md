---
title: persistentStoreDescriptions
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/persistentstoredescriptions
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentstoredescriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/persistentstoredescriptions.json'
content_hash: 'sha256:5a746bb308f606b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# persistentStoreDescriptions

<sub>Instance Property</sub>

The descriptions of the container’s persistent stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistentStoreDescriptions: [NSPersistentStoreDescription] { get set }
```

## Discussion

If you want to override the type (or types) of persistent store(s) used by the persistent container, you can set this property with an array of [NSPersistentStoreDescription](../nspersistentstoredescription.md) objects.

If you will be configuring custom persistent store descriptions, you must set this property before calling [- loadPersistentStoresWithCompletionHandler:](<loadpersistentstores(completionhandler_).md>).

## See Also

### Managing Persistent Stores

- [- loadPersistentStoresWithCompletionHandler:](<loadpersistentstores(completionhandler_).md>) — Loads the persistent stores.
