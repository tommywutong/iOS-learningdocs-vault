---
title: NSStoreUUIDKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsstoreuuidkey
source_url: 'https://developer.apple.com/documentation/coredata/nsstoreuuidkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstoreuuidkey.json'
content_hash: 'sha256:2b349fa73297d9fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSStoreUUIDKey

<sub>Global Variable</sub>

A key that provides the store’s UUID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSStoreUUIDKey: String
```

## Discussion

The store UUID is useful to identify stores through URI representations, but it is _not_ guaranteed to be unique. The UUID generated for new stores is unique—users can freely copy files and thus the UUID stored inside—so if you track or reference stores explicitly you need to be aware of duplicate UUIDs and potentially override the UUID when a new store is added to the list of known stores in your application.

## See Also

### Managing a store’s metadata

- [setMetadata(_:type:at:options:)](<nspersistentstorecoordinator/setmetadata(__type_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location.
- [metadataForPersistentStore(type:at:options:)](<nspersistentstorecoordinator/metadataforpersistentstore(type_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location.
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [- metadataForPersistentStore:](<nspersistentstorecoordinator/metadata(for_).md>) — Returns the metadata of the specified persistent store.
- [- setMetadata:forPersistentStore:](<nspersistentstorecoordinator/setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [NSStoreTypeKey](nsstoretypekey.md) — A key that identifies the store type.
