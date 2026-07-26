---
title: iCloud Constants
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/icloud-constants
source_url: 'https://developer.apple.com/documentation/corefoundation/icloud-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/icloud-constants.json'
content_hash: 'sha256:c4ca488c8f0ce6fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# iCloud Constants

<sub>API Collection</sub>

These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.

## Topics

### Constants

- [kCFURLIsUbiquitousItemKey](kcfurlisubiquitousitemkey.md) — A `CFBoolean` value that tells whether the item is synced to the cloud. (read-only)
- [kCFURLUbiquitousItemHasUnresolvedConflictsKey](kcfurlubiquitousitemhasunresolvedconflictskey.md) — A `CFBoolean` value that tells whether the item has conflicts outstanding. (read-only)
- [kCFURLUbiquitousItemIsDownloadedKey](kcfurlubiquitousitemisdownloadedkey.md) — A `CFBoolean` value that tells whether there is local data present for the item. (read-only) _(deprecated)_
- [kCFURLUbiquitousItemIsDownloadingKey](kcfurlubiquitousitemisdownloadingkey.md) — A `CFBoolean` value that tells whether data for the item is being downloaded. (read-only)
- [kCFURLUbiquitousItemIsUploadedKey](kcfurlubiquitousitemisuploadedkey.md) — A `CFBoolean` value that tells whether there is data present in the cloud for this item. (read-only)
- [kCFURLUbiquitousItemIsUploadingKey](kcfurlubiquitousitemisuploadingkey.md) — A `CFBoolean` value that tells whether data for the item is being uploaded. (read-only)
- [kCFURLUbiquitousItemPercentDownloadedKey](kcfurlubiquitousitempercentdownloadedkey.md) _(deprecated)_
- [kCFURLUbiquitousItemPercentUploadedKey](kcfurlubiquitousitempercentuploadedkey.md) _(deprecated)_

## See Also

### File System Constants

- [Common File System Resource Keys](common-file-system-resource-keys.md) — Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md) — Possible values for the [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md) — Keys that apply to properties of files.
- [Volume Property Keys](volume-property-keys.md) — Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md) — Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.
