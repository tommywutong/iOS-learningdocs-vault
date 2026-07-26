---
title: NSPersistentStoreFileProtectionKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorefileprotectionkey
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorefileprotectionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorefileprotectionkey.json'
content_hash: 'sha256:a45c97905a6796a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreFileProtectionKey

<sub>Global Variable</sub>

Key to represent the protection class for the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
let NSPersistentStoreFileProtectionKey: String
```

## Discussion

Backward compatibility may preclude some features. The acceptable values are those defined for the [protectionKey](../foundation/fileattributekey/protectionkey.md). The default value is [completeUntilFirstUserAuthentication](../foundation/fileprotectiontype/completeuntilfirstuserauthentication.md) for all applications built on or after iOS v5.0. The default value for all older applications is [none](../foundation/fileprotectiontype/none.md).

## See Also

### Constants

- [NSReadOnlyPersistentStoreOption](nsreadonlypersistentstoreoption.md) — A flag that indicates whether a store is treated as read-only or not.
- [NSValidateXMLStoreOption](nsvalidatexmlstoreoption.md) — A flag that indicates whether an XML file should be validated with the DTD while opening.
- [NSPersistentStoreTimeoutOption](nspersistentstoretimeoutoption.md) — Options key that specifies the connection timeout for Core Data stores.
- [NSSQLitePragmasOption](nssqlitepragmasoption.md) — Options key for a dictionary of SQLite pragma settings with pragma values indexed by pragma names as keys.
- [NSSQLiteAnalyzeOption](nssqliteanalyzeoption.md) — Option key to run an analysis of the store data to optimize indices based on statistical information when the store is added to the coordinator.
- [NSSQLiteManualVacuumOption](nssqlitemanualvacuumoption.md) — Option key to rebuild the store file, forcing a database wide defragmentation when the store is added to the coordinator.
- [NSPersistentStoreForceDestroyOption](nspersistentstoreforcedestroyoption.md) — A flag that indicates the coordinator destroys the store file even if the operation might be unsafe, overriding locks, if necessary.
