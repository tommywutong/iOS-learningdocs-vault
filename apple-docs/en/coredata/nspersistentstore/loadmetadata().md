---
title: loadMetadata()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/loadmetadata()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/loadmetadata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/loadmetadata%28%29.json'
content_hash: 'sha256:6ab80637c776ae70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# loadMetadata()

<sub>Instance Method</sub>

Instructs the persistent store to load its metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadMetadata() throws
```

## Discussion

There is no way to return an error if the store is invalid.

## See Also

### Managing Store Metadata

- [+ metadataForPersistentStoreWithURL:error:](<metadataforpersistentstore(with_).md>) — Returns the metadata from the persistent store at the given URL.
- [+ setMetadata:forPersistentStoreWithURL:error:](<setmetadata(__forpersistentstoreat_).md>) — Sets the metadata for the store at a given URL.
- [metadata](metadata.md) — The metadata for the persistent store.
