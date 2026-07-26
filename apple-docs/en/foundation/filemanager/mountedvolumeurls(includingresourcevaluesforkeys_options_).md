---
title: 'mountedVolumeURLs(includingResourceValuesForKeys:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/mountedvolumeurls%28includingresourcevaluesforkeys%3Aoptions%3A%29.json'
content_hash: 'sha256:d766d6a5657d3a49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# mountedVolumeURLs(includingResourceValuesForKeys:options:)

<sub>Instance Method</sub>

Returns an array of URLs that identify the mounted volumes available on the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mountedVolumeURLs(includingResourceValuesForKeys propertyKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions = []) -> [URL]?
```

## Parameters

- `propertyKeys` — An array of keys that identify the file properties that you want pre-fetched for each volume. For each returned URL, the values for these keys are cached in the corresponding [NSURL](../nsurl.md) objects. You may specify `nil` for this parameter. For a list of keys you can specify, see Common File System Resource Keys.

- `options` — Option flags for the enumeration. For a list of possible values, see [VolumeEnumerationOptions](volumeenumerationoptions.md).

## Return Value

An array of `NSURL` objects identifying the mounted volumes.

> [!important] Important
> This method returns `nil` on platforms other than macOS.

## Discussion

This call may block if I/O is required to determine values for the requested `propertyKeys`.

## See Also

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [DirectoryEnumerator](directoryenumerator.md) — An object that enumerates the contents of a directory.
- [VolumeEnumerationOptions](volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
