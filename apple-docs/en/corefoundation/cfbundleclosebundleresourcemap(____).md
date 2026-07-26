---
title: 'CFBundleCloseBundleResourceMap(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfbundleclosebundleresourcemap(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleclosebundleresourcemap(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleclosebundleresourcemap%28_%3A_%3A%29.json'
content_hash: 'sha256:42e37c21f9797078'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCloseBundleResourceMap(_:_:)

<sub>Function</sub>

Closes an open resource map for a bundle.

> [!warning] Deprecated
> The Carbon Resource Manager is deprecated. This should only be used to access Resource Manager-style resources in old bundles.

<sub>macOS</sub>

```swift
func CFBundleCloseBundleResourceMap(_ bundle: CFBundle!, _ refNum: CFBundleRefNum)
```

## Parameters

- `bundle` — The bundle whose resource map is referenced by `refNum`.

- `refNum` — The reference number for a resource map to close.

## Discussion

You open a resource map using either [CFBundleOpenBundleResourceFiles](<cfbundleopenbundleresourcefiles(______).md>) or [CFBundleOpenBundleResourceMap](<cfbundleopenbundleresourcemap(__).md>).

## See Also

### Locating Bundle Resources

- [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) — Returns the location of a resource contained in the specified bundle.
- [CFBundleCopyResourceURLInDirectory](<cfbundlecopyresourceurlindirectory(________).md>) — Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) — Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [CFBundleCopyResourceURLsOfTypeInDirectory](<cfbundlecopyresourceurlsoftypeindirectory(______).md>) — Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [CFBundleCopyResourceURLForLocalization](<cfbundlecopyresourceurlforlocalization(__________).md>) — Returns the location of a localized resource in a bundle.
- [CFBundleCopyResourceURLsOfTypeForLocalization](<cfbundlecopyresourceurlsoftypeforlocalization(________).md>) — Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [CFBundleOpenBundleResourceFiles](<cfbundleopenbundleresourcefiles(______).md>) — Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps. _(deprecated)_
- [CFBundleOpenBundleResourceMap](<cfbundleopenbundleresourcemap(__).md>) — Opens the non-localized and localized resource files (if any) for a bundle in a single resource map. _(deprecated)_
