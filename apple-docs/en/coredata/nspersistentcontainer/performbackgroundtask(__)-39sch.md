---
title: 'performBackgroundTask(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/performbackgroundtask(_:)-39sch'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/performbackgroundtask(_:)-39sch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/performbackgroundtask%28_%3A%29-39sch.json'
content_hash: 'sha256:0ddbec5b62868171'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# performBackgroundTask(_:)

<sub>Instance Method</sub>

Executes a closure on a private queue using an ephemeral managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performBackgroundTask(_ block: @escaping @Sendable (NSManagedObjectContext) -> Void)
```

## Parameters

- `block` — A closure that is executed by the persistent container against a newly created private context. The private context is passed into the block as part of the execution of the block.

## Discussion

Each time this method is invoked, the persistent container creates a new [NSManagedObjectContext](../nsmanagedobjectcontext.md) with the [concurrencyType](../nsmanagedobjectcontext/concurrencytype-swift.property.md) set to [NSPrivateQueueConcurrencyType](../nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md). The persistent container then executes the passed in block against that newly created context on the context’s private queue.

## See Also

### Performing Background Tasks

- [performBackgroundTask(_:)](<performbackgroundtask(__)-25nok.md>)
