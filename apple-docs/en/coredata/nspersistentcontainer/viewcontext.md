---
title: viewContext
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/viewcontext
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/viewcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/viewcontext.json'
content_hash: 'sha256:a4dde29dda2a3461'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# viewContext

<sub>Instance Property</sub>

The main queue’s managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var viewContext: NSManagedObjectContext { get }
```

## Discussion

This property contains a reference to the [NSManagedObjectContext](../nsmanagedobjectcontext.md) that is created and owned by the persistent container which is associated with the main queue of the application. This context is created automatically as part of the initialization of the persistent container.

This context is associated directly with the [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) and is non-generational by default.

## See Also

### Acquiring Contexts

- [- newBackgroundContext](<newbackgroundcontext().md>) — Returns a new managed object context that executes on a private queue.
