---
title: 'elementsDerived(fromExternalRecordAt:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.6+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/elementsderived(fromexternalrecordat:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/elementsderived(fromexternalrecordat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/elementsderived%28fromexternalrecordat%3A%29.json'
content_hash: 'sha256:9b098168a4511839'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# elementsDerived(fromExternalRecordAt:)

<sub>Type Method</sub>

Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.

> [!warning] Deprecated
> Spotlight integration is deprecated. Use CoreSpotlight integration instead.

<sub>macOS</sub>

```swift
class func elementsDerived(fromExternalRecordAt fileURL: URL) -> [AnyHashable : Any]
```

## Parameters

- `fileURL` — A file URL specifying the location of a Spotlight external record file.

## Return Value

A dictionary containing the parsed elements derived from the Spotlight support file specified by `fileURL`.

## Discussion

Dictionary keys and the corresponding values are described in [Spotlight record keys](../spotlight-record-keys.md).

## See Also

### Deprecated type methods

- [+ metadataForPersistentStoreWithURL:error:](<metadataforpersistentstore(with_).md>) — Returns a dictionary that contains the metadata stored in the persistent store at the specified location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:error:](<metadataforpersistentstore(oftype_at_).md>) — Returns a dictionary containing the metadata stored in the persistent store at a given URL. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ registerStoreClass:forStoreType:](<registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [+ removeUbiquitousContentAndPersistentStoreAtURL:options:error:](<removeubiquitouscontentandpersistentstore(at_options_).md>) — Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:error:](<setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
