---
title: resolvingSymlinksInPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/resolvingsymlinksinpath
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/resolvingsymlinksinpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/resolvingsymlinksinpath.json'
content_hash: 'sha256:251550110a26aed2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# resolvingSymlinksInPath

<sub>Instance Property</sub>

A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resolvingSymlinksInPath: URL? { get }
```

## Discussion

If the receiver has no symbolic links, this property contains a copy of the original URL.

If some symbolic links cannot be resolved, this property contains those broken symbolic links.

If the name of the receiving path begins with `/private`, this property strips off the `/private` designator, provided the result is the name of an existing file.

This property only works on URLs with the `file:` path scheme. For all other URLs, it contains a copy of the receiver.

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
- [URLByStandardizingPath](standardizingpath.md) — A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean value that indicates whether the URL string’s path represents a directory.
