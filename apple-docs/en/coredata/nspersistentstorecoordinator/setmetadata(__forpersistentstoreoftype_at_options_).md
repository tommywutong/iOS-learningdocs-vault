---
title: 'setMetadata(_:forPersistentStoreOfType:at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/setmetadata%28_%3Aforpersistentstoreoftype%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:e659855259465a8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# setMetadata(_:forPersistentStoreOfType:at:options:)

<sub>Type Method</sub>

Updates the metadata of a specific type of persistent store at the provided location.

> [!warning] Deprecated
> Use [setMetadata(_:type:at:options:)](<setmetadata(__type_at_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreOfType storeType: String, at url: URL, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `metadata` — A dictionary that contains the metadata to store.

- `storeType` — The type of store. If `nil`, Core Data automatically attempts to determine the store class to use.

- `url` — The file URL of the store.

- `options` — A dictionary that contains options for the store.

## See Also

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](../nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](../nsstoreuuidkey.md) — A key that provides the store’s UUID.
