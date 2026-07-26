---
title: 'removeUbiquitousContentAndPersistentStore(at:options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore%28at%3Aoptions%3A%29.json'
content_hash: 'sha256:7a0503fa740f1cfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# removeUbiquitousContentAndPersistentStore(at:options:)

<sub>Type Method</sub>

Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func removeUbiquitousContentAndPersistentStore(at storeURL: URL, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `storeURL` — The URL of the store to delete.

- `options` — A dictionary containing the options normally passed to [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>).

## Discussion

Errors may be returned as a result of file I/O, iCloud network or iCloud account issues.

## See Also

### Deprecated type methods

- [+ elementsDerivedFromExternalRecordURL:](<elementsderived(fromexternalrecordat_).md>) — Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL. _(deprecated)_
- [+ metadataForPersistentStoreWithURL:error:](<metadataforpersistentstore(with_).md>) — Returns a dictionary that contains the metadata stored in the persistent store at the specified location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:error:](<metadataforpersistentstore(oftype_at_).md>) — Returns a dictionary containing the metadata stored in the persistent store at a given URL. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ registerStoreClass:forStoreType:](<registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:error:](<setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
