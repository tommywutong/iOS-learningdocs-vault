---
title: 'registerStoreClass(_:forStoreType:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:forstoretype:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:forstoretype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/registerstoreclass%28_%3Aforstoretype%3A%29.json'
content_hash: 'sha256:7228d7ceb7d68f04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# registerStoreClass(_:forStoreType:)

<sub>Type Method</sub>

Registers a persistent store subclass using the specified store type identifier.

> [!warning] Deprecated
> Use [registerStoreClass(_:type:)](<registerstoreclass(__type_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String)
```

## Parameters

- `storeClass` — The `NSPersistentStore` subclass to use for the store of type `storeType`.

- `storeType` — A unique string that identifies a store type.

## Discussion

You must invoke this method before a custom subclass of [NSPersistentStore](../nspersistentstore.md) can be loaded into a persistent store coordinator.

You can pass `nil` for `storeClass` to unregister the store type.

## See Also

### Registering store types

- [registerStoreClass(_:type:)](<registerstoreclass(__type_).md>) — Registers a persistent store subclass using the specified store type.
- [registeredStoreTypes](registeredstoretypes.md) — The coordinator’s registered store types.
