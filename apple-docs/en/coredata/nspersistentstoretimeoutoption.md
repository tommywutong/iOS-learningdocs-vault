---
title: NSPersistentStoreTimeoutOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoretimeoutoption
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoretimeoutoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoretimeoutoption.json'
content_hash: 'sha256:58cebe58421e854e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreTimeoutOption

<sub>Global Variable</sub>

Options key that specifies the connection timeout for Core Data stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSPersistentStoreTimeoutOption: String
```

## Discussion

The corresponding value is an `NSNumber` object that represents the duration in seconds that Core Data will wait while attempting to create a connection to a persistent store. If a connection is cannot be made within that timeframe, the operation is aborted and an error is returned.

## See Also

### Constants

- [NSReadOnlyPersistentStoreOption](nsreadonlypersistentstoreoption.md) — A flag that indicates whether a store is treated as read-only or not.
- [NSValidateXMLStoreOption](nsvalidatexmlstoreoption.md) — A flag that indicates whether an XML file should be validated with the DTD while opening.
- [NSSQLitePragmasOption](nssqlitepragmasoption.md) — Options key for a dictionary of SQLite pragma settings with pragma values indexed by pragma names as keys.
- [NSSQLiteAnalyzeOption](nssqliteanalyzeoption.md) — Option key to run an analysis of the store data to optimize indices based on statistical information when the store is added to the coordinator.
- [NSSQLiteManualVacuumOption](nssqlitemanualvacuumoption.md) — Option key to rebuild the store file, forcing a database wide defragmentation when the store is added to the coordinator.
- [NSPersistentStoreFileProtectionKey](nspersistentstorefileprotectionkey.md) — Key to represent the protection class for the persistent store.
- [NSPersistentStoreForceDestroyOption](nspersistentstoreforcedestroyoption.md) — A flag that indicates the coordinator destroys the store file even if the operation might be unsafe, overriding locks, if necessary.
