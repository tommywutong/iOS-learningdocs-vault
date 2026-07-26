---
title: 'metadataForPersistentStore(type:at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(type:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(type:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore%28type%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:f080ba75ee8aac1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# metadataForPersistentStore(type:at:options:)

<sub>Type Method</sub>

Returns the metadata of a specific type of persistent store at the provided location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataForPersistentStore(type storeType: NSPersistentStore.StoreType, at storeURL: URL, options: [AnyHashable : Any]? = nil) throws -> [String : Any]
```

## Parameters

- `storeType` — The store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `storeURL` — The store’s location.

- `options` — A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](../nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](../nsstoreuuidkey.md) — A key that provides the store’s UUID.
