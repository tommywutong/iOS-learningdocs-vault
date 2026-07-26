---
title: parent
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/parent
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/parent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/parent.json'
content_hash: 'sha256:e2d1d0d610b54db7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# parent

<sub>Instance Property</sub>

The parent of the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var parent: NSManagedObjectContext? { get set }
```

## Discussion

`nil` indicates there is no parent context. For more details, see [Parent store](../nsmanagedobjectcontext.md#Parent-store).

## See Also

### Configuring a context

- [persistentStoreCoordinator](persistentstorecoordinator.md) — The persistent store coordinator of the context.
- [name](name.md) — The developer-provided name of the context.
- [userInfo](userinfo.md) — The user information for the context.
