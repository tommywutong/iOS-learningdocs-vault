---
title: 'CFBundleCopyResourceURLsOfTypeInDirectory(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyresourceurlsoftypeindirectory(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyresourceurlsoftypeindirectory(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyresourceurlsoftypeindirectory%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3e58b23d67598253'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyResourceURLsOfTypeInDirectory(_:_:_:)

<sub>Function</sub>

Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyResourceURLsOfTypeInDirectory(_ bundleURL: CFURL!, _ resourceType: CFString!, _ subDirName: CFString!) -> CFArray!
```

## Parameters

- `bundleURL` — The location of a bundle to examine.

- `resourceType` — The abstract type of the resources to locate. The type is expressed as a filename extension, such as `jpg`.

- `subDirName` — The name of the subdirectory of the bundle’s resources directory to search. Pass `NULL` to search the standard CFBundle resource locations.

## Return Value

A CFArray object containing the CFURL objects of the requested resources. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function provides a means to obtain an array containing the locations of all of the requested resources without first creating a CFBundle object. However, since CFBundle objects cache search results, it is faster to create a CFBundle object if you need to repeatedly access resources.

Note that file names are case-sensitive, even on file systems (such as HFS+) that are not case sensitive with regards to file names.

## See Also

### Locating Bundle Resources

- [CFBundleCloseBundleResourceMap](<cfbundleclosebundleresourcemap(____).md>) — Closes an open resource map for a bundle. _(deprecated)_
- [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) — Returns the location of a resource contained in the specified bundle.
- [CFBundleCopyResourceURLInDirectory](<cfbundlecopyresourceurlindirectory(________).md>) — Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) — Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [CFBundleCopyResourceURLForLocalization](<cfbundlecopyresourceurlforlocalization(__________).md>) — Returns the location of a localized resource in a bundle.
- [CFBundleCopyResourceURLsOfTypeForLocalization](<cfbundlecopyresourceurlsoftypeforlocalization(________).md>) — Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [CFBundleOpenBundleResourceFiles](<cfbundleopenbundleresourcefiles(______).md>) — Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps. _(deprecated)_
- [CFBundleOpenBundleResourceMap](<cfbundleopenbundleresourcemap(__).md>) — Opens the non-localized and localized resource files (if any) for a bundle in a single resource map. _(deprecated)_
