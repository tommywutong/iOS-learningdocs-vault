---
title: NSPersistentStoreForceDestroyOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreforcedestroyoption
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreforcedestroyoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreforcedestroyoption.json'
content_hash: 'sha256:f153d8080d8b57f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreForceDestroyOption

<sub>Global Variable</sub>

A flag that indicates the coordinator destroys the store file even if the operation might be unsafe, overriding locks, if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSPersistentStoreForceDestroyOption: String
```

## See Also

### Constants

- [NSReadOnlyPersistentStoreOption](nsreadonlypersistentstoreoption.md) — A flag that indicates whether a store is treated as read-only or not.
- [NSValidateXMLStoreOption](nsvalidatexmlstoreoption.md) — A flag that indicates whether an XML file should be validated with the DTD while opening.
- [NSPersistentStoreTimeoutOption](nspersistentstoretimeoutoption.md) — Options key that specifies the connection timeout for Core Data stores.
- [NSSQLitePragmasOption](nssqlitepragmasoption.md) — Options key for a dictionary of SQLite pragma settings with pragma values indexed by pragma names as keys.
- [NSSQLiteAnalyzeOption](nssqliteanalyzeoption.md) — Option key to run an analysis of the store data to optimize indices based on statistical information when the store is added to the coordinator.
- [NSSQLiteManualVacuumOption](nssqlitemanualvacuumoption.md) — Option key to rebuild the store file, forcing a database wide defragmentation when the store is added to the coordinator.
- [NSPersistentStoreFileProtectionKey](nspersistentstorefileprotectionkey.md) — Key to represent the protection class for the persistent store.
