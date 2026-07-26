---
title: 'registerStoreClass(_:type:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:type:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/registerstoreclass%28_%3Atype%3A%29.json'
content_hash: 'sha256:0bba6dbe471af8f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# registerStoreClass(_:type:)

<sub>Type Method</sub>

Registers a persistent store subclass using the specified store type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func registerStoreClass(_ storeClass: AnyClass?, type: NSPersistentStore.StoreType)
```

## Parameters

- `storeClass` — A subclass of [NSPersistentStore](../nspersistentstore.md).

- `type` — The store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

## Discussion

You must register the subclass before you load instances of it into the persistent store coordinator. To unregister a subclass for a specific store type, use `nil` for `storeClass`.

## See Also

### Registering store types

- [+ registerStoreClass:forStoreType:](<registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [registeredStoreTypes](registeredstoretypes.md) — The coordinator’s registered store types.
