---
title: 'CFBundleCopyInfoDictionaryForURL(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyinfodictionaryforurl(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyinfodictionaryforurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyinfodictionaryforurl%28_%3A%29.json'
content_hash: 'sha256:d2bf459833c77d93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyInfoDictionaryForURL(_:)

<sub>Function</sub>

Returns the information dictionary for a given URL location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyInfoDictionaryForURL(_ url: CFURL!) -> CFDictionary!
```

## Parameters

- `url` — A CFURL object describing the location of a file.

## Return Value

A CFDictionary object containing `url`’s information dictionary. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

For a directory URL, this is equivalent to [CFBundleCopyInfoDictionaryInDirectory](<cfbundlecopyinfodictionaryindirectory(__).md>). For a plain file URL representing an unbundled application, this function will attempt to read an information dictionary either from the `(__TEXT, __info_plist)` section of the file (for a Mach-O file) or from a `plst` resource.

## See Also

### Getting Bundle Properties

- [CFBundleCopyBundleURL](<cfbundlecopybundleurl(__).md>) — Returns the location of a bundle.
- [CFBundleGetDevelopmentRegion](<cfbundlegetdevelopmentregion(__).md>) — Returns the bundle’s development region from the bundle’s information property list.
- [CFBundleGetIdentifier](<cfbundlegetidentifier(__).md>) — Returns the bundle identifier from a bundle’s information property list.
- [CFBundleGetInfoDictionary](<cfbundlegetinfodictionary(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleGetLocalInfoDictionary](<cfbundlegetlocalinfodictionary(__).md>) — Returns a bundle’s localized information dictionary.
- [CFBundleGetValueForInfoDictionaryKey](<cfbundlegetvalueforinfodictionarykey(____).md>) — Returns a value (localized if possible) from a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryInDirectory](<cfbundlecopyinfodictionaryindirectory(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleGetPackageInfo](<cfbundlegetpackageinfo(______).md>) — Returns a bundle’s package type and creator.
- [CFBundleGetPackageInfoInDirectory](<cfbundlegetpackageinfoindirectory(______).md>) — Returns a bundle’s package type and creator without having to create a CFBundle object.
- [CFBundleCopyExecutableArchitectures](<cfbundlecopyexecutablearchitectures(__).md>) — Returns an array of CFNumbers representing the architectures a given bundle provides.
- [CFBundleCopyExecutableArchitecturesForURL](<cfbundlecopyexecutablearchitecturesforurl(__).md>) — Returns an array of CFNumbers representing the architectures a given URL provides.
- [CFBundleGetVersionNumber](<cfbundlegetversionnumber(__).md>) — Returns a bundle’s version number.
