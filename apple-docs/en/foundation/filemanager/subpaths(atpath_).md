---
title: 'subpaths(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/subpaths(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/subpaths(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/subpaths%28atpath%3A%29.json'
content_hash: 'sha256:7722bbe247077a9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# subpaths(atPath:)

<sub>Instance Method</sub>

Returns an array of strings identifying the paths for all items in the specified directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subpaths(atPath path: String) -> [String]?
```

## Parameters

- `path` — The path of the directory to list.

## Return Value

An array of [NSString](../nsstring.md) objects, each of which contains the path of an item in the directory specified by `path`. If `path` is a symbolic link, this method traverses the link. This method returns `nil` if it cannot retrieve the device of the linked-to file.

## Discussion

This method recurses the specified directory and its subdirectories. The method skips the “`.`” and “`..`” directories at each level of the recursion.

This method reveals every element of the subtree at `path`, including the contents of file packages (such as apps, nib files, and RTFD files). This code fragment gets the contents of `/System/Library/Fonts` after verifying that the directory exists:

```objc
BOOL isDir = NO;
NSArray *subpaths;
NSString *fontPath = @"/System/Library/Fonts";
NSFileManager *fileManager = [[NSFileManager alloc] init];
if ([fileManager fileExistsAtPath:fontPath isDirectory:&isDir] && isDir)
    subpaths = [fileManager subpathsAtPath:fontPath];
```

### Special Considerations

In macOS 10.5 and later, use [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) instead.

## See Also

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [- enumeratorAtPath:](<enumerator(atpath_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [DirectoryEnumerator](directoryenumerator.md) — An object that enumerates the contents of a directory.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [VolumeEnumerationOptions](volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
