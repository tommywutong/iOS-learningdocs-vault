---
title: 'subpathsOfDirectory(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/subpathsofdirectory(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/subpathsofdirectory(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/subpathsofdirectory%28atpath%3A%29.json'
content_hash: 'sha256:4191979164ffa4fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# subpathsOfDirectory(atPath:)

<sub>Instance Method</sub>

Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subpathsOfDirectory(atPath path: String) throws -> [String]
```

## Parameters

- `path` — The path of the directory to list.

## Return Value

An array of strings, each containing the path of an item in the directory specified by `path`. When using Objective-C, returns `nil` if an error occurred.

## Discussion

This method recurses the specified directory and its subdirectories. The method skips the “`.`” and “`..`” directories at each level of the recursion.

Because this method recurses the directory’s contents, you might not want to use it in performance-critical code. Instead, consider using the [enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md) or [- enumeratorAtPath:](<enumerator(atpath_).md>) method to enumerate the directory contents yourself. Doing so gives you more control over the retrieval of items and more opportunities to complete the enumeration or perform other tasks at the same time.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [DirectoryEnumerator](directoryenumerator.md) — An object that enumerates the contents of a directory.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [VolumeEnumerationOptions](volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
