---
title: standardizingPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/standardizingpath
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/standardizingpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/standardizingpath.json'
content_hash: 'sha256:10eb10d56e56dab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# standardizingPath

<sub>Instance Property</sub>

A URL that points to the same resource as the original URL using an absolute path. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var standardizingPath: URL? { get }
```

## Discussion

This property only works on URLs with the `file:` path scheme. For all other URLs, it returns a copy of the original URL.

Like [stringByStandardizingPath](../nsstring/standardizingpath.md), this property can make the following changes in the provided URL:

- Expand an initial tilde expression using [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md).
- Reduce empty components and references to the current directory (that is, the sequences “//” and “/./”) to single path separators.
- In absolute paths only, resolve references to the parent directory (that is, the component “..”) to the real parent directory if possible using [stringByResolvingSymlinksInPath](../nsstring/resolvingsymlinksinpath.md), which consults the file system to resolve each potential symbolic link.

In relative paths, because symbolic links can’t be resolved, references to the parent directory are left in place.

- Remove an initial component of “/private” from the path if the result still indicates an existing file or directory (checked by consulting the file system).

Note that the path contained by this property may still have symbolic link components in it. Note also that this property only works with file paths (not, for example, string representations of URLs).

## See Also

### Modifying and Converting a File URL

- [filePathURL](filepathurl.md) — A file path URL that points to the same resource as the URL object. (read-only)
- [- fileReferenceURL](<filereferenceurl().md>) — Returns a new file reference URL that points to the same resource as the receiver.
- [- URLByAppendingPathComponent:](<appendingpathcomponent(__).md>) — Returns a new URL by appending a path component to the original URL.
- [- URLByAppendingPathComponent:isDirectory:](<appendingpathcomponent(__isdirectory_).md>) — Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [- URLByAppendingPathComponent:conformingToType:](<appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [- URLByAppendingPathExtension:](<appendingpathextension(__).md>) — Returns a new URL by appending a path extension to the original URL.
- [- URLByAppendingPathExtensionForType:](<appendingpathextension(for_).md>) — Returns a URL by appending the path extension for a uniform type identifier.
- [URLByDeletingLastPathComponent](deletinglastpathcomponent.md) — A URL you create by removing the last path component from the receiver. (read-only)
- [URLByDeletingPathExtension](deletingpathextension.md) — A URL you create by removing the path extension from the receiver, if any. (read-only)
- [URLByResolvingSymlinksInPath](resolvingsymlinksinpath.md) — A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean value that indicates whether the URL string’s path represents a directory.
