---
title: NSExternalRecordExtensionOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.6+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsexternalrecordextensionoption
source_url: 'https://developer.apple.com/documentation/coredata/nsexternalrecordextensionoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsexternalrecordextensionoption.json'
content_hash: 'sha256:d03bb6afcad2dff2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSExternalRecordExtensionOption

<sub>Global Variable</sub>

Option indicating the file extension to use for Spotlight external record files.

> [!warning] Deprecated
> Spotlight integration is deprecated. Use CoreSpotlight integration instead.

<sub>macOS</sub>

```swift
let NSExternalRecordExtensionOption: String
```

## See Also

### Deprecated

- [NSExternalRecordsDirectoryOption](nsexternalrecordsdirectoryoption.md) — Option indicating the directory where Spotlight external record files should be written to. _(deprecated)_
- [NSExternalRecordsFileFormatOption](nsexternalrecordsfileformatoption.md) — Option to specify the file format of a Spotlight external records. _(deprecated)_
- [NSPersistentStoreUbiquitousContentNameKey](nspersistentstoreubiquitouscontentnamekey.md) — Option to specify that a persistent store has a given name in ubiquity. _(deprecated)_
- [NSPersistentStoreUbiquitousContentURLKey](nspersistentstoreubiquitouscontenturlkey.md) — Option to specify the log path to use for ubiquitous content logs. _(deprecated)_
- [NSPersistentStoreUbiquitousPeerTokenOption](nspersistentstoreubiquitouspeertokenoption.md) — The corresponding value is an optionally specified string which will be mixed in to Core Data’s identifier for each iCloud peer. The value must be an alphanumeric string without any special characters, whitespace or punctuation. The primary use for this option is to allow multiple applications on the same peer (device) to share a Core Data store integrated with iCloud. Each application will require its own store file. _(deprecated)_
- [NSPersistentStoreRemoveUbiquitousMetadataOption](nspersistentstoreremoveubiquitousmetadataoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should remove all associated ubiquity metadata from a persistent store. You typically use this option during migration or copying to disassociate a persistent store file from an iCloud account. _(deprecated)_
- [NSPersistentStoreUbiquitousContainerIdentifierKey](nspersistentstoreubiquitouscontaineridentifierkey.md) — The a string specifying the iCloud container identifier. _(deprecated)_
- [NSPersistentStoreRebuildFromUbiquitousContentOption](nspersistentstorerebuildfromubiquitouscontentoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should erase the local store file and rebuild it from the iCloud data in Mobile Documents. _(deprecated)_
