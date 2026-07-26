---
title: type
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/type
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/type.json'
content_hash: 'sha256:3ebff9fc78931b40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# type

<sub>Instance Property</sub>

The type string of the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var type: String { get }
```

## Discussion

This string is used when specifying the type of store to add to a persistent store coordinator.

### Special Considerations

Subclasses must override this method to provide a unique type.

## See Also

### Getting Store Configuration

- [configurationName](configurationname.md) — The name of the managed object model configuration that creates the persistent store.
- [options](options.md) — The options that Core Data uses to create the store.
- [persistentStoreCoordinator](persistentstorecoordinator.md) — The persistent store coordinator that loads the persistent store.
- [StoreType](storetype.md) — The types of persistent stores that Core Data supports.
- [Persistent Store Types](../persistent-store-types.md) — Persist data through the available store types.
