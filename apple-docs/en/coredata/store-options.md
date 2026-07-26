---
title: Store options
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/store-options
source_url: 'https://developer.apple.com/documentation/coredata/store-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/store-options.json'
content_hash: 'sha256:b20d1106903d782a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Core Data stack](core-data-stack.md) · [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)

# Store options

<sub>API Collection</sub>

The options keys that configure the behavior and characteristics of a persistent store.

## Topics

### Constants

- [NSReadOnlyPersistentStoreOption](nsreadonlypersistentstoreoption.md) — A flag that indicates whether a store is treated as read-only or not.
- [NSValidateXMLStoreOption](nsvalidatexmlstoreoption.md) — A flag that indicates whether an XML file should be validated with the DTD while opening.
- [NSPersistentStoreTimeoutOption](nspersistentstoretimeoutoption.md) — Options key that specifies the connection timeout for Core Data stores.
- [NSSQLitePragmasOption](nssqlitepragmasoption.md) — Options key for a dictionary of SQLite pragma settings with pragma values indexed by pragma names as keys.
- [NSSQLiteAnalyzeOption](nssqliteanalyzeoption.md) — Option key to run an analysis of the store data to optimize indices based on statistical information when the store is added to the coordinator.
- [NSSQLiteManualVacuumOption](nssqlitemanualvacuumoption.md) — Option key to rebuild the store file, forcing a database wide defragmentation when the store is added to the coordinator.
- [NSPersistentStoreFileProtectionKey](nspersistentstorefileprotectionkey.md) — Key to represent the protection class for the persistent store.
- [NSPersistentStoreForceDestroyOption](nspersistentstoreforcedestroyoption.md) — A flag that indicates the coordinator destroys the store file even if the operation might be unsafe, overriding locks, if necessary.

### Deprecated

- [NSExternalRecordsDirectoryOption](nsexternalrecordsdirectoryoption.md) — Option indicating the directory where Spotlight external record files should be written to. _(deprecated)_
- [NSExternalRecordExtensionOption](nsexternalrecordextensionoption.md) — Option indicating the file extension to use for Spotlight external record files. _(deprecated)_
- [NSExternalRecordsFileFormatOption](nsexternalrecordsfileformatoption.md) — Option to specify the file format of a Spotlight external records. _(deprecated)_
- [NSPersistentStoreUbiquitousContentNameKey](nspersistentstoreubiquitouscontentnamekey.md) — Option to specify that a persistent store has a given name in ubiquity. _(deprecated)_
- [NSPersistentStoreUbiquitousContentURLKey](nspersistentstoreubiquitouscontenturlkey.md) — Option to specify the log path to use for ubiquitous content logs. _(deprecated)_
- [NSPersistentStoreUbiquitousPeerTokenOption](nspersistentstoreubiquitouspeertokenoption.md) — The corresponding value is an optionally specified string which will be mixed in to Core Data’s identifier for each iCloud peer. The value must be an alphanumeric string without any special characters, whitespace or punctuation. The primary use for this option is to allow multiple applications on the same peer (device) to share a Core Data store integrated with iCloud. Each application will require its own store file. _(deprecated)_
- [NSPersistentStoreRemoveUbiquitousMetadataOption](nspersistentstoreremoveubiquitousmetadataoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should remove all associated ubiquity metadata from a persistent store. You typically use this option during migration or copying to disassociate a persistent store file from an iCloud account. _(deprecated)_
- [NSPersistentStoreUbiquitousContainerIdentifierKey](nspersistentstoreubiquitouscontaineridentifierkey.md) — The a string specifying the iCloud container identifier. _(deprecated)_
- [NSPersistentStoreRebuildFromUbiquitousContentOption](nspersistentstorerebuildfromubiquitouscontentoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should erase the local store file and rebuild it from the iCloud data in Mobile Documents. _(deprecated)_

## See Also

### Creating a persistent store coordinator

- [- initWithManagedObjectModel:](<nspersistentstorecoordinator/init(managedobjectmodel_).md>) — Creates a persistent store coordinator with the specified managed object model.
- [Migration options](migration-options.md) — The options keys that configure the migration behavior of a persistent store.
- [Store versions](store-versions.md) — The metadata keys you use when comparing store versions.
