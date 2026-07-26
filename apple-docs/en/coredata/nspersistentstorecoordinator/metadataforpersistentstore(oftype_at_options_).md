---
title: 'metadataForPersistentStore(ofType:at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore%28oftype%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:fa8d70e890aa84c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# metadataForPersistentStore(ofType:at:options:)

<sub>Type Method</sub>

Returns the metadata of a specific type of persistent store at the provided location.

> [!warning] Deprecated
> Use [metadataForPersistentStore(type:at:options:)](<metadataforpersistentstore(type_at_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataForPersistentStore(ofType storeType: String, at url: URL, options: [AnyHashable : Any]? = nil) throws -> [String : Any]
```

## Parameters

- `storeType` — The type of the store. If `nil`, Core Data automatically attempts to determine the store class to use.

- `url` — The file URL of the store.

- `options` — A dictionary that contains options for the store.

## Return Value

A dictionary that contains, at a minimum, values for the [NSStoreTypeKey](../nsstoretypekey.md) and [NSStoreUUIDKey](../nsstoreuuidkey.md) keys.

## See Also

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](../nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](../nsstoreuuidkey.md) — A key that provides the store’s UUID.
