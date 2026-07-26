---
title: 'contentsOfDirectory(at:includingPropertiesForKeys:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/contentsofdirectory%28at%3Aincludingpropertiesforkeys%3Aoptions%3A%29.json'
content_hash: 'sha256:82a8aa3767592554'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# contentsOfDirectory(at:includingPropertiesForKeys:options:)

<sub>Instance Method</sub>

Performs a shallow search of the specified directory and returns URLs for the contained items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contentsOfDirectory(at url: URL, includingPropertiesForKeys keys: [URLResourceKey]?, options mask: FileManager.DirectoryEnumerationOptions = []) throws -> [URL]
```

## Parameters

- `url` — The URL for the directory whose contents you want to enumerate.

- `keys` — An array of keys that identify the file properties that you want pre-fetched for each item in the directory. For each returned URL, the specified properties are fetched and cached in the [NSURL](../nsurl.md) object. For a list of keys you can specify, see [Common File System Resource Keys](../../corefoundation/common-file-system-resource-keys.md). If you want directory contents to have no pre-fetched file properties, pass an empty array to this parameter. If you want directory contents to have default set of pre-fetched file properties, pass `nil` to this parameter.

- `mask` — Options for the enumeration. Because this method performs only shallow enumerations, options that prevent descending into subdirectories or packages are not allowed; the only supported option is [NSDirectoryEnumerationSkipsHiddenFiles](directoryenumerationoptions/skipshiddenfiles.md).

## Return Value

An array of [NSURL](../nsurl.md) objects, each of which identifies a file, directory, or symbolic link contained in `url`. If the directory contains no entries, this method returns an empty array. When using Objective-C, if an error occurs, this method returns `nil` and assigns an appropriate error object to the `error` parameter.

## Discussion

This method performs a shallow search of the directory and therefore does not traverse symbolic links or return the contents of any subdirectories. This method also does not return URLs for the current directory (”`.`”), parent directory (”`..`”), or resource forks (files that begin with “`._`”) but it does return other hidden files. If you need to perform a deep enumeration, use the [enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md) method instead.

The order of the files in the returned array is undefined.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Discovering directory contents

- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [DirectoryEnumerator](directoryenumerator.md) — An object that enumerates the contents of a directory.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [VolumeEnumerationOptions](volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
