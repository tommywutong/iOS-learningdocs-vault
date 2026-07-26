---
title: 'CFBundleCopyAuxiliaryExecutableURL(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyauxiliaryexecutableurl(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyauxiliaryexecutableurl(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyauxiliaryexecutableurl%28_%3A_%3A%29.json'
content_hash: 'sha256:79a604e2452d1e99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyAuxiliaryExecutableURL(_:_:)

<sub>Function</sub>

Returns the location of a bundle’s auxiliary executable code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyAuxiliaryExecutableURL(_ bundle: CFBundle!, _ executableName: CFString!) -> CFURL!
```

## Parameters

- `bundle` — The bundle to examine.

- `executableName` — The name of `bundle`’s auxiliary executable code.

## Return Value

The URL location of the specified bundle’s auxiliary executable code, or `NULL` if it could not be found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function can be used to find executables other than your main executable. This is useful, for instance, for applications that have some command line tool that is packaged with and used by the application. The tool can be packaged in the various platform executable directories in the bundle and can be located with this function. This allows an application to ship versions of the tool for each platform as it does for the main application executable.

## See Also

### Finding Locations in a Bundle

- [CFBundleCopyBuiltInPlugInsURL](<cfbundlecopybuiltinpluginsurl(__).md>) — Returns the location of a bundle’s built in plug-in.
- [CFBundleCopyExecutableURL](<cfbundlecopyexecutableurl(__).md>) — Returns the location of a bundle’s main executable code.
- [CFBundleCopyPrivateFrameworksURL](<cfbundlecopyprivateframeworksurl(__).md>) — Returns the location of a bundle’s private Frameworks directory.
- [CFBundleCopyResourcesDirectoryURL](<cfbundlecopyresourcesdirectoryurl(__).md>) — Returns the location of a bundle’s Resources directory.
- [CFBundleCopySharedFrameworksURL](<cfbundlecopysharedframeworksurl(__).md>) — Returns the location of a bundle’s shared frameworks directory.
- [CFBundleCopySharedSupportURL](<cfbundlecopysharedsupporturl(__).md>) — Returns the location of a bundle’s shared support files directory.
- [CFBundleCopySupportFilesDirectoryURL](<cfbundlecopysupportfilesdirectoryurl(__).md>) — Returns the location of the bundle’s support files directory.
