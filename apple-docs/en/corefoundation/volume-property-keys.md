---
title: Volume Property Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/volume-property-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/volume-property-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/volume-property-keys.json'
content_hash: 'sha256:0ad887d675d4b13e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# Volume Property Keys

<sub>API Collection</sub>

Keys that apply to volumes.

## Topics

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
- [kCFURLVolumeSupportsRootDirectoryDatesKey](kcfurlvolumesupportsrootdirectorydateskey.md) — Key for determining whether the volume supports reliable storage of times for the root directory, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsVolumeSizesKey](kcfurlvolumesupportsvolumesizeskey.md) — Key for determining whether the volume supports returning volume size information, returned as a `CFBoolean` object. If `true`, volume size information is available as values of the [kCFURLVolumeTotalCapacityKey](kcfurlvolumetotalcapacitykey.md) and [kCFURLVolumeAvailableCapacityKey](kcfurlvolumeavailablecapacitykey.md) keys.
- [kCFURLVolumeSupportsRenamingKey](kcfurlvolumesupportsrenamingkey.md) — Key for determining whether the volume can be renamed, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsAdvisoryFileLockingKey](kcfurlvolumesupportsadvisoryfilelockingkey.md) — Key for determining whether the volume implements whole-file advisory locks in the style of flock, along with the `O_EXLOCK` and `O_SHLOCK` flags of the open function, returned as a `CFBoolean` object.
- [kCFURLVolumeSupportsExtendedSecurityKey](kcfurlvolumesupportsextendedsecuritykey.md) — Key for determining whether the volume supports extended security (access control lists), returned as a `CFBoolean` object.
- [kCFURLVolumeIsBrowsableKey](kcfurlvolumeisbrowsablekey.md) — Key for determining whether the volume is visible in GUI-based file-browsing environments, such as the Desktop or the Finder application, returned as a `CFBoolean` object.
- [kCFURLVolumeMaximumFileSizeKey](kcfurlvolumemaximumfilesizekey.md) — Key for the largest file size supported by the volume in bytes, returned as a `CFNumber` object, or `NULL` if it cannot be determined.
- [kCFURLVolumeIsEjectableKey](kcfurlvolumeisejectablekey.md) — Key for determining whether the volume is ejectable from the drive mechanism under software control, returned as a `CFBoolean` object.
- [kCFURLVolumeIsRemovableKey](kcfurlvolumeisremovablekey.md) — Key for determining whether the volume is removable from the drive mechanism, returned as a `CFBoolean` object.
- [kCFURLVolumeIsInternalKey](kcfurlvolumeisinternalkey.md) — Key for determining whether the volume is connected to an internal bus, returned as a `CFBoolean` object, or `NULL` if it cannot be determined.
- [kCFURLVolumeIsAutomountedKey](kcfurlvolumeisautomountedkey.md) — Key for determining whether the volume is automounted, returned as a `CFBoolean` object.
- [kCFURLVolumeIsLocalKey](kcfurlvolumeislocalkey.md) — Key for determining whether the volume is stored on a local device, returned as a `CFBoolean` object.
- [kCFURLVolumeIsReadOnlyKey](kcfurlvolumeisreadonlykey.md) — Key for determining whether the volume is read-only, returned as a `CFBoolean` object.
- [kCFURLVolumeCreationDateKey](kcfurlvolumecreationdatekey.md) — Key for the volume’s creation date, returned as a `CFDate` object, or `NULL` if it cannot be determined.
- [kCFURLVolumeURLForRemountingKey](kcfurlvolumeurlforremountingkey.md) — Key for the URL needed to remount the network volume, returned as a `CFURL` object, or `NULL` if a URL is not available.
- [kCFURLVolumeUUIDStringKey](kcfurlvolumeuuidstringkey.md) — Key for the volume’s persistent UUID, returned as a `CFString` object, or `NULL` if a persistent UUID is not available.

## See Also

### File System Constants

- [Common File System Resource Keys](common-file-system-resource-keys.md) — Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md) — Possible values for the [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md) — Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md) — These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md) — Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.
