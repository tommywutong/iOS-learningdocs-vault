---
title: privateQueue
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct/privatequeue
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct/privatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct/privatequeue.json'
content_hash: 'sha256:3465a2877a0f3101'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSManagedObjectContext](../../nsmanagedobjectcontext.md) · [ConcurrencyType](../concurrencytype-swift.struct.md)

# privateQueue

<sub>Type Property</sub>

A concurrency type where the context performs its tasks on a private queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let privateQueue: NSManagedObjectContext.ConcurrencyType
```

## See Also

### Concurrency Types

- [mainQueue](mainqueue.md) — A concurrency type where the context performs its tasks on the main queue.
