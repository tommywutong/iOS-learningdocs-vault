---
title: 'CFBundleGetVersionNumber(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetversionnumber(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetversionnumber(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetversionnumber%28_%3A%29.json'
content_hash: 'sha256:1a79d17777beaa01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetVersionNumber(_:)

<sub>Function</sub>

Returns a bundle’s version number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetVersionNumber(_ bundle: CFBundle!) -> UInt32
```

## Parameters

- `bundle` — The bundle to examine. The bundle’s version number can be number or a string of the standard form “2.5.3d5”.

## Return Value

A `vers` resource style version number. If it is a string, it is automatically converted to the numeric representation, where the major version number is restricted to 2 BCD digits (in other words, it must be in the range 0-99) and the minor and bug fix version numbers are each restricted to a single BCD digit (0-9).

## Discussion

This function is only supported for the `vers` resource style version numbers. Where other version number styles—namely X, or X.Y, or X.Y.Z—are used, you can use [CFBundleGetValueForInfoDictionaryKey](<cfbundlegetvalueforinfodictionarykey(____).md>) with the key `kCFBundleVersionKey` to extract the version number as a string from the bundle’s information dictionary.

Some version numbers of the form X, X.Y, and X.Y.Z may work with this function, if X \<= 99, Y \<= 9, and Z \<= 9. Thus a version number 76.5.4 will work, but 76.12 will not work.

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
- [CFBundleCopyExecutableArchitecturesForURL](<cfbundlecopyexecutablearchitecturesforurl(__).md>) — Returns an array of CFNumbers representing the architectures a given URL provides.
