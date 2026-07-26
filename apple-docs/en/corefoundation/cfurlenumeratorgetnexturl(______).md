---
title: 'CFURLEnumeratorGetNextURL(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlenumeratorgetnexturl(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlenumeratorgetnexturl(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlenumeratorgetnexturl%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:96e704611d79a1c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLEnumeratorGetNextURL(_:_:_:)

<sub>Function</sub>

Advances an enumerator to the next URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLEnumeratorGetNextURL(_ enumerator: CFURLEnumerator!, _ url: UnsafeMutablePointer<Unmanaged<CFURL>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFURLEnumeratorResult
```

## Parameters

- `enumerator` — The enumerator.

- `url` — Contains the next URL if this function returns [kCFURLEnumeratorSuccess](cfurlenumeratorresult/success.md).

- `error` — Contains error information if this function returns [kCFURLEnumeratorError](cfurlenumeratorresult/error.md). Error information is retained and must be released. Can be `NULL`.

## Return Value

The result of advancing the enumerator.

## Discussion

If this function returns [kCFURLEnumeratorEnd](cfurlenumeratorresult/end.md), the enumeration has finished.

A return value of [kCFURLEnumeratorError](cfurlenumeratorresult/error.md) does not imply that the enumeration has finished.

If this function returns [kCFURLEnumeratorError](cfurlenumeratorresult/error.md), the user info dictionary of `error` is populated with the following entries (when possible):

- The [kCFErrorUnderlyingErrorKey](kcferrorunderlyingerrorkey.md) entry is populated with the underlying error if the underlying error is not in the [kCFErrorDomainCocoa](kcferrordomaincocoa.md) domain.
- The [NSURLErrorKey](../foundation/nsurlerrorkey.md) entry is populated with the URL that caused the error, as a [CFURL](cfurl.md) object.
- The [NSFilePathErrorKey](../foundation/nsfilepatherrorkey.md) entry is populated with the file path that caused the error, as a [CFString](cfstring.md) object.

## See Also

### Related Documentation

- [CFURLEnumeratorResult](cfurlenumeratorresult.md) — Result codes from the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.

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
