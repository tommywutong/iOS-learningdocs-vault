---
title: persistentStoreCoordinator
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/persistentstorecoordinator
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/persistentstorecoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/persistentstorecoordinator.json'
content_hash: 'sha256:88671468cf42041c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# persistentStoreCoordinator

<sub>Instance Property</sub>

The persistent store coordinator of the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get set }
```

## Return Value

The persistent store coordinator of the receiver.

## Discussion

The coordinator provides the managed object model and handles persistency. Note that multiple contexts can share a coordinator. May not be `nil`.

Setting [persistentStoreCoordinator](persistentstorecoordinator.md) to `nil` will raise an exception. If you want to “disconnect” a context from its persistent store coordinator, you should simply set all strong references to the context to `nil` and allow it to be deallocated normally.

For more details, see [Parent store](../nsmanagedobjectcontext.md#Parent-store).

## See Also

### Configuring a context

- [parentContext](parent.md) — The parent of the context.
- [name](name.md) — The developer-provided name of the context.
- [userInfo](userinfo.md) — The user information for the context.
