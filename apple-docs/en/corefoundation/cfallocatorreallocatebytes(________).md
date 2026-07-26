---
title: 'CFAllocatorReallocateBytes(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfallocatorreallocatebytes(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorreallocatebytes(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorreallocatebytes%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fcc5abe9284b3d2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorReallocateBytes(_:_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAllocatorReallocateBytes(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!, _ newsize: CFIndex, _ hint: CFOptionFlags) -> UnsafeMutableRawPointer!
```

## See Also

### Functions

- [CFAllocatorAllocateBytes](<cfallocatorallocatebytes(______).md>)
- [CFAllocatorAllocateTyped](<cfallocatorallocatetyped(________).md>)
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
- [CFFileSecurityCreate](<cffilesecuritycreate(__).md>) — Creates a `CFFileSecurityRef` object.
