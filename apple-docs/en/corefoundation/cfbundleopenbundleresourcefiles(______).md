---
title: 'CFBundleOpenBundleResourceFiles(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfbundleopenbundleresourcefiles(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleopenbundleresourcefiles(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleopenbundleresourcefiles%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dad7fc18e79149da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleOpenBundleResourceFiles(_:_:_:)

<sub>Function</sub>

Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.

> [!warning] Deprecated
> The Carbon Resource Manager is deprecated. This should only be used to access Resource Manager-style resources in old bundles.

<sub>macOS</sub>

```swift
func CFBundleOpenBundleResourceFiles(_ bundle: CFBundle!, _ refNum: UnsafeMutablePointer<CFBundleRefNum>!, _ localizedRefNum: UnsafeMutablePointer<CFBundleRefNum>!) -> Int32
```

## Parameters

- `bundle` — The bundle whose resource map you want to open.

- `refNum` — On return, the reference number of the non-localized resource map.

- `localizedRefNum` — On return, the reference number of the localized resource map.

## Return Value

An error code. The function returns `0` (`noErr`) if successful. If the bundle contains more than one resource file, the function returns an error code only if none was opened. The most common error is `resFNotFound`, but the function may also pass through other errors returned from the Resource Manager.

## See Also

### Locating Bundle Resources

- [CFBundleCloseBundleResourceMap](<cfbundleclosebundleresourcemap(____).md>) — Closes an open resource map for a bundle. _(deprecated)_
- [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) — Returns the location of a resource contained in the specified bundle.
- [CFBundleCopyResourceURLInDirectory](<cfbundlecopyresourceurlindirectory(________).md>) — Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) — Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [CFBundleCopyResourceURLsOfTypeInDirectory](<cfbundlecopyresourceurlsoftypeindirectory(______).md>) — Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [CFBundleCopyResourceURLForLocalization](<cfbundlecopyresourceurlforlocalization(__________).md>) — Returns the location of a localized resource in a bundle.
- [CFBundleCopyResourceURLsOfTypeForLocalization](<cfbundlecopyresourceurlsoftypeforlocalization(________).md>) — Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [CFBundleOpenBundleResourceMap](<cfbundleopenbundleresourcemap(__).md>) — Opens the non-localized and localized resource files (if any) for a bundle in a single resource map. _(deprecated)_
