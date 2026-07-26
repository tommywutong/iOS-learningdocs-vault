---
title: NSStoreTypeKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsstoretypekey
source_url: 'https://developer.apple.com/documentation/coredata/nsstoretypekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstoretypekey.json'
content_hash: 'sha256:621a0c591fea083a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSStoreTypeKey

<sub>Global Variable</sub>

A key that identifies the store type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSStoreTypeKey: String
```

## See Also

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<nspersistentstorecoordinator/setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<nspersistentstorecoordinator/metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<nspersistentstorecoordinator/metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<nspersistentstorecoordinator/setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreUUIDKey](nsstoreuuidkey.md) — A key that provides the store’s UUID.
