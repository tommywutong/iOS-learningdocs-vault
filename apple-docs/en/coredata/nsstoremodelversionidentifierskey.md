---
title: NSStoreModelVersionIdentifiersKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsstoremodelversionidentifierskey
source_url: 'https://developer.apple.com/documentation/coredata/nsstoremodelversionidentifierskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstoremodelversionidentifierskey.json'
content_hash: 'sha256:e904a6e4e2ef6ddf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSStoreModelVersionIdentifiersKey

<sub>Global Variable</sub>

Key to represent the version identifiers for the model used to create the store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSStoreModelVersionIdentifiersKey: String
```

## Discussion

If you add your own annotations to a model’s version identifier (see [versionIdentifiers](nsmanagedobjectmodel/versionidentifiers.md)), they are stored in the persistent store’s metadata. You can use this key to retrieve the identifiers from the metadata dictionaries available from `NSPersistentStore` ([metadata](nspersistentstore/metadata.md)) and `NSPersistentStoreCoordinator` ([- metadataForPersistentStore:](<nspersistentstorecoordinator/metadata(for_).md>) and related methods). The corresponding value is a Foundation collection (an `NSArray` or `NSSet` object).

## See Also

### Constants

- [NSStoreModelVersionHashesKey](nsstoremodelversionhasheskey.md) — Key to represent the version hash information for the model used to create the store.
- [NSPersistentStoreOSCompatibility](nspersistentstoreoscompatibility.md) — Key to represent the earliest version of the operation system that the persistent store supports.
