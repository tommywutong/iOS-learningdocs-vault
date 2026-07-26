---
title: name
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/name
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/name.json'
content_hash: 'sha256:25e63aefe932b9cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# name

<sub>Instance Property</sub>

The container’s name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String { get }
```

## Discussion

This property is passed in as part of the initialization of the persistent container. This name is used to locate the [NSManagedObjectModel](../nsmanagedobjectmodel.md) (if the [NSManagedObjectModel](../nsmanagedobjectmodel.md) object is not passed in as part of the initialization) and is used to name the persistent store.

## See Also

### Getting the Container’s Configuration

- [managedObjectModel](managedobjectmodel.md) — The container’s managed object model.
- [persistentStoreCoordinator](persistentstorecoordinator.md) — The container’s persistent store coordinator.
