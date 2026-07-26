---
title: 'CFBundleCopySupportFilesDirectoryURL(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopysupportfilesdirectoryurl(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopysupportfilesdirectoryurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopysupportfilesdirectoryurl%28_%3A%29.json'
content_hash: 'sha256:3c47be1d1a1ae367'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopySupportFilesDirectoryURL(_:)

<sub>Function</sub>

Returns the location of the bundle’s support files directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopySupportFilesDirectoryURL(_ bundle: CFBundle!) -> CFURL!
```

## Parameters

- `bundle` — The CFBundle object whose support files directory you want to locate.

## Return Value

A CFURL object describing the location of the bundle’s support files directory, or `NULL` if it could not be found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

In general, you should never need to use this function. Use [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) and similar functions instead.

## See Also

### Finding Locations in a Bundle

- [CFBundleCopyAuxiliaryExecutableURL](<cfbundlecopyauxiliaryexecutableurl(____).md>) — Returns the location of a bundle’s auxiliary executable code.
- [CFBundleCopyBuiltInPlugInsURL](<cfbundlecopybuiltinpluginsurl(__).md>) — Returns the location of a bundle’s built in plug-in.
- [CFBundleCopyExecutableURL](<cfbundlecopyexecutableurl(__).md>) — Returns the location of a bundle’s main executable code.
- [CFBundleCopyPrivateFrameworksURL](<cfbundlecopyprivateframeworksurl(__).md>) — Returns the location of a bundle’s private Frameworks directory.
- [CFBundleCopyResourcesDirectoryURL](<cfbundlecopyresourcesdirectoryurl(__).md>) — Returns the location of a bundle’s Resources directory.
- [CFBundleCopySharedFrameworksURL](<cfbundlecopysharedframeworksurl(__).md>) — Returns the location of a bundle’s shared frameworks directory.
- [CFBundleCopySharedSupportURL](<cfbundlecopysharedsupporturl(__).md>) — Returns the location of a bundle’s shared support files directory.
