---
title: NSManagedObjectContext.ConcurrencyType
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.struct.json'
content_hash: 'sha256:366f1388e6e02652'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.ConcurrencyType

<sub>Structure</sub>

The concurrency types to use with a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ConcurrencyType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md)

## Topics

### Concurrency Types

- [mainQueue](concurrencytype-swift.struct/mainqueue.md) — A concurrency type where the context performs its tasks on the main queue.
- [privateQueue](concurrencytype-swift.struct/privatequeue.md) — A concurrency type where the context performs its tasks on a private queue.

## See Also

### Creating a context

- [init(_:)](<init(__).md>) — Creates a context that uses the specified concurrency type.
- [- initWithConcurrencyType:](<init(concurrencytype_).md>) — Creates a context that uses the specified concurrency type. _(deprecated)_
- [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md) — The concurrency types you can use with a managed object context.
