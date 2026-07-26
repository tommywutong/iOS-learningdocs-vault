---
title: 'setMetadata(_:type:at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:type:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:type:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/setmetadata%28_%3Atype%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:13cc00ac493e0c6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# setMetadata(_:type:at:options:)

<sub>Type Method</sub>

Updates the metadata of a specific type of persistent store at the provided location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setMetadata(_ metadata: [String : Any]?, type storeType: NSPersistentStore.StoreType, at storeURL: URL, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `metadata` — A dictionary that contains the metadata to associate with the store.

- `storeType` — The store type. For possible values, see [StoreType](../nspersistentstore/storetype.md).

- `storeURL` — The store’s location.

- `options` — A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Managing a store’s metadata

- [metadataForPersistentStore(type:at:options:)](<metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](../nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](../nsstoreuuidkey.md) — A key that provides the store’s UUID.
