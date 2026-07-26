---
title: managedObjectModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/managedobjectmodel
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/managedobjectmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/managedobjectmodel.json'
content_hash: 'sha256:768a8b77eec9bc18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# managedObjectModel

<sub>Instance Property</sub>

The container’s managed object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var managedObjectModel: NSManagedObjectModel { get }
```

## Discussion

This property contains a reference to the [NSManagedObjectModel](../nsmanagedobjectmodel.md) object associated with this persistent container.

## See Also

### Getting the Container’s Configuration

- [name](name.md) — The container’s name.
- [persistentStoreCoordinator](persistentstorecoordinator.md) — The container’s persistent store coordinator.
