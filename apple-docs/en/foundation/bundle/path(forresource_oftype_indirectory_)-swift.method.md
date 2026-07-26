---
title: 'path(forResource:ofType:inDirectory:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/path(forresource:oftype:indirectory:)-swift.method'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/path(forresource:oftype:indirectory:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/path%28forresource%3Aoftype%3Aindirectory%3A%29-swift.method.json'
content_hash: 'sha256:aeefef2b2c164924'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# path(forResource:ofType:inDirectory:)

<sub>Instance Method</sub>

Returns the full pathname for the resource identified by the specified name and file extension and located in the specified bundle subdirectory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func path(forResource name: String?, ofType ext: String?, inDirectory subpath: String?) -> String?
```

## Parameters

- `name` — The name of the resource file. If you specify `nil`, the method returns the first resource file it finds that matches the remaining criteria.

- `ext` — The filename extension of the files to locate. If you specify an empty string or `nil`, all the files in `subpath` and its subdirectories are returned. If an extension is provided the subdirectories are not searched.

- `subpath` — The name of the bundle subdirectory.

## Return Value

The full pathname for the resource file, or `nil` if the file could not be located.

## Discussion

If `subpath` is `nil`, this method searches the top-level nonlocalized resource directory and the top-level of any language-specific directories. (In macOS, the top-level nonlocalized resource directory is typically called `Resources` but in iOS, it is the main bundle directory.) For example, suppose you have a Mac app with a modern bundle and you specify `@"Documentation"` for the `subpath` parameter. This method would first look in the `Contents/Resources/Documentation` directory of the bundle, followed by the `Documentation` subdirectories of each language-specific `.lproj` directory.

Whether this method recurses through subdirectories is dependent on the `extension` parameter. If `nil` or an empty string it will recurse, otherwise, it does not. (The search order for the language-specific directories corresponds to the user’s preferences.) For details on how localized resources are found, read [The Bundle Search Pattern](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW7) in [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

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
- [- pathForResource:ofType:inDirectory:forLocalization:](<path(forresource_oftype_indirectory_forlocalization_).md>) — Returns the full pathname for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [- pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.method.md>) — Returns an array containing the pathnames for all bundle resources having the specified filename extension and residing in the resource subdirectory.
- [- pathsForResourcesOfType:inDirectory:forLocalization:](<paths(forresourcesoftype_indirectory_forlocalization_).md>) — Returns an array containing the file for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [+ pathForResource:ofType:inDirectory:](<path(forresource_oftype_indirectory_)-swift.type.method.md>) — Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [+ pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.type.method.md>) — Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.
