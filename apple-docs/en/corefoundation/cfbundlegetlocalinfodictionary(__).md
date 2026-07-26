---
title: 'CFBundleGetLocalInfoDictionary(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetlocalinfodictionary(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetlocalinfodictionary(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetlocalinfodictionary%28_%3A%29.json'
content_hash: 'sha256:909538041c1d877c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetLocalInfoDictionary(_:)

<sub>Function</sub>

Returns a bundle’s localized information dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetLocalInfoDictionary(_ bundle: CFBundle!) -> CFDictionary!
```

## Parameters

- `bundle` — The bundle to examine.

## Return Value

A dictionary containing the key-value pairs in `bundle`’s localized information dictionary (from the `InfoPlist.strings` file for the current locale). Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting Bundle Properties

- [CFBundleCopyBundleURL](<cfbundlecopybundleurl(__).md>) — Returns the location of a bundle.
- [CFBundleGetDevelopmentRegion](<cfbundlegetdevelopmentregion(__).md>) — Returns the bundle’s development region from the bundle’s information property list.
- [CFBundleGetIdentifier](<cfbundlegetidentifier(__).md>) — Returns the bundle identifier from a bundle’s information property list.
- [CFBundleGetInfoDictionary](<cfbundlegetinfodictionary(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleGetValueForInfoDictionaryKey](<cfbundlegetvalueforinfodictionarykey(____).md>) — Returns a value (localized if possible) from a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryInDirectory](<cfbundlecopyinfodictionaryindirectory(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryForURL](<cfbundlecopyinfodictionaryforurl(__).md>) — Returns the information dictionary for a given URL location.
- [CFBundleGetPackageInfo](<cfbundlegetpackageinfo(______).md>) — Returns a bundle’s package type and creator.
- [CFBundleGetPackageInfoInDirectory](<cfbundlegetpackageinfoindirectory(______).md>) — Returns a bundle’s package type and creator without having to create a CFBundle object.
- [CFBundleCopyExecutableArchitectures](<cfbundlecopyexecutablearchitectures(__).md>) — Returns an array of CFNumbers representing the architectures a given bundle provides.
- [CFBundleCopyExecutableArchitecturesForURL](<cfbundlecopyexecutablearchitecturesforurl(__).md>) — Returns an array of CFNumbers representing the architectures a given URL provides.
- [CFBundleGetVersionNumber](<cfbundlegetversionnumber(__).md>) — Returns a bundle’s version number.
