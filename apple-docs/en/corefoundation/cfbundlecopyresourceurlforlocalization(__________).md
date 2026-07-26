---
title: 'CFBundleCopyResourceURLForLocalization(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopyresourceurlforlocalization(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopyresourceurlforlocalization(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopyresourceurlforlocalization%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:be85a7a8b61ad2cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyResourceURLForLocalization(_:_:_:_:_:)

<sub>Function</sub>

Returns the location of a localized resource in a bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyResourceURLForLocalization(_ bundle: CFBundle!, _ resourceName: CFString!, _ resourceType: CFString!, _ subDirName: CFString!, _ localizationName: CFString!) -> CFURL!
```

## Parameters

- `bundle` — The bundle to examine.

- `resourceName` — The name of the requested resource.

- `resourceType` — The abstract type of the resource to locate. The type is expressed as a filename extension, such as `jpg`.

- `subDirName` — The name of the subdirectory of the bundle’s resources directory to search. Pass `NULL` to search the standard CFBundle resource locations.

- `localizationName` — The name of the localization. This value should correspond to the name of one of the bundle’s language-specific resource directories without the `.lproj` extension. (This parameter is treated literally: If you pass `"de"`, the function will not match resources in a `German.lproj` directory in the bundle.)

## Return Value

The location of a localized resource in `bundle`, or `NULL` if the resource could not be found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that file names are case-sensitive, even on file systems (such as HFS+) that are not case sensitive with regards to file names.

You should typically have little reason to use this function (see Getting the Current Language and Locale)—CFBundle’s interfaces automatically apply the user’s preferences to determine which localized resource files to return in response to a programmatic request. See also [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) for how to determine what localizations are available

## See Also

### Locating Bundle Resources

- [CFBundleCloseBundleResourceMap](<cfbundleclosebundleresourcemap(____).md>) — Closes an open resource map for a bundle. _(deprecated)_
- [CFBundleCopyResourceURL](<cfbundlecopyresourceurl(________).md>) — Returns the location of a resource contained in the specified bundle.
- [CFBundleCopyResourceURLInDirectory](<cfbundlecopyresourceurlindirectory(________).md>) — Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [CFBundleCopyResourceURLsOfType](<cfbundlecopyresourceurlsoftype(______).md>) — Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [CFBundleCopyResourceURLsOfTypeInDirectory](<cfbundlecopyresourceurlsoftypeindirectory(______).md>) — Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [CFBundleCopyResourceURLsOfTypeForLocalization](<cfbundlecopyresourceurlsoftypeforlocalization(________).md>) — Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [CFBundleOpenBundleResourceFiles](<cfbundleopenbundleresourcefiles(______).md>) — Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps. _(deprecated)_
- [CFBundleOpenBundleResourceMap](<cfbundleopenbundleresourcemap(__).md>) — Opens the non-localized and localized resource files (if any) for a bundle in a single resource map. _(deprecated)_
