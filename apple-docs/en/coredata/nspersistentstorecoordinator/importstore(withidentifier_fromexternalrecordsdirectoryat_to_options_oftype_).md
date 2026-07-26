---
title: 'importStore(withIdentifier:fromExternalRecordsDirectoryAt:to:options:ofType:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/importstore(withidentifier:fromexternalrecordsdirectoryat:to:options:oftype:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/importstore(withidentifier:fromexternalrecordsdirectoryat:to:options:oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/importstore%28withidentifier%3Afromexternalrecordsdirectoryat%3Ato%3Aoptions%3Aoftype%3A%29.json'
content_hash: 'sha256:25d24647ab034824'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# importStore(withIdentifier:fromExternalRecordsDirectoryAt:to:options:ofType:)

<sub>Instance Method</sub>

Creates and populates a store with the external records found at a given URL.

> [!warning] Deprecated
> Spotlight integration is deprecated. Use CoreSpotlight integration instead.

<sub>macOS</sub>

```swift
func importStore(withIdentifier storeIdentifier: String?, fromExternalRecordsDirectoryAt externalRecordsURL: URL, to destinationURL: URL, options: [AnyHashable : Any]? = nil, ofType storeType: String) throws -> NSPersistentStore
```

## Parameters

- `storeIdentifier` — The identifier for a store. If this value is `nil` then the method imports the records for the first store found.

- `externalRecordsURL` — The location of the directory containing external records.

- `destinationURL` — An URL object that specifies the location for the new store. There should be no existing store at this location, as the store will be created from scratch (appending to an existing store is not allowed).

- `options` — A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see [Store options](../store-options.md).

- `storeType` — A string constant (such as `NSSQLiteStoreType`) that specifies the type of the new store—see [Persistent Store Types](../persistent-store-types.md).

## Return Value

An object representing the newly-created store.

## See Also

### Related Documentation

- [- removePersistentStore:error:](<remove(__).md>) — Removes the specified persistent store from the coordinator.
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_

### Deprecated instance methods

- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- lock](<lock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
- [- tryLock](<trylock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- unlock](<unlock().md>) — Relinquishes a previously acquired lock. _(deprecated)_
- [- performBlock:](<perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
