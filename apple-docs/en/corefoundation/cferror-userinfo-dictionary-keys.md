---
title: CFError userInfo Dictionary Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cferror-userinfo-dictionary-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/cferror-userinfo-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferror-userinfo-dictionary-keys.json'
content_hash: 'sha256:2c97d6a66773a386'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFURL](cfurl.md)

# CFError userInfo Dictionary Keys

<sub>API Collection</sub>

Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.

## Topics

### Constants

- [kCFURLKeysOfUnsetValuesKey](kcfurlkeysofunsetvalueskey.md) — Key for the resource properties that have not been set after the [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) function returns an error, returned as an array of `CFString` objects.

## See Also

### File System Constants

- [Common File System Resource Keys](common-file-system-resource-keys.md) — Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md) — Possible values for the [kCFURLFileResourceTypeKey](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md) — Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md) — These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md) — Keys that apply to volumes.
