---
title: 'CFBundleCopyInfoDictionaryInDirectory(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyinfodictionaryindirectory(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyinfodictionaryindirectory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyinfodictionaryindirectory%28_%3A%29.json'
content_hash: 'sha256:6dea385d5f30a102'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyInfoDictionaryInDirectory(_:)

<sub>Function</sub>

Returns a bundle’s information dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyInfoDictionaryInDirectory(_ bundleURL: CFURL!) -> CFDictionary!
```

## Parameters

- `bundleURL` — A CFURL object describing the location of a bundle.

## Return Value

A CFDictionary object containing the information dictionary for a bundle located at `bundleURL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function provides a means to obtain an information dictionary for a bundle without first creating a CFBundle object.

## See Also

### Getting Bundle Properties

- [CFBundleCopyBundleURL](<cfbundlecopybundleurl(__).md>) — Returns the location of a bundle.
- [CFBundleGetDevelopmentRegion](<cfbundlegetdevelopmentregion(__).md>) — Returns the bundle’s development region from the bundle’s information property list.
- [CFBundleGetIdentifier](<cfbundlegetidentifier(__).md>) — Returns the bundle identifier from a bundle’s information property list.
- [CFBundleGetInfoDictionary](<cfbundlegetinfodictionary(__).md>) — Returns a bundle’s information dictionary.
- [CFBundleGetLocalInfoDictionary](<cfbundlegetlocalinfodictionary(__).md>) — Returns a bundle’s localized information dictionary.
- [CFBundleGetValueForInfoDictionaryKey](<cfbundlegetvalueforinfodictionarykey(____).md>) — Returns a value (localized if possible) from a bundle’s information dictionary.
- [CFBundleCopyInfoDictionaryForURL](<cfbundlecopyinfodictionaryforurl(__).md>) — Returns the information dictionary for a given URL location.
- [CFBundleGetPackageInfo](<cfbundlegetpackageinfo(______).md>) — Returns a bundle’s package type and creator.
- [CFBundleGetPackageInfoInDirectory](<cfbundlegetpackageinfoindirectory(______).md>) — Returns a bundle’s package type and creator without having to create a CFBundle object.
- [CFBundleCopyExecutableArchitectures](<cfbundlecopyexecutablearchitectures(__).md>) — Returns an array of CFNumbers representing the architectures a given bundle provides.
- [CFBundleCopyExecutableArchitecturesForURL](<cfbundlecopyexecutablearchitecturesforurl(__).md>) — Returns an array of CFNumbers representing the architectures a given URL provides.
- [CFBundleGetVersionNumber](<cfbundlegetversionnumber(__).md>) — Returns a bundle’s version number.
