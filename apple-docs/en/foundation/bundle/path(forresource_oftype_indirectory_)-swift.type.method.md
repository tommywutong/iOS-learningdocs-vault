---
title: 'path(forResource:ofType:inDirectory:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/path(forresource:oftype:indirectory:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/path(forresource:oftype:indirectory:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/path%28forresource%3Aoftype%3Aindirectory%3A%29-swift.type.method.json'
content_hash: 'sha256:4932ffacc28306ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# path(forResource:ofType:inDirectory:)

<sub>Type Method</sub>

Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func path(forResource name: String?, ofType ext: String?, inDirectory bundlePath: String) -> String?
```

## Parameters

- `name` — The name of a resource file contained in the directory specified by `bundlePath`. If you specify `nil`, the method returns the first resource file it finds with the specified extension.

- `ext` — The filename extension of the file to locate. If you specify an empty string or `nil`, the extension is assumed not to exist and the file is the first file encountered that exactly matches `name`.

- `bundlePath` — The path of a top-level bundle directory. This must be a valid path. For example, to specify the bundle directory for a Mac app, you might specify the path `/Applications/MyApp.app`.

## Return Value

The full pathname for the resource file or `nil` if the file could not be located. This method also returns `nil` if the bundle specified by the `bundlePath` parameter does not exist or is not a readable directory.

## Discussion

For details on how localized resources are found, read [The Bundle Search Pattern](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW7) in [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

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
- [+ pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.type.method.md>) — Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.
