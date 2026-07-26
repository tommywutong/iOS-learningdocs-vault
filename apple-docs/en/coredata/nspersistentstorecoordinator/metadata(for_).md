---
title: 'metadata(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/metadata(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadata(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/metadata%28for%3A%29.json'
content_hash: 'sha256:1b3d6a4fb944f447'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# metadata(for:)

<sub>Instance Method</sub>

Returns the metadata of the specified persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metadata(for store: NSPersistentStore) -> [String : Any]
```

## Parameters

- `store` — A persistent store.

## Return Value

A dictionary that contains the metadata currently stored or to-be-stored in `store`.

## See Also

### Related Documentation

- [+ setMetadata:forPersistentStoreOfType:URL:error:](<setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:error:](<metadataforpersistentstore(oftype_at_).md>) — Returns a dictionary containing the metadata stored in the persistent store at a given URL. _(deprecated)_

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](../nsstoretypekey.md) — A key that identifies the store type.
- [NSStoreUUIDKey](../nsstoreuuidkey.md) — A key that provides the store’s UUID.
