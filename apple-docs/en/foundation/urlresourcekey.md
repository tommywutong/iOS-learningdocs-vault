---
title: URLResourceKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey.json'
content_hash: 'sha256:ae486947a10aaa59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLResourceKey

<sub>Structure</sub>

Keys that apply to file system URLs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLResourceKey
```

## Discussion

To request information using one of these keys, pass it to the `forKey:` parameter of the [- getResourceValue:forKey:error:](<nsurl/getresourcevalue(__forkey_).md>) instance method.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Application keys

- [NSURLIsApplicationKey](urlresourcekey/isapplicationkey.md) — `true` if resource is an application (Read-only, value type boolean `NSNumber`).
- [NSURLApplicationIsScriptableKey](urlresourcekey/applicationisscriptablekey.md) — `true` if the resource is scriptable. Only applies to applications (Read-only, value type boolean `NSNumber`).

### Directory keys

- [NSURLIsDirectoryKey](urlresourcekey/isdirectorykey.md) — A key for determining whether the resource is a directory.
- [NSURLParentDirectoryURLKey](urlresourcekey/parentdirectoryurlkey.md) — The container directory of the resource.
- [NSURLDirectoryEntryCountKey](urlresourcekey/directoryentrycountkey.md) — The key for a count of items in the directory.

### File keys

- [NSURLFileAllocatedSizeKey](urlresourcekey/fileallocatedsizekey.md) — The key for the total allocated size on-disk for the file.
- [NSURLFileProtectionKey](urlresourcekey/fileprotectionkey.md) — The key for the protection level of the file.
- [URLFileProtection](urlfileprotection.md) — Protection-level values for a URL resource key.
- [NSURLFileContentIdentifierKey](urlresourcekey/filecontentidentifierkey.md) — The key for a value that APFS assigns to identify a file’s content data stream.
- [NSURLFileResourceIdentifierKey](urlresourcekey/fileresourceidentifierkey.md) — The key for the resource’s unique identifier.
- [NSURLFileResourceTypeKey](urlresourcekey/fileresourcetypekey.md) — The key for the resource’s object type.
- [URLFileResourceType](urlfileresourcetype.md) — Possible values for the type of file resource.
- [NSURLFileSecurityKey](urlresourcekey/filesecuritykey.md) — The key for the resource’s security information.
- [NSURLFileSizeKey](urlresourcekey/filesizekey.md) — The key for the file’s size, in bytes.
- [NSURLIsAliasFileKey](urlresourcekey/isaliasfilekey.md) — The key for determining whether the file is an alias.
- [NSURLIsPackageKey](urlresourcekey/ispackagekey.md) — The key for determining whether the resource is a file package.
- [NSURLIsRegularFileKey](urlresourcekey/isregularfilekey.md) — The key for determining whether the resource is a regular file rather than a directory or a symbolic link.
- [NSURLIsPurgeableKey](urlresourcekey/ispurgeablekey.md) — The key for a Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [NSURLIsSparseKey](urlresourcekey/issparsekey.md) — The key for a Boolean value that indicates whether the file has sparse regions.
- [NSURLMayHaveExtendedAttributesKey](urlresourcekey/mayhaveextendedattributeskey.md) — The key for a Boolean value that indicates whether the file has extended attributes.
- [NSURLMayShareFileContentKey](urlresourcekey/maysharefilecontentkey.md) — The key for a Boolean value that indicates whether cloned files and their original files may share data blocks.
- [NSURLPreferredIOBlockSizeKey](urlresourcekey/preferredioblocksizekey.md) — The key for the optimal block size to use when reading or writing the file’s data.
- [NSURLTotalFileAllocatedSizeKey](urlresourcekey/totalfileallocatedsizekey.md) — The key for the total allocated size of the file, in bytes.
- [NSURLTotalFileSizeKey](urlresourcekey/totalfilesizekey.md) — The key for the total displayable size of the file, in bytes.
- [NSURLFileIdentifierKey](urlresourcekey/fileidentifierkey.md) — The key for the file system’s internal inode identifier for the item.

### Volume capacity keys

- [Checking Volume Storage Capacity](checking-volume-storage-capacity.md) — Confirm that you have enough local storage space for a large amount of data.
- [NSURLVolumeAvailableCapacityKey](urlresourcekey/volumeavailablecapacitykey.md) — Key for the volume’s available capacity in bytes (read-only).
- [NSURLVolumeAvailableCapacityForImportantUsageKey](urlresourcekey/volumeavailablecapacityforimportantusagekey.md) — Key for the volume’s available capacity in bytes for storing important resources (read-only).
- [NSURLVolumeAvailableCapacityForOpportunisticUsageKey](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md) — Key for the volume’s available capacity in bytes for storing nonessential resources (read-only).
- [NSURLVolumeTotalCapacityKey](urlresourcekey/volumetotalcapacitykey.md) — Key for the volume’s total capacity in bytes (read-only).

### Volume status keys

- [NSURLVolumeIsAutomountedKey](urlresourcekey/volumeisautomountedkey.md) — A key for determining whether the volume is automounted.
- [NSURLVolumeIsBrowsableKey](urlresourcekey/volumeisbrowsablekey.md) — A key for determining whether the volume is visible in GUI-based file-browsing environments, such as the Desktop or the Finder app.
- [NSURLVolumeIsEjectableKey](urlresourcekey/volumeisejectablekey.md) — A key for determining whether the volume is ejectable from the drive mechanism under software control.
- [NSURLVolumeIsEncryptedKey](urlresourcekey/volumeisencryptedkey.md) — A key for determining whether the volume is encrypted.
- [NSURLVolumeIsInternalKey](urlresourcekey/volumeisinternalkey.md) — A key for determining whether the volume is connected to an internal bus.
- [NSURLVolumeIsJournalingKey](urlresourcekey/volumeisjournalingkey.md) — A key for determining whether the volume is currently journaling.
- [NSURLVolumeIsLocalKey](urlresourcekey/volumeislocalkey.md) — A key for determining whether the volume is on a local device.
- [NSURLVolumeIsReadOnlyKey](urlresourcekey/volumeisreadonlykey.md) — A key for determining whether the volume is read-only.
- [NSURLVolumeIsRemovableKey](urlresourcekey/volumeisremovablekey.md) — A key for determining whether the volume is removable from the drive mechanism.
- [NSURLVolumeIsRootFileSystemKey](urlresourcekey/volumeisrootfilesystemkey.md) — A key for determining whether the volume is the root file system.
- [NSURLVolumeSupportsFileProtectionKey](urlresourcekey/volumesupportsfileprotectionkey.md) — A Boolean value that indicates the volume supports data protection for files.
- [NSURLVolumeTypeNameKey](urlresourcekey/volumetypenamekey.md) — The key for the name of the file system type.
- [NSURLVolumeSubtypeKey](urlresourcekey/volumesubtypekey.md) — The key for the file system subtype value.
- [NSURLVolumeMountFromLocationKey](urlresourcekey/volumemountfromlocationkey.md) — The key for the volume mounted-from location.

### Volume support keys

- [NSURLIsMountTriggerKey](urlresourcekey/ismounttriggerkey.md) — Key for determining whether the URL is a file system trigger directory, returned as a Boolean `NSNumber` object (read-only). Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [NSURLIsVolumeKey](urlresourcekey/isvolumekey.md) — Key for determining whether the resource is the root directory of a volume, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeCreationDateKey](urlresourcekey/volumecreationdatekey.md) — Key for the volume’s creation date, returned as an `NSDate` object, or `NULL` if it cannot be determined (read-only).
- [NSURLVolumeIdentifierKey](urlresourcekey/volumeidentifierkey.md) — The unique identifier of the resource’s volume, returned as an `id` (read-only).
- [NSURLVolumeLocalizedFormatDescriptionKey](urlresourcekey/volumelocalizedformatdescriptionkey.md) — Key for the volume’s descriptive format name, returned as an `NSString` object (read-only).
- [NSURLVolumeLocalizedNameKey](urlresourcekey/volumelocalizednamekey.md) — The name of the volume as it should be displayed in the user interface, returned as an `NSString` object (read-only).
- [NSURLVolumeMaximumFileSizeKey](urlresourcekey/volumemaximumfilesizekey.md) — Key for the largest file size supported by the volume in bytes, returned as a Boolean `NSNumber` object, or `nil` if it cannot be determined (read-only).
- [NSURLVolumeNameKey](urlresourcekey/volumenamekey.md) — The name of the volume, returned as an string object.
- [NSURLVolumeResourceCountKey](urlresourcekey/volumeresourcecountkey.md) — Key for the total number of resources on the volume, returned as an `NSNumber` object (read-only).
- [NSURLVolumeSupportsAccessPermissionsKey](urlresourcekey/volumesupportsaccesspermissionskey.md) — `true` if the volume supports setting POSIX access permissions with the `NSURLFileSecurityKey` property. (Read-only, value type boolean `NSNumber`).
- [NSURLVolumeSupportsAdvisoryFileLockingKey](urlresourcekey/volumesupportsadvisoryfilelockingkey.md) — Key for determining whether the volume implements whole-file advisory locks in the style of flock, along with the `O_EXLOCK` and `O_SHLOCK` flags of the open function, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsCasePreservedNamesKey](urlresourcekey/volumesupportscasepreservednameskey.md) — Key for determining whether the volume supports case-preserved names, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsCaseSensitiveNamesKey](urlresourcekey/volumesupportscasesensitivenameskey.md) — Key for determining whether the volume supports case-sensitive names, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsCompressionKey](urlresourcekey/volumesupportscompressionkey.md) — Whether the volume supports transparent decompression of compressed files using `decmpfs`, returned as `NSNumber` containing a Boolean value (read-only).
- [NSURLVolumeSupportsExclusiveRenamingKey](urlresourcekey/volumesupportsexclusiverenamingkey.md) — Whether the volume supports exclusive renaming using `renamex_np(2)` with the `RENAME_EXCL` option, returned as `NSNumber` containing a Boolean value (read-only).
- [NSURLVolumeSupportsExtendedSecurityKey](urlresourcekey/volumesupportsextendedsecuritykey.md) — Key for determining whether the volume supports extended security (access control lists), returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsFileCloningKey](urlresourcekey/volumesupportsfilecloningkey.md) — Whether the volume supports cloning using `clonefile(2)`, returned as `NSNumber` containing a Boolean value (read-only).
- [NSURLVolumeSupportsHardLinksKey](urlresourcekey/volumesupportshardlinkskey.md) — Key for determining whether the volume supports hard links, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsImmutableFilesKey](urlresourcekey/volumesupportsimmutablefileskey.md) — `true` if the volume supports making files immutable with the `NSURLIsUserImmutableKey` or `NSURLIsSystemImmutableKey` properties. (Read-only, value type boolean `NSNumber`).
- [NSURLVolumeSupportsJournalingKey](urlresourcekey/volumesupportsjournalingkey.md) — Key for determining whether the volume supports journaling, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsPersistentIDsKey](urlresourcekey/volumesupportspersistentidskey.md) — Key for determining whether the volume supports persistent IDs, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsRenamingKey](urlresourcekey/volumesupportsrenamingkey.md) — Key for determining whether the volume can be renamed, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsRootDirectoryDatesKey](urlresourcekey/volumesupportsrootdirectorydateskey.md) — Key for determining whether the volume supports reliable storage of times for the root directory, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsSparseFilesKey](urlresourcekey/volumesupportssparsefileskey.md) — Key for determining whether the volume supports sparse files, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsSwapRenamingKey](urlresourcekey/volumesupportsswaprenamingkey.md) — Whether the volume supports renaming using `renamex_np(2)` with the `RENAME_SWAP` option, returned as `NSNumber` containing a Boolean value (read-only).
- [NSURLVolumeSupportsSymbolicLinksKey](urlresourcekey/volumesupportssymboliclinkskey.md) — Key for determining whether the volume supports symbolic links, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeSupportsVolumeSizesKey](urlresourcekey/volumesupportsvolumesizeskey.md) — Key for determining whether the volume supports returning volume size information, returned as a Boolean `NSNumber` object (read-only). If `true`, volume size information is available as values of the [NSURLVolumeTotalCapacityKey](urlresourcekey/volumetotalcapacitykey.md) and[NSURLVolumeAvailableCapacityKey](urlresourcekey/volumeavailablecapacitykey.md) keys.
- [NSURLVolumeSupportsZeroRunsKey](urlresourcekey/volumesupportszerorunskey.md) — Key for determining whether the volume supports zero runs, returned as a Boolean `NSNumber` object (read-only).
- [NSURLVolumeURLForRemountingKey](urlresourcekey/volumeurlforremountingkey.md) — Key for the URL needed to remount the network volume, returned as an `NSURL` object, or `nil` if a URL is not available (read-only).
- [NSURLVolumeURLKey](urlresourcekey/volumeurlkey.md) — The root directory of the resource’s volume, returned as an `NSURL` object (read-only).
- [NSURLVolumeUUIDStringKey](urlresourcekey/volumeuuidstringkey.md) — Key for the volume’s persistent UUID, returned as an `NSString` object, or `nil` if a persistent UUID is not available (read-only).

### Ubiquitous keys

- [NSURLIsUbiquitousItemKey](urlresourcekey/isubiquitousitemkey.md) — The key for a Boolean value that indicates whether the item is in iCloud storage.
- [NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey](urlresourcekey/ubiquitousshareditemmostrecenteditornamecomponentskey.md) — The key for the name components of the most recent editor.
- [NSURLUbiquitousItemDownloadRequestedKey](urlresourcekey/ubiquitousitemdownloadrequestedkey.md) — The key for a Boolean value that indicates whether the system has already made a call [- startDownloadingUbiquitousItemAtURL:error:](<filemanager/startdownloadingubiquitousitem(at_).md>) to download the item.
- [NSURLUbiquitousItemIsDownloadingKey](urlresourcekey/ubiquitousitemisdownloadingkey.md) — The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [NSURLUbiquitousItemDownloadingErrorKey](urlresourcekey/ubiquitousitemdownloadingerrorkey.md) — The key for an error object that indicates why downloading the item from iCloud fails.
- [NSURLUbiquitousItemDownloadingStatusKey](urlresourcekey/ubiquitousitemdownloadingstatuskey.md) — The key for the current download state for the item.
- [URLUbiquitousItemDownloadingStatus](urlubiquitousitemdownloadingstatus.md) — Values that describe the iCloud storage state of a file.
- [NSURLUbiquitousItemIsExcludedFromSyncKey](urlresourcekey/ubiquitousitemisexcludedfromsynckey.md) — The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [NSURLUbiquitousItemIsUploadedKey](urlresourcekey/ubiquitousitemisuploadedkey.md) — The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [NSURLUbiquitousItemIsUploadingKey](urlresourcekey/ubiquitousitemisuploadingkey.md) — The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [NSURLUbiquitousItemUploadingErrorKey](urlresourcekey/ubiquitousitemuploadingerrorkey.md) — The key for an error object that indicates why uploading the item to iCloud fails.
- [NSURLUbiquitousItemHasUnresolvedConflictsKey](urlresourcekey/ubiquitousitemhasunresolvedconflictskey.md) — The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [NSURLUbiquitousItemContainerDisplayNameKey](urlresourcekey/ubiquitousitemcontainerdisplaynamekey.md) — The key for a string that contains the name of the item’s container as it appears to the user.
- [NSURLUbiquitousSharedItemOwnerNameComponentsKey](urlresourcekey/ubiquitousshareditemownernamecomponentskey.md) — The key for the name components of the item’s owner.
- [NSURLUbiquitousSharedItemCurrentUserPermissionsKey](urlresourcekey/ubiquitousshareditemcurrentuserpermissionskey.md) — The key for the current user’s permissions.
- [NSURLUbiquitousSharedItemCurrentUserRoleKey](urlresourcekey/ubiquitousshareditemcurrentuserrolekey.md) — The key for the role of the current user.
- [NSURLUbiquitousItemIsSharedKey](urlresourcekey/ubiquitousitemissharedkey.md) — The key for a Boolean value that indicates a shared item.
- [URLUbiquitousSharedItemRole](urlubiquitousshareditemrole.md) — The key for the role of a shared item.
- [URLUbiquitousSharedItemPermissions](urlubiquitousshareditempermissions.md) — The key for the permissions of a shared item.
- [NSURLUbiquitousItemIsSyncPausedKey](urlresourcekey/ubiquitousitemissyncpausedkey.md) — A Boolean value that indicates whether sync is paused for this item (value type boolean `NSNumber`).
- [NSURLUbiquitousItemSupportedSyncControlsKey](urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md) — The read-only value of the `NSFileManagerSupportedSyncControls` options (value type `NSNumber`).

### Thumbnail keys

- [NSURLThumbnailKey](urlresourcekey/thumbnailkey.md) — All thumbnails as a single NSImage (read-write). _(deprecated)_
- [NSURLThumbnailDictionaryKey](urlresourcekey/thumbnaildictionarykey.md) — A dictionary of NSImage/UIImage objects keyed by size (read-write). See [URLThumbnailDictionaryItem](urlthumbnaildictionaryitem.md) for a list of possible keys. _(deprecated)_
- [URLThumbnailDictionaryItem](urlthumbnaildictionaryitem.md) — Possible keys for the [NSURLThumbnailDictionaryKey](urlresourcekey/thumbnaildictionarykey.md) dictionary.

### Other resource keys

- [NSURLKeysOfUnsetValuesKey](urlresourcekey/keysofunsetvalueskey.md) — Key for the resource properties that have not been set after the [- setResourceValues:error:](<nsurl/setresourcevalues(__).md>) method returns an error, returned as an array of `NSString` objects.
- [NSURLQuarantinePropertiesKey](urlresourcekey/quarantinepropertieskey.md)
- [NSURLAddedToDirectoryDateKey](urlresourcekey/addedtodirectorydatekey.md) — The time at which the resource’s was created or renamed into or within its parent directory, returned as an `NSDate`. Inconsistent behavior may be observed when this attribute is requested on hard-linked items. This property is not supported by all volumes. (read-only)
- [NSURLAttributeModificationDateKey](urlresourcekey/attributemodificationdatekey.md) — The time at which the resource’s attributes were most recently modified, returned as an `NSDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported (read-only).
- [NSURLContentAccessDateKey](urlresourcekey/contentaccessdatekey.md) — The time at which the resource was most recently accessed.
- [NSURLContentModificationDateKey](urlresourcekey/contentmodificationdatekey.md) — The time at which the resource was most recently modified.
- [NSURLCreationDateKey](urlresourcekey/creationdatekey.md) — The time at which the resource was created.
- [NSURLCustomIconKey](urlresourcekey/customiconkey.md) — The icon stored with the resource, returned as an `NSImage` object, or `nil` if the resource has no custom icon.
- [NSURLDocumentIdentifierKey](urlresourcekey/documentidentifierkey.md) — The document identifier returned as an `NSNumber` (read-only).
- [NSURLEffectiveIconKey](urlresourcekey/effectiveiconkey.md) — The resource’s normal icon, returned as an `NSImage` object (read-only).
- [NSURLGenerationIdentifierKey](urlresourcekey/generationidentifierkey.md) — An opaque generation identifier, returned as an `id <NSCopying, NSCoding, NSObject>` (read-only)
- [NSURLHasHiddenExtensionKey](urlresourcekey/hashiddenextensionkey.md) — Key for determining whether the resource’s extension is normally removed from its localized name, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsExcludedFromBackupKey](urlresourcekey/isexcludedfrombackupkey.md) — A key for indicating whether the system excludes the resource from all backups of app data.
- [NSURLIsExecutableKey](urlresourcekey/isexecutablekey.md) — Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a Boolean `NSNumber` object (read-only).
- [NSURLIsHiddenKey](urlresourcekey/ishiddenkey.md) — Key for determining whether the resource is normally not displayed to users, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsReadableKey](urlresourcekey/isreadablekey.md) — Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a Boolean `NSNumber` object (read-only).
- [NSURLIsSymbolicLinkKey](urlresourcekey/issymboliclinkkey.md) — Key for determining whether the resource is a symbolic link, returned as a Boolean `NSNumber` object (read-only).
- [NSURLIsSystemImmutableKey](urlresourcekey/issystemimmutablekey.md) — Key for determining whether the resource’s system immutable bit is set, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsUserImmutableKey](urlresourcekey/isuserimmutablekey.md) — Key for determining whether the resource’s user immutable bit is set, returned as a Boolean `NSNumber` object (read-write).
- [NSURLIsWritableKey](urlresourcekey/iswritablekey.md) — Key for determining whether the current process (as determined by the EUID) can write to the resource, returned as a Boolean `NSNumber` object (read-only).
- [NSURLLabelColorKey](urlresourcekey/labelcolorkey.md) — The resource’s label color, returned as an `NSColor` object, or `nil` if the resource has no label color (read-only).
- [NSURLLabelNumberKey](urlresourcekey/labelnumberkey.md) — The resource’s label number, returned as an `NSNumber` object (read-write).
- [NSURLLinkCountKey](urlresourcekey/linkcountkey.md) — The number of hard links to the resource, returned as an `NSNumber` object (read-only).
- [NSURLLocalizedLabelKey](urlresourcekey/localizedlabelkey.md) — The resource’s localized label text, returned as an `NSString` object, or `nil` if the resource has no localized label text (read-only).
- [NSURLLocalizedNameKey](urlresourcekey/localizednamekey.md) — The resource’s localized or extension-hidden name, returned as an `NSString` object (read-only).
- [NSURLLocalizedTypeDescriptionKey](urlresourcekey/localizedtypedescriptionkey.md) — The resource’s localized type description, returned as an `NSString` object (read-only).
- [NSURLNameKey](urlresourcekey/namekey.md) — The resource’s name in the file system, returned as an `NSString` object (read-write).
- [NSURLPathKey](urlresourcekey/pathkey.md) — The file system path for the URL, returned as an [NSString](nsstring.md) object (read-only).
- [NSURLCanonicalPathKey](urlresourcekey/canonicalpathkey.md)
- [NSURLTagNamesKey](urlresourcekey/tagnameskey.md) — The names of tags attached to the resource, returned as an array of `NSString` values (read-write).
- [NSURLTypeIdentifierKey](urlresourcekey/typeidentifierkey.md) — The resource’s uniform type identifier (UTI), returned as an `NSString` object (read-only). _(deprecated)_
- [NSURLContentTypeKey](urlresourcekey/contenttypekey.md) — The resource’s type.

### Initializers

- [init(_:)](<urlresourcekey/init(__).md>)
- [init(rawValue:)](<urlresourcekey/init(rawvalue_).md>)

### Deprecated

- [NSURLUbiquitousItemIsDownloadedKey](urlresourcekey/ubiquitousitemisdownloadedkey.md) — The key for a Boolean value that indicates whether the system downloaded this item’s data from iCloud storage. _(deprecated)_
- [NSURLUbiquitousItemPercentDownloadedKey](urlresourcekey/ubiquitousitempercentdownloadedkey.md) — The key for a value that indicates the percentage of data that the system downloaded from iCloud storage. _(deprecated)_
- [NSURLUbiquitousItemPercentUploadedKey](urlresourcekey/ubiquitousitempercentuploadedkey.md) — The key for a value that indicates the percentage of data that the system uploaded to iCloud storage. _(deprecated)_

## See Also

### Accessing Resource Values

- [- resourceValuesForKeys:error:](<nsurl/resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.
- [- getResourceValue:forKey:error:](<nsurl/getresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- setResourceValue:forKey:error:](<nsurl/setresourcevalue(__forkey_).md>) — Sets the URL’s resource property for a given key to a given value.
- [- setResourceValues:error:](<nsurl/setresourcevalues(__).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [- removeAllCachedResourceValues](<nsurl/removeallcachedresourcevalues().md>) — Removes all cached resource values and temporary resource values from the URL object.
- [- removeCachedResourceValueForKey:](<nsurl/removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given key from the URL object.
- [- setTemporaryResourceValue:forKey:](<nsurl/settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
