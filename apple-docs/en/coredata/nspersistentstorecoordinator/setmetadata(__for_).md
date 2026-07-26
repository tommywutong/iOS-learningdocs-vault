---
title: 'setMetadata(_:for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/setmetadata%28_%3Afor%3A%29.json'
content_hash: 'sha256:fd9e92a9ce1b4a28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# setMetadata(_:for:)

<sub>Instance Method</sub>

Updates the metadata for the specified persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setMetadata(_ metadata: [String : Any]?, for store: NSPersistentStore)
```

## Parameters

- `metadata` — A dictionary containing metadata for the store.

- `store` — A persistent store.

## Discussion

The store type and UUID (`NSStoreTypeKey` and `NSStoreUUIDKey`) are always added automatically, however `NSStoreUUIDKey` is only added if it is not set manually as part of the dictionary argument.

> [!important] Important
> Setting the metadata for a store does not change the information on disk until the store is actually saved.

## See Also

### Related Documentation

- [+ setMetadata:forPersistentStoreOfType:URL:error:](<setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:error:](<metadataforpersistentstore(oftype_at_).md>) — Returns a dictionary containing the metadata stored in the persistent store at a given URL. _(deprecated)_

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [NSStoreTypeKey](../nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](../nsstoreuuidkey.md) — A key that provides the store’s UUID.
