---
title: 'init(_:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/init(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/init%28_%3A%29.json'
content_hash: 'sha256:8c9a111b5dda6e32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# init(_:)

<sub>Initializer</sub>

Creates a context that uses the specified concurrency type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated convenience init(_ type: NSManagedObjectContext.ConcurrencyType)
```

## Parameters

- `type` — The context’s concurrency type. For possible values, see [ConcurrencyType](concurrencytype-swift.struct.md).

## Discussion

For more information, see [Concurrency](../nsmanagedobjectcontext.md#Concurrency).

## See Also

### Creating a context

- [ConcurrencyType](concurrencytype-swift.struct.md) — The concurrency types to use with a managed object context.
- [- initWithConcurrencyType:](<init(concurrencytype_).md>) — Creates a context that uses the specified concurrency type. _(deprecated)_
- [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md) — The concurrency types you can use with a managed object context.
