---
title: 'paths(forResourcesOfType:inDirectory:forLocalization:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/paths(forresourcesoftype:indirectory:forlocalization:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/paths(forresourcesoftype:indirectory:forlocalization:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/paths%28forresourcesoftype%3Aindirectory%3Aforlocalization%3A%29.json'
content_hash: 'sha256:fa5bda4dc876a00d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# paths(forResourcesOfType:inDirectory:forLocalization:)

<sub>Instance Method</sub>

Returns an array containing the file for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func paths(forResourcesOfType ext: String?, inDirectory subpath: String?, forLocalization localizationName: String?) -> [String]
```

## Parameters

- `ext` — The filename extension of the files to locate. If you specify an empty string or `nil`, the extension is assumed not to exist and all of the files in `subpath` are returned.

- `subpath` — The name of the bundle subdirectory to search.

- `localizationName` — The language ID for the localization. This parameter should correspond to the name of one of the bundle’s language-specific resource directories without the `.lproj` extension.

## Return Value

An array containing the full pathnames for all bundle resources matching the specified criteria. This method returns an empty array if no matching resource files are found.

## Discussion

This method is equivalent to [- pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.method.md>), except that only nonlocalized resources and those in the language-specific `.lproj` directory specified by `localizationName` are searched.

## See Also

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
- [+ pathForResource:ofType:inDirectory:](<path(forresource_oftype_indirectory_)-swift.type.method.md>) — Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [+ pathsForResourcesOfType:inDirectory:](<paths(forresourcesoftype_indirectory_)-swift.type.method.md>) — Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.
