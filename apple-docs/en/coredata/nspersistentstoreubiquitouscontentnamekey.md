---
title: NSPersistentStoreUbiquitousContentNameKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspersistentstoreubiquitouscontentnamekey
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontentnamekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreubiquitouscontentnamekey.json'
content_hash: 'sha256:840253c121a4d570'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreUbiquitousContentNameKey

<sub>Global Variable</sub>

Option to specify that a persistent store has a given name in ubiquity.

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let NSPersistentStoreUbiquitousContentNameKey: String
```

## Discussion

This option is required for ubiquitous content to function.

## See Also

### Deprecated

- [NSExternalRecordsDirectoryOption](nsexternalrecordsdirectoryoption.md) — Option indicating the directory where Spotlight external record files should be written to. _(deprecated)_
- [NSExternalRecordExtensionOption](nsexternalrecordextensionoption.md) — Option indicating the file extension to use for Spotlight external record files. _(deprecated)_
- [NSExternalRecordsFileFormatOption](nsexternalrecordsfileformatoption.md) — Option to specify the file format of a Spotlight external records. _(deprecated)_
- [NSPersistentStoreUbiquitousContentURLKey](nspersistentstoreubiquitouscontenturlkey.md) — Option to specify the log path to use for ubiquitous content logs. _(deprecated)_
- [NSPersistentStoreUbiquitousPeerTokenOption](nspersistentstoreubiquitouspeertokenoption.md) — The corresponding value is an optionally specified string which will be mixed in to Core Data’s identifier for each iCloud peer. The value must be an alphanumeric string without any special characters, whitespace or punctuation. The primary use for this option is to allow multiple applications on the same peer (device) to share a Core Data store integrated with iCloud. Each application will require its own store file. _(deprecated)_
- [NSPersistentStoreRemoveUbiquitousMetadataOption](nspersistentstoreremoveubiquitousmetadataoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should remove all associated ubiquity metadata from a persistent store. You typically use this option during migration or copying to disassociate a persistent store file from an iCloud account. _(deprecated)_
- [NSPersistentStoreUbiquitousContainerIdentifierKey](nspersistentstoreubiquitouscontaineridentifierkey.md) — The a string specifying the iCloud container identifier. _(deprecated)_
- [NSPersistentStoreRebuildFromUbiquitousContentOption](nspersistentstorerebuildfromubiquitouscontentoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should erase the local store file and rebuild it from the iCloud data in Mobile Documents. _(deprecated)_
