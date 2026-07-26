---
title: 'CFFileSecuritySetAccessControlList(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffilesecuritysetaccesscontrollist(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffilesecuritysetaccesscontrollist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffilesecuritysetaccesscontrollist%28_%3A_%3A%29.json'
content_hash: 'sha256:8d0fd79a3cef8afd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileSecuritySetAccessControlList(_:_:)

<sub>Function</sub>

Sets the access control list associated with a `CFFileSecurityRef` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileSecuritySetAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: acl_t!) -> Bool
```

## Parameters

- `fileSec` — The `CFFileSecurityRef` object to modify.

- `accessControlList` — The access control list to set, or `kCFFileSecurityRemoveACL` to indicate that the access control list should be removed from a file, or `NULL` to unset the access control list property in the object.

## Return Value

Returns `true` if the access control list was successfully set, or `false` otherwise.

## Discussion

To remove the access control list from a file system object, pass `kCFFileSecurityRemoveACL` as the `accessControlList` parameter. Then, call [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) to set [kCFURLFileSecurityKey](kcfurlfilesecuritykey.md) to the resulting `fileSec` object.

Setting the `accessControlList` to `NULL` unsets the ACL property of the `CFFileSecurityRef` object. By doing this, the access control list of the file will be unchanged if you subsequently use this object to set permissions on an actual file system object.

## See Also

### Functions

- [CFAllocatorAllocateBytes](<cfallocatorallocatebytes(______).md>)
- [CFAllocatorAllocateTyped](<cfallocatorallocatetyped(________).md>)
- [CFAllocatorReallocateBytes](<cfallocatorreallocatebytes(________).md>)
- [CFAllocatorReallocateTyped](<cfallocatorreallocatetyped(__________).md>)
- [CFAttributedStringGetBidiLevelsAndResolvedDirections](<cfattributedstringgetbidilevelsandresolveddirections(__________).md>)
- [CFBundleCopyLocalizedStringForLocalizations](<cfbundlecopylocalizedstringforlocalizations(__________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleIsArchitectureLoadable](<cfbundleisarchitectureloadable(__).md>)
- [CFBundleIsExecutableLoadable](<cfbundleisexecutableloadable(__).md>)
- [CFBundleIsExecutableLoadableForURL](<cfbundleisexecutableloadableforurl(__).md>)
- [CFCopyHomeDirectoryURL](<cfcopyhomedirectoryurl().md>)
- [CFDateFormatterCreateISO8601Formatter](<cfdateformattercreateiso8601formatter(____).md>)
- [CFFileSecurityClearProperties](<cffilesecurityclearproperties(____).md>) — Clears properties from a `CFFileSecurityRef` object.
- [CFFileSecurityCopyAccessControlList](<cffilesecuritycopyaccesscontrollist(____).md>) — Copies the access control list associated with a `CFFileSecurityRef` object.
- [CFFileSecurityCopyGroupUUID](<cffilesecuritycopygroupuuid(____).md>) — Copies the group UUID associated with a `CFFileSecurityRef` object.
- [CFFileSecurityCopyOwnerUUID](<cffilesecuritycopyowneruuid(____).md>) — Copies the owner UUID associated with a `CFFileSecurityRef` object.
