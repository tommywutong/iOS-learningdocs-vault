---
title: 'CFURLEnumeratorSkipDescendents(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlenumeratorskipdescendents(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratorskipdescendents(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratorskipdescendents%28_%3A%29.json'
content_hash: 'sha256:4683be78e20866a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLEnumeratorSkipDescendents(_:)

<sub>Function</sub>

Tells a recursive enumerator not to descend into the directory at the URL that was returned by the most recent call to the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLEnumeratorSkipDescendents(_ enumerator: CFURLEnumerator!)
```

## Parameters

- `enumerator` — The enumerator.

## Discussion

A call to this function is ignored in the following cases:

- The [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function has never been called with this enumerator.
- The last URL returned by the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function is not a directory.
- The enumerator is not a directory enumerator that was created with the [kCFURLEnumeratorDescendRecursively](cfurlenumeratoroptions/descendrecursively.md) option.

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
