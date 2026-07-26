---
title: 'paths(forResourcesOfType:inDirectory:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/paths(forresourcesoftype:indirectory:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/paths(forresourcesoftype:indirectory:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/paths%28forresourcesoftype%3Aindirectory%3A%29-swift.type.method.json'
content_hash: 'sha256:d63cd000a9f1d55c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# paths(forResourcesOfType:inDirectory:)

<sub>Type Method</sub>

Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func paths(forResourcesOfType ext: String?, inDirectory bundlePath: String) -> [String]
```

## Parameters

- `ext` — The filename extension of the files to locate. If you specify an empty string or `nil`, the extension is assumed not to exist and all of the files in `bundlePath` are returned.

- `bundlePath` — The top-level directory of a bundle. This must represent a valid path.

## Return Value

An array containing the full pathnames for all bundle resources with the specified extension. This method returns an empty array if no matching resource files are found. It also returns an empty array if the bundle specified by the `bundlePath` parameter does not exist or is not a readable directory.

## Discussion

This method provides a means for dynamically discovering multiple bundle resources of the same type. For details on how localized resources are found, read [The Bundle Search Pattern](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW7) in [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

> [!note] Note
> This method is best suited only for the occasional retrieval of resource files. In most cases where you need to retrieve bundle resources, it is preferable to use the `NSBundle` instance methods instead.

## See Also

### Related Documentation

- [- localizedStringForKey:value:table:](<localizedstring(forkey_value_table_).md>) — Returns a localized version of the string designated by the specified key and residing in the specified table.

### Finding resource files

- [- URLForResource:withExtension:subdirectory:](<url(forresource_withextension_subdirectory_).md>) — Returns the file URL for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [- URLForResource:withExtension:](<url(forresource_withextension_).md>) — Returns the file URL for the resource identified by the specified name and file extension.
- [- URLsForResourcesWithExtension:subdirectory:](<urls(forresourceswithextension_subdirectory_).md>) — Returns an array of file URLs for all resources identified by the specified file extension and located in the specified bundle subdirectory.
- [- URLForResource:withExtension:subdirectory:localization:](<url(forresource_withextension_subdirectory_localization_).md>) — Returns the file URL for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [- URLsForResourcesWithExtension:subdirectory:localization:](<urls(forresourceswithextension_subdirectory_localization_).md>) — Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [+ URLForResource:withExtension:subdirectory:inBundleWithURL:](<url(forresource_withextension_subdirectory_in_).md>) — Creates and returns a file URL for the resource with the specified name and extension in the specified bundle.
- [+ URLsForResourcesWithExtension:subdirectory:inBundleWithURL:](<urls(forresourceswithextension_subdirectory_in_).md>) — Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, within the specified bundle.
- [- pathForResource:ofType:](<path(forresource_oftype_).md>) — Returns the full pathname for the resource identified by the specified name and file extension.
- [- pathForResource:ofType:inDirectory:](<path(forresource_oftype_indirectory_)-swift.method.md>) — Returns the full pathname for the resource identified by the specified name and file extension and located in the specified bundle subdirectory.
- [- pathForResource:ofType:inDirectory:forLocalization:](<path(forresource_oftype_indirectory_forlocalization_).md>) — Returns the full pathname for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [- pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.method.md>) — Returns an array containing the pathnames for all bundle resources having the specified filename extension and residing in the resource subdirectory.
- [- pathsForResourcesOfType:inDirectory:forLocalization:](<paths(forresourcesoftype_indirectory_forlocalization_).md>) — Returns an array containing the file for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [+ pathForResource:ofType:inDirectory:](<path(forresource_oftype_indirectory_)-swift.type.method.md>) — Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.
