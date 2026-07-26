---
title: 'setMetadata(_:forPersistentStoreAt:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstore/setmetadata(_:forpersistentstoreat:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/setmetadata(_:forpersistentstoreat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/setmetadata%28_%3Aforpersistentstoreat%3A%29.json'
content_hash: 'sha256:7b5c286224a90b82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# setMetadata(_:forPersistentStoreAt:)

<sub>Type Method</sub>

Sets the metadata for the store at a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreAt url: URL) throws
```

## Parameters

- `metadata` — The metadata for the store at `url`.

- `url` — The location of the store.

## Discussion

Subclasses must override this method to set metadata appropriately.

## See Also

### Managing Store Metadata

- [+ metadataForPersistentStoreWithURL:error:](<metadataforpersistentstore(with_).md>) — Returns the metadata from the persistent store at the given URL.
- [- loadMetadata:](<loadmetadata().md>) — Instructs the persistent store to load its metadata.
- [metadata](metadata.md) — The metadata for the persistent store.
