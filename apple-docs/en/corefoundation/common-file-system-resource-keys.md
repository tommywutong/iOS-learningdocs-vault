---
title: Common File System Resource Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/common-file-system-resource-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/common-file-system-resource-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/common-file-system-resource-keys.json'
content_hash: 'sha256:fc6a1ac1aa2a424c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# Common File System Resource Keys

<sub>API Collection</sub>

Keys that are applicable to file system URLs.

## Topics

### Constants

- [kCFURLNameKey](kcfurlnamekey.md) — Key for the resource’s name in the file system, returned as a `CFString` object.
- [kCFURLLocalizedNameKey](kcfurllocalizednamekey.md) — Key for the resource’s localized or extension-hidden name, retuned as a `CFString` object.
- [kCFURLPathKey](kcfurlpathkey.md) — A `CFString` value containing the URL’s path as a file system path. (read-only)
- [kCFURLIsRegularFileKey](kcfurlisregularfilekey.md) — Key for determining whether the resource is a regular file, as opposed to a directory or a symbolic link. Returned as a `CFBoolean` object.
- [kCFURLIsDirectoryKey](kcfurlisdirectorykey.md) — Key for determining whether the resource is a directory, returned as a `CFBoolean` object.
- [kCFURLIsSymbolicLinkKey](kcfurlissymboliclinkkey.md) — Key for determining whether the resource is a symbolic link, returned as a `CFBoolean` object.
- [kCFURLIsVolumeKey](kcfurlisvolumekey.md) — Key for determining whether the resource is the root directory of a volume, returned as a `CFBoolean` object.
- [kCFURLIsPackageKey](kcfurlispackagekey.md) — Key for determining whether the resource is a packaged directory, returned as a `CFBoolean` object.
- [kCFURLIsSystemImmutableKey](kcfurlissystemimmutablekey.md) — Key for determining whether the resource’s system immutable bit is set, returned as a `CFBoolean` object.
- [kCFURLIsUserImmutableKey](kcfurlisuserimmutablekey.md) — Key for determining whether the resource’s user immutable bit is set, returned as a `CFBoolean` object.
- [kCFURLIsHiddenKey](kcfurlishiddenkey.md) — Key for determining whether the resource is normally not displayed to users, returned as a `CFBoolean` object.
- [kCFURLHasHiddenExtensionKey](kcfurlhashiddenextensionkey.md) — Key for determining whether the resource’s extension is normally removed from its localized name, returned as a `CFBoolean` object.
- [kCFURLCreationDateKey](kcfurlcreationdatekey.md) — Key for the resource’s creation date, returned as a `CFDate` object if the volume supports creation dates, or `nil` if creation dates are unsupported.
- [kCFURLContentAccessDateKey](kcfurlcontentaccessdatekey.md) — Key for the last time the resource was accessed, returned as a `CFDate` object if the volume supports access dates, or `nil` if access dates are unsupported.
- [kCFURLContentModificationDateKey](kcfurlcontentmodificationdatekey.md) — Key for the last time the resource was modified, returned as a `CFDate` object if the volume supports modification dates, or `nil` if modification dates are unsupported.
- [kCFURLAttributeModificationDateKey](kcfurlattributemodificationdatekey.md) — Key for the last time the resource’s attributes were modified, returned as a `CFDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported.
- [kCFURLLinkCountKey](kcfurllinkcountkey.md) — Key for the number of hard links to the resource, returned as a `CFNumber` object.
- [kCFURLParentDirectoryURLKey](kcfurlparentdirectoryurlkey.md) — Key for the parent directory of the resource, returned as a `CFURL` object, or `nil` if the resource is the root directory of its volume.
- [kCFURLVolumeURLKey](kcfurlvolumeurlkey.md) — Key for the root directory of the resource’s volume, returned as a `CFURL` object.
- [kCFURLTypeIdentifierKey](kcfurltypeidentifierkey.md) — Key for the resource’s uniform type identifier (UTI), returned as a `CFString` object. _(deprecated)_
- [kCFURLLocalizedTypeDescriptionKey](kcfurllocalizedtypedescriptionkey.md) — Key for the resource’s localized type description, returned as a `CFString` object.
- [kCFURLLabelNumberKey](kcfurllabelnumberkey.md) — Key for the resource’s label number, returned as a `CFNumber` object.
- [kCFURLLabelColorKey](kcfurllabelcolorkey.md) — Key for the resource’s label color, returned as a `CFColorRef` object, or `NULL` if the resource has no label color. _(deprecated)_
- [kCFURLLocalizedLabelKey](kcfurllocalizedlabelkey.md) — Key for the resource’s localized label text, returned as a `CFString` object, or `NULL` if the resource has no localized label text.
- [kCFURLEffectiveIconKey](kcfurleffectiveiconkey.md) — Key for the resource’s typical icon, returned as a `CGImageRef` object. _(deprecated)_
- [kCFURLCustomIconKey](kcfurlcustomiconkey.md) — Key for the icon stored with the resource, returned as a `CGImageRef` object, or `NULL` if the resource has no custom icon. _(deprecated)_
- [kCFURLFileResourceIdentifierKey](kcfurlfileresourceidentifierkey.md) — Key for the resource’s unique identifier, returned as a `CFType` object.
- [kCFURLVolumeIdentifierKey](kcfurlvolumeidentifierkey.md) — Key for the unique identifier of the resource’s volume, returned as a `CFType` object.
- [kCFURLPreferredIOBlockSizeKey](kcfurlpreferredioblocksizekey.md) — Key for the optimal block size to use when reading or writing this file’s data, returned as a `CFNumber` object, or `NULL` if the preferred size is not available.
- [kCFURLIsReadableKey](kcfurlisreadablekey.md) — Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a `CFBoolean` object.
- [kCFURLIsWritableKey](kcfurliswritablekey.md) — Key for determining whether the current process (as determined by the EUID) can write to the resource, returned as a `CFBoolean` object.
- [kCFURLIsExecutableKey](kcfurlisexecutablekey.md) — Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a `CFBoolean` object.
- [kCFURLFileSecurityKey](kcfurlfilesecuritykey.md) — Key for the resource’s security information, returned as a `CFFileSecurity` object.
- [kCFURLIsExcludedFromBackupKey](kcfurlisexcludedfrombackupkey.md)
- [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) — Key for the resource’s object type, returned as a `CFString` object.

## See Also

### File System Constants

- [File Resource Types](file-resource-types.md) — Possible values for the [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md) — Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md) — These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md) — Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md) — Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.
