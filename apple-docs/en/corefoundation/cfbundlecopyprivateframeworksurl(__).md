---
title: 'CFBundleCopyPrivateFrameworksURL(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyprivateframeworksurl(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyprivateframeworksurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyprivateframeworksurl%28_%3A%29.json'
content_hash: 'sha256:85a5ac96c4a4b760'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyPrivateFrameworksURL(_:)

<sub>Function</sub>

Returns the location of a bundle’s private Frameworks directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyPrivateFrameworksURL(_ bundle: CFBundle!) -> CFURL!
```

## Parameters

- `bundle` — The bundle to examine.

## Return Value

A CFURL object describing the location of `bundle`’s private frameworks directory, or `NULL` if it could not be found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Finding Locations in a Bundle

- [CFBundleCopyAuxiliaryExecutableURL](<cfbundlecopyauxiliaryexecutableurl(____).md>) — Returns the location of a bundle’s auxiliary executable code.
- [CFBundleCopyBuiltInPlugInsURL](<cfbundlecopybuiltinpluginsurl(__).md>) — Returns the location of a bundle’s built in plug-in.
- [CFBundleCopyExecutableURL](<cfbundlecopyexecutableurl(__).md>) — Returns the location of a bundle’s main executable code.
- [CFBundleCopyResourcesDirectoryURL](<cfbundlecopyresourcesdirectoryurl(__).md>) — Returns the location of a bundle’s Resources directory.
- [CFBundleCopySharedFrameworksURL](<cfbundlecopysharedframeworksurl(__).md>) — Returns the location of a bundle’s shared frameworks directory.
- [CFBundleCopySharedSupportURL](<cfbundlecopysharedsupporturl(__).md>) — Returns the location of a bundle’s shared support files directory.
- [CFBundleCopySupportFilesDirectoryURL](<cfbundlecopysupportfilesdirectoryurl(__).md>) — Returns the location of the bundle’s support files directory.
