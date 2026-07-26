---
title: registeredStoreTypes
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator/registeredstoretypes
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registeredstoretypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/registeredstoretypes.json'
content_hash: 'sha256:4508db7de2d16a0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# registeredStoreTypes

<sub>Type Property</sub>

The coordinator’s registered store types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var registeredStoreTypes: [String : NSValue] { get }
```

## Return Value

A dictionary of the registered store types—the keys are the store type strings, and the values are the [NSPersistentStore](../nspersistentstore.md) subclasses.

## See Also

### Registering store types

- [registerStoreClass(_:type:)](<registerstoreclass(__type_).md>) — Registers a persistent store subclass using the specified store type.
- [+ registerStoreClass:forStoreType:](<registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
