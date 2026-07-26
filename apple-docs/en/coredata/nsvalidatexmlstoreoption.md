---
title: NSValidateXMLStoreOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsvalidatexmlstoreoption
source_url: 'https://developer.apple.com/documentation/coredata/nsvalidatexmlstoreoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsvalidatexmlstoreoption.json'
content_hash: 'sha256:5da395192b5d3d13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSValidateXMLStoreOption

<sub>Global Variable</sub>

A flag that indicates whether an XML file should be validated with the DTD while opening.

<sub>macOS</sub>

```swift
let NSValidateXMLStoreOption: String
```

## Discussion

The default value is [false](../swift/false.md).

## See Also

### Constants

- [NSReadOnlyPersistentStoreOption](nsreadonlypersistentstoreoption.md) — A flag that indicates whether a store is treated as read-only or not.
- [NSPersistentStoreTimeoutOption](nspersistentstoretimeoutoption.md) — Options key that specifies the connection timeout for Core Data stores.
- [NSSQLitePragmasOption](nssqlitepragmasoption.md) — Options key for a dictionary of SQLite pragma settings with pragma values indexed by pragma names as keys.
- [NSSQLiteAnalyzeOption](nssqliteanalyzeoption.md) — Option key to run an analysis of the store data to optimize indices based on statistical information when the store is added to the coordinator.
- [NSSQLiteManualVacuumOption](nssqlitemanualvacuumoption.md) — Option key to rebuild the store file, forcing a database wide defragmentation when the store is added to the coordinator.
- [NSPersistentStoreFileProtectionKey](nspersistentstorefileprotectionkey.md) — Key to represent the protection class for the persistent store.
- [NSPersistentStoreForceDestroyOption](nspersistentstoreforcedestroyoption.md) — A flag that indicates the coordinator destroys the store file even if the operation might be unsafe, overriding locks, if necessary.
