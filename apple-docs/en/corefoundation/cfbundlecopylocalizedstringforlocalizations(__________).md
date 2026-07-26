---
title: 'CFBundleCopyLocalizedStringForLocalizations(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopylocalizedstringforlocalizations(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizedstringforlocalizations(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopylocalizedstringforlocalizations%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0d50bfd860253af4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyLocalizedStringForLocalizations(_:_:_:_:_:)

<sub>Function</sub>

Returns a localized string from a bundle’s strings file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyLocalizedStringForLocalizations(_ bundle: CFBundle!, _ key: CFString!, _ value: CFString!, _ tableName: CFString!, _ localizations: CFArray!) -> CFString!
```

## Parameters

- `bundle` — The bundle to examine.

- `key` — The key for the localized string to retrieve. This key will be used to look up the localized string in the strings file. Typically the key is identical to the value of the localized string in the development language.

- `value` — A default value to return if no value exists for `key`.

- `tableName` — The name of the strings file to search. The name should not include the `strings` filename extension. The case of the string must match that of the file name, even on file systems (such as HFS+) that are not case sensitive with regards to file names

- `localizations` — An array of BCP 47 language codes corresponding to available localizations. Bundle compares the array against its available localizations, and uses the best result to retrieve the localized string. If empty, we treat it as no localization is available, and may return a fallback.

## Return Value

A CFString object that contains the localized string. If no value exists for `key`, returns `value` unless `value` is `NULL` or an empty string, in which case `key` is returned instead. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Returns a localized string given a list of possible localizations. The one most suitable to use with the given `bundle` is returned.

## See Also

### Functions

- [CFAllocatorAllocateBytes](<cfallocatorallocatebytes(______).md>)
- [CFAllocatorAllocateTyped](<cfallocatorallocatetyped(________).md>)
- [CFAllocatorReallocateBytes](<cfallocatorreallocatebytes(________).md>)
- [CFAllocatorReallocateTyped](<cfallocatorreallocatetyped(__________).md>)
- [CFAttributedStringGetBidiLevelsAndResolvedDirections](<cfattributedstringgetbidilevelsandresolveddirections(__________).md>)
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
