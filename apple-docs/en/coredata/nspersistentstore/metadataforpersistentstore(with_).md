---
title: 'metadataForPersistentStore(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstore/metadataforpersistentstore(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/metadataforpersistentstore(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/metadataforpersistentstore%28with%3A%29.json'
content_hash: 'sha256:8ecac4b6784d43cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# metadataForPersistentStore(with:)

<sub>Type Method</sub>

Returns the metadata from the persistent store at the given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataForPersistentStore(with url: URL) throws -> [String : Any]
```

## Parameters

- `url` — The location of the store.

## Return Value

The metadata from the persistent store at `url`. Returns `nil` if there is an error.

## Discussion

Subclasses must override this method.

## See Also

### Managing Store Metadata

- [+ setMetadata:forPersistentStoreWithURL:error:](<setmetadata(__forpersistentstoreat_).md>) — Sets the metadata for the store at a given URL.
- [- loadMetadata:](<loadmetadata().md>) — Instructs the persistent store to load its metadata.
- [metadata](metadata.md) — The metadata for the persistent store.
