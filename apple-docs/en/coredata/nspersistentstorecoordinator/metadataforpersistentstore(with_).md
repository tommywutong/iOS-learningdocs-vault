---
title: 'metadataForPersistentStore(with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore%28with%3A%29.json'
content_hash: 'sha256:c22fd4c993cab368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# metadataForPersistentStore(with:)

<sub>Type Method</sub>

Returns a dictionary that contains the metadata stored in the persistent store at the specified location.

> [!warning] Deprecated
> Use [+ metadataForPersistentStoreOfType:URL:error:](<metadataforpersistentstore(oftype_at_).md>) instead.

<sub>Mac Catalyst</sub>

```swift
class func metadataForPersistentStore(with url: URL) throws -> [AnyHashable : Any]
```

## Parameters

- `url` — An URL object that specifies the location of a persistent store.

## Return Value

A dictionary containing the metadata for the persistent store at `url`. If no store is found, or there is a problem accessing its contents, returns `nil`. The keys guaranteed to be in this dictionary are `NSStoreTypeKey` and `NSStoreUUIDKey`.

## Discussion

This method allows you to access the metadata in a persistent store without initializing a Core Data stack.

## See Also

### Related Documentation

- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.

### Deprecated type methods

- [+ elementsDerivedFromExternalRecordURL:](<elementsderived(fromexternalrecordat_).md>) — Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:error:](<metadataforpersistentstore(oftype_at_).md>) — Returns a dictionary containing the metadata stored in the persistent store at a given URL. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ registerStoreClass:forStoreType:](<registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [+ removeUbiquitousContentAndPersistentStoreAtURL:options:error:](<removeubiquitouscontentandpersistentstore(at_options_).md>) — Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:error:](<setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
