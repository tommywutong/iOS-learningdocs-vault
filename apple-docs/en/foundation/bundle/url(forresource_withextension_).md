---
title: 'url(forResource:withExtension:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/url(forresource:withextension:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/url(forresource:withextension:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/url%28forresource%3Awithextension%3A%29.json'
content_hash: 'sha256:0ed831fe2adbd8b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# url(forResource:withExtension:)

<sub>Instance Method</sub>

Returns the file URL for the resource identified by the specified name and file extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func url(forResource name: String?, withExtension ext: String?) -> URL?
```

## Parameters

- `name` — The name of the resource file. If you specify `nil`, the method returns the first resource file it finds with the specified extension.

- `ext` — The extension of the resource file. If `extension` is an empty string or `nil`, the extension is assumed not to exist and the file URL is the first file encountered that exactly matches `name`.

## Return Value

The file URL for the resource file or `nil` if the file could not be located.

## Discussion

If `extension` is an empty string or `nil`, the returned pathname is the first one encountered where the file name exactly matches `name`. For details on how localized resources are found, read [The Bundle Search Pattern](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW7) in [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

## See Also

### Finding resource files

- [- URLForResource:withExtension:subdirectory:](<url(forresource_withextension_subdirectory_).md>) — Returns the file URL for the resource file identified by the specified name and extension and residing in a given bundle directory.
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
- [+ pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.type.method.md>) — Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.
