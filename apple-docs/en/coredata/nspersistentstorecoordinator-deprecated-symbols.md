---
title: Deprecated Symbols
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator-deprecated-symbols.json'
content_hash: 'sha256:eb6d51352565eb62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Core Data stack](core-data-stack.md) · [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)

# Deprecated Symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Deprecated constants

- [NSXMLExternalRecordType](nsxmlexternalrecordtype.md) — Specifies an XML file format. _(deprecated)_
- [NSBinaryExternalRecordType](nsbinaryexternalrecordtype.md) — Specifies a binary file format _(deprecated)_

### Deprecated enumerations

- [NSPersistentStoreUbiquitousTransitionType](nspersistentstoreubiquitoustransitiontype.md) — These constants are used as the value corresponding to the [NSPersistentStoreUbiquitousTransitionTypeKey](nspersistentstoreubiquitoustransitiontypekey.md) in the user info dictionary of [NSPersistentStoreCoordinatorStoresWillChangeNotification](nspersistentstorecoordinatorstoreswillchangenotification.md) and [NSPersistentStoreCoordinatorStoresDidChangeNotification](nspersistentstorecoordinatorstoresdidchangenotification.md) notifications to identify the type of event leading to a change. _(deprecated)_

### Deprecated type properties

- [NSPersistentStoreDidImportUbiquitousContentChanges](../foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md) — Posted after records are imported from the ubiquitous content store. _(deprecated)_

### Deprecated type methods

- [+ elementsDerivedFromExternalRecordURL:](<nspersistentstorecoordinator/elementsderived(fromexternalrecordat_).md>) — Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL. _(deprecated)_
- [+ metadataForPersistentStoreWithURL:error:](<nspersistentstorecoordinator/metadataforpersistentstore(with_).md>) — Returns a dictionary that contains the metadata stored in the persistent store at the specified location. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:error:](<nspersistentstorecoordinator/metadataforpersistentstore(oftype_at_).md>) — Returns a dictionary containing the metadata stored in the persistent store at a given URL. _(deprecated)_
- [+ metadataForPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/metadataforpersistentstore(oftype_at_options_).md>) — Returns the metadata of a specific type of persistent store at the provided location. _(deprecated)_
- [+ registerStoreClass:forStoreType:](<nspersistentstorecoordinator/registerstoreclass(__forstoretype_).md>) — Registers a persistent store subclass using the specified store type identifier. _(deprecated)_
- [+ removeUbiquitousContentAndPersistentStoreAtURL:options:error:](<nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at_options_).md>) — Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:error:](<nspersistentstorecoordinator/setmetadata(__forpersistentstoreoftype_at_).md>) — Sets the metadata for a given store. _(deprecated)_
- [+ setMetadata:forPersistentStoreOfType:URL:options:error:](<nspersistentstorecoordinator/setmetadata(__forpersistentstoreoftype_at_options_).md>) — Updates the metadata of a specific type of persistent store at the provided location. _(deprecated)_

### Deprecated instance methods

- [- addPersistentStoreWithType:configuration:URL:options:error:](<nspersistentstorecoordinator/addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- destroyPersistentStoreAtURL:withType:options:error:](<nspersistentstorecoordinator/destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:](<nspersistentstorecoordinator/importstore(withidentifier_fromexternalrecordsdirectoryat_to_options_oftype_).md>) — Creates and populates a store with the external records found at a given URL. _(deprecated)_
- [- lock](<nspersistentstorecoordinator/lock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<nspersistentstorecoordinator/migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<nspersistentstorecoordinator/replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
- [- tryLock](<nspersistentstorecoordinator/trylock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- unlock](<nspersistentstorecoordinator/unlock().md>) — Relinquishes a previously acquired lock. _(deprecated)_
- [- performBlock:](<nspersistentstorecoordinator/perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<nspersistentstorecoordinator/performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
