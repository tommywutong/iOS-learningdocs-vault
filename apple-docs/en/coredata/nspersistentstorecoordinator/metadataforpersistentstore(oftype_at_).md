---
title: 'metadataForPersistentStore(ofType:at:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+（9.0 起废弃）, iPadOS 3.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.11 起废弃）, tvOS（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/metadataforpersistentstore%28oftype%3Aat%3A%29.json'
content_hash: 'sha256:52b092b36eef30ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# metadataForPersistentStore(ofType:at:)

<sub>Type Method</sub>

Returns a dictionary containing the metadata stored in the persistent store at a given URL.

> [!warning] Deprecated
> Use -metadataForPersistentStoreOfType:URL:options:error: and pass in an options dictionary matching addPersistentStoreWithType

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func metadataForPersistentStore(ofType storeType: String?, at url: URL) throws -> [String : Any]
```

## Parameters

- `storeType` — The type of the store at `url`. If this value is `nil`, Core Data determines which store class should be used to get or set the store file’s metadata by inspecting the file contents.

- `url` — The location of a persistent store.

## Return Value

A dictionary containing the metadata stored in the persistent store at `url`, or `nil` if the store cannot be opened or if there is a problem accessing its contents.

## Discussion

The keys guaranteed to be in this dictionary are [NSStoreTypeKey](../nsstoretypekey.md) and [NSStoreUUIDKey](../nsstoreuuidkey.md).

## Discussion

You can use this method to retrieve the metadata from a store without the overhead of creating a Core Data stack.

## See Also

### Related Documentation

- [- setMetadata:forPersistentStore:](<setmetadata(__for_).md>) — Updates the metadata for the specified persistent store.
- [- metadataForPersistentStore:](<metadata(for_).md>) — Returns the metadata of the specified persistent store.

### Deprecated type methods

- [+ elementsDerivedFromExternalRecordURL:](<elementsderived(fromexternalrecordat_).md>) — Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL. _(deprecated)_
- [+ metadataForPersistentStoreWithURL:error:](<metadataforpersistentstore(with_).md>) — Returns a dictionary that contains the metadata stored in the persistent store at the specified location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ registerStoreClass:forStoreType:](<registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [+ removeUbiquitousContentAndPersistentStoreAtURL:options:error:](<removeubiquitouscontentandpersistentstore(at_options_).md>) — Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:error:](<setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_
