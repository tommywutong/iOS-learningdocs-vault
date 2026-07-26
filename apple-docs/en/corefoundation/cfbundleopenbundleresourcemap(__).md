---
title: 'CFBundleOpenBundleResourceMap(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfbundleopenbundleresourcemap(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleopenbundleresourcemap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleopenbundleresourcemap%28_%3A%29.json'
content_hash: 'sha256:78946ea1f904ebc7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleOpenBundleResourceMap(_:)

<sub>Function</sub>

Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.

> [!warning] Deprecated
> The Carbon Resource Manager is deprecated. This should only be used to access Resource Manager-style resources in old bundles.

<sub>macOS</sub>

```swift
func CFBundleOpenBundleResourceMap(_ bundle: CFBundle!) -> CFBundleRefNum
```

## Parameters

- `bundle` — The bundle whose resource map you want to open.

## Return Value

A distinct reference number for the resource map.

## Discussion

Creates and makes current a single read-only resource map containing the non-localized and localized resource files. If this function is called multiple times, it opens the files multiple times and returns distinct reference numbers for each. Use [CFBundleCloseBundleResourceMap](<cfbundleclosebundleresourcemap(____).md>) to close a resource map.

## See Also

### Locating Bundle Resources

- [CFBundleCloseBundleResourceMap](<cfbundleclosebundleresourcemap(____).md>) — Closes an open resource map for a bundle. _(deprecated)_
- [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) — Returns the location of a resource contained in the specified bundle.
- [CFBundleCopyResourceURLInDirectory](<cfbundlecopyresourceurlindirectory(________).md>) — Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) — Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [CFBundleCopyResourceURLsOfTypeInDirectory](<cfbundlecopyresourceurlsoftypeindirectory(______).md>) — Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [CFBundleCopyResourceURLForLocalization](<cfbundlecopyresourceurlforlocalization(__________).md>) — Returns the location of a localized resource in a bundle.
- [CFBundleCopyResourceURLsOfTypeForLocalization](<cfbundlecopyresourceurlsoftypeforlocalization(________).md>) — Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [CFBundleOpenBundleResourceFiles](<cfbundleopenbundleresourcefiles(______).md>) — Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps. _(deprecated)_
