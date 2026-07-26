---
title: NSPersistentStoreUbiquitousContentURLKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspersistentstoreubiquitouscontenturlkey
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontenturlkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreubiquitouscontenturlkey.json'
content_hash: 'sha256:459f8c0c532a42d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreUbiquitousContentURLKey

<sub>Global Variable</sub>

Option to specify the log path to use for ubiquitous content logs.

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let NSPersistentStoreUbiquitousContentURLKey: String
```

## Discussion

In iOS 6 and OS X 10.8 and below, this option is required for ubiquitous content to function. In iOS 7 and macOS 10.9 and later, it is optional.

## See Also

### Deprecated

- [NSExternalRecordsDirectoryOption](nsexternalrecordsdirectoryoption.md) — Option indicating the directory where Spotlight external record files should be written to. _(deprecated)_
- [NSExternalRecordExtensionOption](nsexternalrecordextensionoption.md) — Option indicating the file extension to use for Spotlight external record files. _(deprecated)_
- [NSExternalRecordsFileFormatOption](nsexternalrecordsfileformatoption.md) — Option to specify the file format of a Spotlight external records. _(deprecated)_
- [NSPersistentStoreUbiquitousContentNameKey](nspersistentstoreubiquitouscontentnamekey.md) — Option to specify that a persistent store has a given name in ubiquity. _(deprecated)_
- [NSPersistentStoreUbiquitousPeerTokenOption](nspersistentstoreubiquitouspeertokenoption.md) — The corresponding value is an optionally specified string which will be mixed in to Core Data’s identifier for each iCloud peer. The value must be an alphanumeric string without any special characters, whitespace or punctuation. The primary use for this option is to allow multiple applications on the same peer (device) to share a Core Data store integrated with iCloud. Each application will require its own store file. _(deprecated)_
- [NSPersistentStoreRemoveUbiquitousMetadataOption](nspersistentstoreremoveubiquitousmetadataoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should remove all associated ubiquity metadata from a persistent store. You typically use this option during migration or copying to disassociate a persistent store file from an iCloud account. _(deprecated)_
- [NSPersistentStoreUbiquitousContainerIdentifierKey](nspersistentstoreubiquitouscontaineridentifierkey.md) — The a string specifying the iCloud container identifier. _(deprecated)_
- [NSPersistentStoreRebuildFromUbiquitousContentOption](nspersistentstorerebuildfromubiquitouscontentoption.md) — The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should erase the local store file and rebuild it from the iCloud data in Mobile Documents. _(deprecated)_
