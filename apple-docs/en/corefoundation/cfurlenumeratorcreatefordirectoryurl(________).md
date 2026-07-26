---
title: 'CFURLEnumeratorCreateForDirectoryURL(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlenumeratorcreatefordirectoryurl(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratorcreatefordirectoryurl(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratorcreatefordirectoryurl%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:56382af817e61d78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLEnumeratorCreateForDirectoryURL(_:_:_:_:)

<sub>Function</sub>

Creates and returns a directory enumerator with provided enumerator behavior options and properties to be prefetched.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLEnumeratorCreateForDirectoryURL(_ alloc: CFAllocator!, _ directoryURL: CFURL!, _ option: CFURLEnumeratorOptions, _ propertyKeys: CFArray!) -> CFURLEnumerator!
```

## Parameters

- `alloc` — The memory allocator to use. If `NULL`, the default allocator is used.

- `directoryURL` — The URL of the directory to enumerate.

- `option` — A bit array of enumerator behavior options.

- `propertyKeys` — An array of file property keys to prefetch for each enumerated URL. Can be `NULL`.

## Return Value

The created directory enumerator.

## Discussion

Directory enumerators do not descend into subdirectories of `directoryURL` by default. To create a recursive enumerator, include the [kCFURLEnumeratorDescendRecursively](cfurlenumeratoroptions/descendrecursively.md) option in `options`.

Specifying prefetch properties allows the enumerator to optimize device access by using bulk operations. However, you should not prefetch properties that are not needed, because doing so may degrade performance.

The created directory enumerator generates URLs with the same type as `directoryURL`. If `directoryURL` is a file reference URL, then enumerated URLs are file reference URLs. If `directoryURL` is a file path URL, then enumerated URLs are file path URLs.

In some areas of the file system hierarchy, file reference URLs cannot be generated. The enumerator always generates file path URLs for these areas.

This function ignores the [kCFURLEnumeratorGenerateFileReferenceURLs](cfurlenumeratoroptions/generatefilereferenceurls.md) option.

## See Also

### Related Documentation

- [CFURLEnumeratorOptions](cfurlenumeratoroptions.md) — Options for controlling enumerator behavior.

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
