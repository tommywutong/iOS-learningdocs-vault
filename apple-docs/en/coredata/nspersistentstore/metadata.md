---
title: metadata
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/metadata
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/metadata.json'
content_hash: 'sha256:87dc1758fa83a063'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# metadata

<sub>Instance Property</sub>

The metadata for the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var metadata: [String : Any]! { get set }
```

## Discussion

The dictionary must include the store type ([NSStoreTypeKey](../nsstoretypekey.md)) and UUID ([NSStoreUUIDKey](../nsstoreuuidkey.md)).

### Special Considerations

Subclasses must override this property to provide storage and persistence for the store metadata.

## See Also

### Managing Store Metadata

- [+ metadataForPersistentStoreWithURL:error:](<metadataforpersistentstore(with_).md>) — Returns the metadata from the persistent store at the given URL.
- [+ setMetadata:forPersistentStoreWithURL:error:](<setmetadata(__forpersistentstoreat_).md>) — Sets the metadata for the store at a given URL.
- [- loadMetadata:](<loadmetadata().md>) — Instructs the persistent store to load its metadata.
