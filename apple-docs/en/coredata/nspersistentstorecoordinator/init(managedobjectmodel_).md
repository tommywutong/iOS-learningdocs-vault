---
title: 'init(managedObjectModel:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/init(managedobjectmodel:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/init(managedobjectmodel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/init%28managedobjectmodel%3A%29.json'
content_hash: 'sha256:614fad832a020cb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# init(managedObjectModel:)

<sub>Initializer</sub>

Creates a persistent store coordinator with the specified managed object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(managedObjectModel model: NSManagedObjectModel)
```

## Parameters

- `model` — A managed object model.

## Return Value

The receiver, initialized with `model`.

## See Also

### Creating a persistent store coordinator

- [Store options](../store-options.md) — The options keys that configure the behavior and characteristics of a persistent store.
- [Migration options](../migration-options.md) — The options keys that configure the migration behavior of a persistent store.
- [Store versions](../store-versions.md) — The metadata keys you use when comparing store versions.
