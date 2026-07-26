---
title: URLResourceValues
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues.json'
content_hash: 'sha256:239ce9f6bff60f0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLResourceValues

<sub>Structure</sub>

The properties that the file system resources support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLResourceValues
```

## Overview

Not all property values exist for all file system URLs. For example, if a file is located on a volume that doesn’t support creation dates, you can request the creation date property, but the request returns `nil` and doesn’t generate an error.

Only the fields requested by the keys you pass into the `URL` function to receive this value will be populated. The other fields return `nil` regardless of the underlying property on the file system.

As a convenience, you can request volume resource values from any file system URL. The value returned reflects the property value for the volume that the resource is located on.

## Topics

### Application values

- [applicationIsScriptable](urlresourcevalues/applicationisscriptable.md) — A Boolean value that indicates whether the application is scriptable.
- [isApplication](urlresourcevalues/isapplication.md) — A Boolean value that indicates whether the resource is an application.

### Directory values

- [isDirectory](urlresourcevalues/isdirectory.md) — A Boolean value that indicates whether the resource is a directory.
- [directoryEntryCount](urlresourcevalues/directoryentrycount.md) — The count of file system objects in the directory.

### File values

- [documentIdentifier](urlresourcevalues/documentidentifier.md) — A value that the kernel assigns to identify a document.
- [fileContentIdentifier](urlresourcevalues/filecontentidentifier.md) — A value APFS assigns that identifies a file’s content data stream.
- [fileAllocatedSize](urlresourcevalues/fileallocatedsize.md) — The total allocated size on-disk for the file, in bytes.
- [fileProtection](urlresourcevalues/fileprotection.md) — The protection level for the file.
- [fileResourceIdentifier](urlresourcevalues/fileresourceidentifier.md) — An identifier for comparing two file system objects for equality.
- [fileResourceType](urlresourcevalues/fileresourcetype.md) — The type of the file system object.
- [fileSecurity](urlresourcevalues/filesecurity.md) — The file system object’s security information.
- [fileSize](urlresourcevalues/filesize.md) — The total file size, in bytes.
- [isPurgeable](urlresourcevalues/ispurgeable.md) — A Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [isSparse](urlresourcevalues/issparse.md) — A Boolean value that indicates whether the file has sparse regions.
- [mayHaveExtendedAttributes](urlresourcevalues/mayhaveextendedattributes.md) — A Boolean value that indicates the file may have extended attributes.
- [isExecutable](urlresourcevalues/isexecutable.md) — A Boolean value that indicates whether you can execute the file resource or search a directory resource.
- [isRegularFile](urlresourcevalues/isregularfile.md) — A Boolean value that indicates whether the resource is a regular file.
- [mayShareFileContent](urlresourcevalues/maysharefilecontent.md) — A Boolean value that indicates whether the cloned files and their original files may share data blocks.
- [totalFileAllocatedSize](urlresourcevalues/totalfileallocatedsize.md) — The total allocated size of the file, in bytes.
- [totalFileSize](urlresourcevalues/totalfilesize.md) — The total displayable size of the file, in bytes.
- [fileIdentifier](urlresourcevalues/fileidentifier.md) — The file system’s internal inode identifier for the item.

### Volume capacity values

- [volumeAvailableCapacity](urlresourcevalues/volumeavailablecapacity.md) — The volume’s available capacity, in bytes.
- [volumeAvailableCapacityForImportantUsage](urlresourcevalues/volumeavailablecapacityforimportantusage.md) — The volume’s available capacity for storing important resources, in bytes.
- [volumeAvailableCapacityForOpportunisticUsage](urlresourcevalues/volumeavailablecapacityforopportunisticusage.md) — The volume’s available capacity for storing nonessential resources, in bytes.
- [volumeTotalCapacity](urlresourcevalues/volumetotalcapacity.md) — The volume’s total capacity, in bytes.

### Volume status values

- [volumeIsAutomounted](urlresourcevalues/volumeisautomounted.md) — A Boolean value that indicates whether the volume is automounted.
- [volumeIsBrowsable](urlresourcevalues/volumeisbrowsable.md) — A Boolean value that indicates whether the volume is visible through the user interface.
- [volumeIsEjectable](urlresourcevalues/volumeisejectable.md) — A Boolean value that indicates whether the volume’s media is ejectable from the drive mechanism under software control.
- [volumeIsEncrypted](urlresourcevalues/volumeisencrypted.md) — A Boolean value that indicates whether the volume is encrypted.
- [volumeIsInternal](urlresourcevalues/volumeisinternal.md) — A Boolean value that indicates whether the volume’s device is connected to an internal bus, or nil if not available.
- [volumeIsJournaling](urlresourcevalues/volumeisjournaling.md) — A Boolean value that indicates whether the volume is currently using a journal for speedy recovery after an unplanned restart.
- [volumeIsLocal](urlresourcevalues/volumeislocal.md) — A Boolean value that indicates whether the volume is on a local device.
- [volumeIsReadOnly](urlresourcevalues/volumeisreadonly.md) — A Boolean value that indicates whether the volume is read-only.
- [volumeIsRemovable](urlresourcevalues/volumeisremovable.md) — A Boolean value that indicates whether the volume’s media is removable from the drive mechanism.
- [volumeIsRootFileSystem](urlresourcevalues/volumeisrootfilesystem.md) — A Boolean value that indicates whether the volume is the root file system.
- [volumeTypeName](urlresourcevalues/volumetypename.md) — The volume’s type name, as a string.
- [volumeSubtype](urlresourcevalues/volumesubtype.md) — An integer value that indicates the file system subtype.
- [volumeMountFromLocation](urlresourcevalues/volumemountfromlocation.md) — The file system device location, as a string.

### Volume support values

- [isMountTrigger](urlresourcevalues/ismounttrigger.md) — A Boolean value that indicates whether this URL is a file system trigger directory.
- [isVolume](urlresourcevalues/isvolume.md) — A Boolean value that indicates whether the root directory is a volume.
- [volume](urlresourcevalues/volume.md) — URL of the volume on which the resource is stored.
- [volumeCreationDate](urlresourcevalues/volumecreationdate.md) — The volume’s creation date, or `nil` if this cannot be determined.
- [volumeIdentifier](urlresourcevalues/volumeidentifier.md) — An identifier that identifies the volume the file system object is on.
- [volumeLocalizedFormatDescription](urlresourcevalues/volumelocalizedformatdescription.md) — The volume format that’s visible to the user.
- [volumeLocalizedName](urlresourcevalues/volumelocalizedname.md) — The name of the volume that’s visible to the user.
- [volumeMaximumFileSize](urlresourcevalues/volumemaximumfilesize.md) — The largest file size supported by this file system, in bytes, or `nil` if this cannot be determined.
- [volumeName](urlresourcevalues/volumename.md) — The name of the volume.
- [volumeResourceCount](urlresourcevalues/volumeresourcecount.md) — The total number of resources on the volume.
- [volumeSupportsAccessPermissions](urlresourcevalues/volumesupportsaccesspermissions.md) — A Boolean value that indicates whether the volume supports setting standard access permissions.
- [volumeSupportsAdvisoryFileLocking](urlresourcevalues/volumesupportsadvisoryfilelocking.md) — A Boolean value that indicates whether the volume implements whole-file flock(2) style advisory locks, and the O_EXLOCK and O_SHLOCK flags of the open(2) call.
- [volumeSupportsCasePreservedNames](urlresourcevalues/volumesupportscasepreservednames.md) — A Boolean value that indicates whether the volume format preserves the case of file and directory names.
- [volumeSupportsCaseSensitiveNames](urlresourcevalues/volumesupportscasesensitivenames.md) — A Boolean value that indicates whether the volume format treats upper and lower case characters in file and directory names as different.
- [volumeSupportsCompression](urlresourcevalues/volumesupportscompression.md) — A Boolean value that indicates whether the volume supports transparent decompression of compressed files using decmpfs.
- [volumeSupportsExclusiveRenaming](urlresourcevalues/volumesupportsexclusiverenaming.md) — A Boolean value that indicates whether the volume warns of a pre-existing destination when renaming a file.
- [volumeSupportsExtendedSecurity](urlresourcevalues/volumesupportsextendedsecurity.md) — A Boolean value that indicates whether the volume implements extended security (ACLs).
- [volumeSupportsFileCloning](urlresourcevalues/volumesupportsfilecloning.md) — A Boolean value that indicates whether the volume supports file cloning.
- [volumeSupportsHardLinks](urlresourcevalues/volumesupportshardlinks.md) — A Boolean value that indicates whether the volume format supports hard links.
- [volumeSupportsImmutableFiles](urlresourcevalues/volumesupportsimmutablefiles.md) — A Boolean value that indicates whether the volume supports making files immutable.
- [volumeSupportsJournaling](urlresourcevalues/volumesupportsjournaling.md) — A Boolean value that indicates whether the volume format supports a journal used to speed recovery in case of unplanned restart (such as a power outage or crash).
- [volumeSupportsPersistentIDs](urlresourcevalues/volumesupportspersistentids.md) — A Boolean value that indicates whether the volume format supports persistent object identifiers and can look up file system objects by their IDs.
- [volumeSupportsRenaming](urlresourcevalues/volumesupportsrenaming.md) — A Boolean value that indicates whether the volume can be renamed.
- [volumeSupportsRootDirectoryDates](urlresourcevalues/volumesupportsrootdirectorydates.md) — A Boolean value that indicates whether the volume supports reliable storage of times for the root directory.
- [volumeSupportsSparseFiles](urlresourcevalues/volumesupportssparsefiles.md) — A Boolean value that indicates whether the volume format supports sparse files.
- [volumeSupportsSwapRenaming](urlresourcevalues/volumesupportsswaprenaming.md) — A Boolean value that indicates whether the volume supports swapping source and target files when both exist.
- [volumeSupportsSymbolicLinks](urlresourcevalues/volumesupportssymboliclinks.md) — A Boolean value that indicates whether the volume format supports symbolic links.
- [volumeSupportsVolumeSizes](urlresourcevalues/volumesupportsvolumesizes.md) — A Boolean value that indicates whether the volume supports returning volume size values.
- [volumeSupportsZeroRuns](urlresourcevalues/volumesupportszeroruns.md) — A Boolean value that indicates whether the volume keeps track of allocated but unwritten parts of a file so that it can substitute zeroes without actually writing zeroes to the media.
- [volumeURLForRemounting](urlresourcevalues/volumeurlforremounting.md) — The `URL` needed to remount a network volume, or `nil` if not available.
- [volumeUUIDString](urlresourcevalues/volumeuuidstring.md) — The volume’s persistent `UUID` as a string, or `nil` if a persistent `UUID` is not available for the volume.

### Ubiquitous values

- [isUbiquitousItem](urlresourcevalues/isubiquitousitem.md) — A Boolean value that indicates whether the item is in the iCloud storage.
- [ubiquitousItemIsShared](urlresourcevalues/ubiquitousitemisshared.md) — A Boolean value that indicates a shared item.
- [ubiquitousItemIsExcludedFromSync](urlresourcevalues/ubiquitousitemisexcludedfromsync.md) — A Boolean value that indicates the system excludes the item from syncing.
- [ubiquitousSharedItemCurrentUserPermissions](urlresourcevalues/ubiquitousshareditemcurrentuserpermissions.md) — The current user’s permissions for the shared item.
- [ubiquitousSharedItemCurrentUserRole](urlresourcevalues/ubiquitousshareditemcurrentuserrole.md) — The current user’s role for the shared item.
- [ubiquitousSharedItemMostRecentEditorNameComponents](urlresourcevalues/ubiquitousshareditemmostrecenteditornamecomponents.md) — The name components of the most recent editor of the shared item.
- [ubiquitousSharedItemOwnerNameComponents](urlresourcevalues/ubiquitousshareditemownernamecomponents.md) — The name components of the owner of the shared item.
- [ubiquitousItemContainerDisplayName](urlresourcevalues/ubiquitousitemcontainerdisplayname.md) — The name of the item’s container as the system displays it to users.
- [ubiquitousItemDownloadRequested](urlresourcevalues/ubiquitousitemdownloadrequested.md) — A Boolean value that indicates whether the user or the system requests a download of the item.
- [ubiquitousItemDownloadingError](urlresourcevalues/ubiquitousitemdownloadingerror.md) — The error when downloading the item from iCloud fails.
- [ubiquitousItemDownloadingStatus](urlresourcevalues/ubiquitousitemdownloadingstatus.md) — The download status of the item.
- [ubiquitousItemHasUnresolvedConflicts](urlresourcevalues/ubiquitousitemhasunresolvedconflicts.md) — A Boolean value that indicates whether the item has outstanding conflicts.
- [ubiquitousItemIsDownloading](urlresourcevalues/ubiquitousitemisdownloading.md) — A Boolean value that indicates whether the system is downloading the item.
- [ubiquitousItemIsUploaded](urlresourcevalues/ubiquitousitemisuploaded.md) — A Boolean value that indicates whether data is present in the cloud for the item.
- [ubiquitousItemIsUploading](urlresourcevalues/ubiquitousitemisuploading.md) — A Boolean value that indicates whether the system is uploading the item.
- [ubiquitousItemUploadingError](urlresourcevalues/ubiquitousitemuploadingerror.md) — The error when uploading the item to iCloud fails.

### Thumbnail values

- [thumbnail](urlresourcevalues/thumbnail.md) — A thumbnail image of the URL. _(deprecated)_
- [thumbnailDictionary](urlresourcevalues/thumbnaildictionary-7jyzz.md) — A dictionary of UIKit image objects keyed by size. _(deprecated)_
- [thumbnailDictionary](urlresourcevalues/thumbnaildictionary-4ztst.md) — A dictionary of AppKit image objects keyed by size. _(deprecated)_

### Universal resource values

- [addedToDirectoryDate](urlresourcevalues/addedtodirectorydate.md) — The date the resource was created, or renamed into or within its parent directory.
- [allValues](urlresourcevalues/allvalues.md) — A loosely-typed dictionary containing all keys and values.
- [attributeModificationDate](urlresourcevalues/attributemodificationdate.md) — The time the resource’s attributes were last modified.
- [canonicalPath](urlresourcevalues/canonicalpath.md) — The URL’s path as a canonical absolute file system path.
- [contentAccessDate](urlresourcevalues/contentaccessdate.md) — The date the resource was last accessed.
- [contentModificationDate](urlresourcevalues/contentmodificationdate.md) — The time the resource content was last modified.
- [creationDate](urlresourcevalues/creationdate.md) — The date the resource was created.
- [customIcon](urlresourcevalues/customicon.md)
- [effectiveIcon](urlresourcevalues/effectiveicon.md)
- [generationIdentifier](urlresourcevalues/generationidentifier.md) — An opaque generation identifier which can be compared using `==` to determine if the data in a document has been modified.
- [hasHiddenExtension](urlresourcevalues/hashiddenextension.md) — True for resources whose filename extension is removed from the localized name property.
- [isAliasFile](urlresourcevalues/isaliasfile.md) — true if the resource is a Finder alias file or a symlink, false otherwise
- [isExcludedFromBackup](urlresourcevalues/isexcludedfrombackup.md) — True if resource should be excluded from backups, false otherwise.
- [isHidden](urlresourcevalues/ishidden.md) — True for resources normally not displayed to users.
- [isPackage](urlresourcevalues/ispackage.md) — True for packaged directories.
- [isReadable](urlresourcevalues/isreadable.md) — True if this process (as determined by EUID) can read the resource.
- [isSymbolicLink](urlresourcevalues/issymboliclink.md) — True for symlinks.
- [isSystemImmutable](urlresourcevalues/issystemimmutable.md) — True for system-immutable resources.
- [isUserImmutable](urlresourcevalues/isuserimmutable.md) — True for user-immutable resources
- [isWritable](urlresourcevalues/iswritable.md) — True if this process (as determined by EUID) can write to the resource.
- [labelColor](urlresourcevalues/labelcolor.md)
- [labelNumber](urlresourcevalues/labelnumber.md) — The label number assigned to the resource.
- [linkCount](urlresourcevalues/linkcount.md) — Number of hard links to the resource.
- [localizedLabel](urlresourcevalues/localizedlabel.md) — The user-visible label text.
- [localizedName](urlresourcevalues/localizedname.md) — Localized or extension-hidden name as displayed to users.
- [localizedTypeDescription](urlresourcevalues/localizedtypedescription.md) — User-visible type or “kind” description.
- [name](urlresourcevalues/name.md) — The resource name provided by the file system.
- [parentDirectory](urlresourcevalues/parentdirectory.md) — The resource’s parent directory, if any.
- [path](urlresourcevalues/path.md) — The URL’s path as a file system path.
- [preferredIOBlockSize](urlresourcevalues/preferredioblocksize.md) — The optimal block size when reading or writing this file’s data, or nil if not available.
- [quarantineProperties](urlresourcevalues/quarantineproperties.md) — The quarantine properties as defined in LSQuarantine.h. To remove quarantine information from a file, pass `nil` as the value when setting this property.
- [tagNames](urlresourcevalues/tagnames.md) — The array of Tag names.
- [typeIdentifier](urlresourcevalues/typeidentifier.md) — A string that represents the identifier for the type of the resource. _(deprecated)_
- [contentType](urlresourcevalues/contenttype.md) — The resource’s type.

### Initializers

- [init()](<urlresourcevalues/init().md>) — Initializes a new resource values structure.

### Instance Properties

- [ubiquitousItemIsSyncPaused](urlresourcevalues/ubiquitousitemissyncpaused.md) — True if the sync of the item has been paused.
- [ubiquitousItemSupportedSyncControls](urlresourcevalues/ubiquitousitemsupportedsynccontrols.md) — The supported sync controls on the item.

## See Also

### Accessing resource values

- [resourceValues(forKeys:)](<url/resourcevalues(forkeys_).md>) — Returns a collection of resource values identified by the given resource keys.
- [setResourceValues(_:)](<url/setresourcevalues(__).md>) — Sets the resource value identified by a given resource key.
- [removeCachedResourceValue(forKey:)](<url/removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given resource value key from the URL object.
- [removeAllCachedResourceValues()](<url/removeallcachedresourcevalues().md>) — Removes all cached resource values and all temporary resource values from the URL object.
- [setTemporaryResourceValue(_:forKey:)](<url/settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](urlresourcekey.md) — Keys that apply to file system URLs.
