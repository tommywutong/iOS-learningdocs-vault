---
title: 'init(concurrencyType:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nsmanagedobjectcontext/init(concurrencytype:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init(concurrencytype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/init%28concurrencytype%3A%29.json'
content_hash: 'sha256:e9663a62b7198e6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# init(concurrencyType:)

<sub>Initializer</sub>

Creates a context that uses the specified concurrency type.

> [!warning] Deprecated
> Use [init(_:)](<init(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(concurrencyType ct: NSManagedObjectContextConcurrencyType)
```

## Parameters

- `ct` — The context’s concurrency type. For possible values, see [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md).

## Discussion

For more information, see [Concurrency](../nsmanagedobjectcontext.md#Concurrency).

## See Also

### Creating a context

- [init(_:)](<init(__).md>) — Creates a context that uses the specified concurrency type.
- [ConcurrencyType](concurrencytype-swift.struct.md) — The concurrency types to use with a managed object context.
- [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md) — The concurrency types you can use with a managed object context.
