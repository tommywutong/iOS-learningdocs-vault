---
title: persistentStoreCoordinator
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/persistentstorecoordinator
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentstorecoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/persistentstorecoordinator.json'
content_hash: 'sha256:80debb2082e10560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# persistentStoreCoordinator

<sub>Instance Property</sub>

The container’s persistent store coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistentStoreCoordinator: NSPersistentStoreCoordinator { get }
```

## Discussion

When the persistent container is initialized, it creates a persistent store coordinator as part of that initialization. That persistent store coordinator is referenced in this property.

## See Also

### Getting the Container’s Configuration

- [managedObjectModel](managedobjectmodel.md) — The container’s managed object model.
- [name](name.md) — The container’s name.
