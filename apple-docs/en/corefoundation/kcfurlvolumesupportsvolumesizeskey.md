---
title: kCFURLVolumeSupportsVolumeSizesKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfurlvolumesupportsvolumesizeskey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsvolumesizeskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlvolumesupportsvolumesizeskey.json'
content_hash: 'sha256:1f6680f10a52885b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLVolumeSupportsVolumeSizesKey

<sub>Global Variable</sub>

Key for determining whether the volume supports returning volume size information, returned as a `CFBoolean` object. If `true`, volume size information is available as values of the [kCFURLVolumeTotalCapacityKey](kcfurlvolumetotalcapacitykey.md) and [kCFURLVolumeAvailableCapacityKey](kcfurlvolumeavailablecapacitykey.md) keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFURLVolumeSupportsVolumeSizesKey: CFString!
```

## See Also

### Constants

- [kCFURLVolumeNameKey](kcfurlvolumenamekey.md) — The name of the volume, returned as a `CFString` object.
- [kCFURLVolumeLocalizedNameKey](kcfurlvolumelocalizednamekey.md) — The user-presentable name of the volume, returned as a `CFString` object.
- [kCFURLVolumeLocalizedFormatDescriptionKey](kcfurlvolumelocalizedformatdescriptionkey.md) — Key for the volume’s descriptive format name, returned as a `CFString` object.
- [kCFURLVolumeTotalCapacityKey](kcfurlvolumetotalcapacitykey.md) — Key for the volume’s capacity in bytes, returned as a `CFNumber` object.
- [kCFURLVolumeAvailableCapacityKey](kcfurlvolumeavailablecapacitykey.md) — Key for the volume’s available capacity in bytes, returned as a `CFNumber` object.
- [kCFURLVolumeResourceCountKey](kcfurlvolumeresourcecountkey.md) — Key for the total number of resources on the volume, returned as a `CFNumber` object.
- [kCFURLVolumeSupportsPersistentIDsKey](kcfurlvolumesupportspersistentidskey.md) — Key for determining whether the volume supports persistent IDs, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsSymbolicLinksKey](kcfurlvolumesupportssymboliclinkskey.md) — Key for determining whether the volume supports symbolic links, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsHardLinksKey](kcfurlvolumesupportshardlinkskey.md) — Key for determining whether the volume supports hard links, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsJournalingKey](kcfurlvolumesupportsjournalingkey.md) — Key for determining whether the volume supports journaling, returned as a `CFBoolean` object.
- [kCFURLVolumeIsJournalingKey](kcfurlvolumeisjournalingkey.md) — Key for determining whether the volume is currently journaling, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsSparseFilesKey](kcfurlvolumesupportssparsefileskey.md) — Key for determining whether the volume supports sparse files, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsZeroRunsKey](kcfurlvolumesupportszerorunskey.md) — Key for determining whether the volume supports zero runs, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsCaseSensitiveNamesKey](kcfurlvolumesupportscasesensitivenameskey.md) — Key for determining whether the volume supports case-sensitive names, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsCasePreservedNamesKey](kcfurlvolumesupportscasepreservednameskey.md) — Key for determining whether the volume supports case-preserved names, returned as a `CFBoolean` object.
