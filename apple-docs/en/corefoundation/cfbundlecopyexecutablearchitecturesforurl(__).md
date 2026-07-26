---
title: 'CFBundleCopyExecutableArchitecturesForURL(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyexecutablearchitecturesforurl(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyexecutablearchitecturesforurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyexecutablearchitecturesforurl%28_%3A%29.json'
content_hash: 'sha256:10419deef06f4127'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyExecutableArchitecturesForURL(_:)

<sub>Function</sub>

Returns an array of CFNumbers representing the architectures a given URL provides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyExecutableArchitecturesForURL(_ url: CFURL!) -> CFArray!
```

## Parameters

- `url` — The URL to examine.

## Return Value

For a directory URL, if the bundle’s executable exists and is a Mach-O file, returns an array of CFNumbers whose values are integers representing the architectures the URL provides. For a plain file URL representing an unbundled executable, returns the architectures it provides if it is a Mach-O file. Possible values are listed in [Architecture Types](1537096-architecture-types.md). If there is no bundle executable or if the executable is not a Mach-O file, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

For a directory URL, this is equivalent to calling [CFBundleCopyExecutableArchitectures](<cfbundlecopyexecutablearchitectures(__).md>) on the corresponding bundle.

## See Also

### Getting Bundle Properties

- [CFBundleCopyBundleURL](<cfbundlecopybundleurl(__).md>) — Returns the location of a bundle.
- [CFBundleGetDevelopmentRegion](<cfbundlegetdevelopmentregion(__).md>) — Returns the bundle’s development region from the bundle’s information property list.
- [CFBundleGetIdentifier](<cfbundlegetidentifier(__).md>) — Returns the bundle identifier from a bundle’s information property list.
- [CFBundleGetInfoDictionary](<cfbundlegetinfodictionary(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleGetLocalInfoDictionary](<cfbundlegetlocalinfodictionary(__).md>) — Returns a bundle’s localized information dictionary.
- [CFBundleGetValueForInfoDictionaryKey](<cfbundlegetvalueforinfodictionarykey(____).md>) — Returns a value (localized if possible) from a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryInDirectory](<cfbundlecopyinfodictionaryindirectory(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryForURL](<cfbundlecopyinfodictionaryforurl(__).md>) — Returns the information dictionary for a given URL location.
- [CFBundleGetPackageInfo](<cfbundlegetpackageinfo(______).md>) — Returns a bundle’s package type and creator.
- [CFBundleGetPackageInfoInDirectory](<cfbundlegetpackageinfoindirectory(______).md>) — Returns a bundle’s package type and creator without having to create a CFBundle object.
- [CFBundleCopyExecutableArchitectures](<cfbundlecopyexecutablearchitectures(__).md>) — Returns an array of CFNumbers representing the architectures a given bundle provides.
- [CFBundleGetVersionNumber](<cfbundlegetversionnumber(__).md>) — Returns a bundle’s version number.
