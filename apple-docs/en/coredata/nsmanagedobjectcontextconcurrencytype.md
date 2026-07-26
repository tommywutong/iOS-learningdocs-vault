---
title: NSManagedObjectContextConcurrencyType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextconcurrencytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextconcurrencytype.json'
content_hash: 'sha256:d64e9714d5f7cb42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectContextConcurrencyType

<sub>Enumeration</sub>

The concurrency types you can use with a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSManagedObjectContextConcurrencyType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Concurrency Types

- [NSPrivateQueueConcurrencyType](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md) — Specifies that the context will be associated with a private dispatch queue.
- [NSMainQueueConcurrencyType](nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.md) — Specifies that the context will be associated with the main queue.
- [NSConfinementConcurrencyType](nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype.md) — Specifies that the context will use the thread confinement pattern. _(deprecated)_

### Initializers

- [init(rawValue:)](<nsmanagedobjectcontextconcurrencytype/init(rawvalue_).md>)

## See Also

### Creating a context

- [init(_:)](<nsmanagedobjectcontext/init(__).md>) — Creates a context that uses the specified concurrency type.
- [ConcurrencyType](nsmanagedobjectcontext/concurrencytype-swift.struct.md) — The concurrency types to use with a managed object context.
- [- initWithConcurrencyType:](<nsmanagedobjectcontext/init(concurrencytype_).md>) — Creates a context that uses the specified concurrency type. _(deprecated)_
