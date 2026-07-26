---
title: persistentStoreCoordinator
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/persistentstorecoordinator
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/persistentstorecoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/persistentstorecoordinator.json'
content_hash: 'sha256:891fbb711599c435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# persistentStoreCoordinator

<sub>Instance Property</sub>

The persistent store coordinator that loads the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get }
```

## See Also

### Getting Store Configuration

- [configurationName](configurationname.md) — The name of the managed object model configuration that creates the persistent store.
- [options](options.md) — The options that Core Data uses to create the store.
- [type](type.md) — The type string of the persistent store.
- [StoreType](storetype.md) — The types of persistent stores that Core Data supports.
- [Persistent Store Types](../persistent-store-types.md) — Persist data through the available store types.
