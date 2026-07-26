---
title: 'enumerator(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/enumerator(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/enumerator(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/enumerator%28atpath%3A%29.json'
content_hash: 'sha256:41354018865789ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# enumerator(atPath:)

<sub>Instance Method</sub>

Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerator(atPath path: String) -> FileManager.DirectoryEnumerator?
```

## Parameters

- `path` — The path of the directory to enumerate.

## Return Value

A [DirectoryEnumerator](directoryenumerator.md) object that enumerates the contents of the directory at `path`.

## Discussion

If `path` is a filename, the method returns an enumerator object that enumerates no files—the first call to [- nextObject](<../nsenumerator/nextobject().md>) will return `nil`.

Because the enumeration is deep—that is, it lists the contents of all subdirectories—this enumerator object is useful for performing actions that involve large file-system subtrees. This method does not resolve symbolic links encountered in the traversal process, nor does it recurse through them if they point to a directory.

This code fragment enumerates the subdirectories and files under a user’s `Documents` directory and processes all files with an extension of `.doc`:

```objc
NSString *docsDir = [NSHomeDirectory() stringByAppendingPathComponent:  @"Documents"];
NSFileManager *localFileManager=[[NSFileManager alloc] init];
NSDirectoryEnumerator *dirEnum =
    [localFileManager enumeratorAtPath:docsDir];
 
NSString *file;
while ((file = [dirEnum nextObject])) {
    if ([[file pathExtension] isEqualToString: @"doc"]) {
        // process the document
        [self scanDocument: [docsDir stringByAppendingPathComponent:file]];
    }
}
```

The [DirectoryEnumerator](directoryenumerator.md) class has methods for obtaining the attributes of the existing path and of the parent directory and for skipping descendants of the existing path.

## See Also

### Related Documentation

- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [currentDirectoryPath](currentdirectorypath.md) — The path to the program’s current directory.

### Discovering directory contents

- [- contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](<contentsofdirectory(at_includingpropertiesforkeys_options_).md>) — Performs a shallow search of the specified directory and returns URLs for the contained items.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.
- [enumerator(at:includingPropertiesForKeys:options:errorHandler:)](<enumerator(at_includingpropertiesforkeys_options_errorhandler_).md>) — Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [DirectoryEnumerator](directoryenumerator.md) — An object that enumerates the contents of a directory.
- [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) — Returns an array of URLs that identify the mounted volumes available on the device.
- [VolumeEnumerationOptions](volumeenumerationoptions.md) — Options for enumerating mounted volumes with the [- mountedVolumeURLsIncludingResourceValuesForKeys:options:](<mountedvolumeurls(includingresourcevaluesforkeys_options_).md>) method.
- [- subpathsOfDirectoryAtPath:error:](<subpathsofdirectory(atpath_).md>) — Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- subpathsAtPath:](<subpaths(atpath_).md>) — Returns an array of strings identifying the paths for all items in the specified directory.
