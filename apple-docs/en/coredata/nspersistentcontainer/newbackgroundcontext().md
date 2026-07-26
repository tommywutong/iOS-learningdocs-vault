---
title: newBackgroundContext()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/newbackgroundcontext()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/newbackgroundcontext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/newbackgroundcontext%28%29.json'
content_hash: 'sha256:e03b83d6b3df6cab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# newBackgroundContext()

<sub>Instance Method</sub>

Returns a new managed object context that executes on a private queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func newBackgroundContext() -> NSManagedObjectContext
```

## Return Value

A newly created private managed object context.

## Discussion

Invoking this method causes the persistent container to create and return a new [NSManagedObjectContext](../nsmanagedobjectcontext.md) with the [concurrencyType](../nsmanagedobjectcontext/concurrencytype-swift.property.md) set to [NSPrivateQueueConcurrencyType](../nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md). This new context will be associated with the [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) directly and is set to consume [NSManagedObjectContextDidSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) broadcasts automatically.

## See Also

### Acquiring Contexts

- [viewContext](viewcontext.md) — The main queue’s managed object context.
