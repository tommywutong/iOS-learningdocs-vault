---
title: File Property Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/file-property-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/file-property-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/file-property-keys.json'
content_hash: 'sha256:ef5f61eebb543e28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# File Property Keys

<sub>API Collection</sub>

Keys that apply to properties of files.

## Topics

### Constants

- [kCFURLFileAllocatedSizeKey](kcfurlfileallocatedsizekey.md) — Key for the total size allocated on disk for the file, returned as an `CFNumber` object.
- [kCFURLFileSizeKey](kcfurlfilesizekey.md) — Key for the file’s size in bytes, returned as a `CFNumber` object.
- [kCFURLIsAliasFileKey](kcfurlisaliasfilekey.md) — Key for determining whether the file is an alias, returned as a `CFBoolean` object.
- [kCFURLIsMountTriggerKey](kcfurlismounttriggerkey.md) — Key for determining whether the URL is a file system trigger directory, returned as a `CFBoolean` object. Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [kCFURLTotalFileAllocatedSizeKey](kcfurltotalfileallocatedsizekey.md) — Key for the total allocated size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.
- [kCFURLTotalFileSizeKey](kcfurltotalfilesizekey.md) — Key for the total displayable size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.

## See Also

### File System Constants

- [Common File System Resource Keys](common-file-system-resource-keys.md) — Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md) — Possible values for the [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) key.
- [iCloud Constants](icloud-constants.md) — These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md) — Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md) — Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.
