---
title: 'appendingPathComponent(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/appendingpathcomponent(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/appendingpathcomponent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/appendingpathcomponent%28_%3A%29.json'
content_hash: 'sha256:721e9b165411b69a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# appendingPathComponent(_:)

<sub>Instance Method</sub>

Returns a new URL by appending a path component to the original URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingPathComponent(_ pathComponent: String) -> URL?
```

## Parameters

- `pathComponent` — The path component to add to the URL, in its original form (not URL encoded).

## Return Value

A new URL with `pathComponent` appended.

## Discussion

If the original URL does not end with a forward slash and `pathComponent` does not begin with a forward slash, a forward slash is inserted between the two parts of the returned URL, unless the original URL is the empty string.

If the receiver is a file URL and `pathComponent` does not end with a trailing slash, this method may read file metadata to determine whether the resulting path is a directory. This is done synchronously, and may have significant performance costs if the receiver is a location on a network mounted filesystem. You can instead call the [- URLByAppendingPathComponent:isDirectory:](<appendingpathcomponent(__isdirectory_).md>) method if you know whether the resulting path is a directory to avoid this file metadata operation.

## See Also

### Modifying and Converting a File URL

- [filePathURL](filepathurl.md) — A file path URL that points to the same resource as the URL object. (read-only)
- [- fileReferenceURL](<filereferenceurl().md>) — Returns a new file reference URL that points to the same resource as the receiver.
- [- URLByAppendingPathComponent:isDirectory:](<appendingpathcomponent(__isdirectory_).md>) — Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [- URLByAppendingPathComponent:conformingToType:](<appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [- URLByAppendingPathExtension:](<appendingpathextension(__).md>) — Returns a new URL by appending a path extension to the original URL.
- [- URLByAppendingPathExtensionForType:](<appendingpathextension(for_).md>) — Returns a URL by appending the path extension for a uniform type identifier.
- [URLByDeletingLastPathComponent](deletinglastpathcomponent.md) — A URL you create by removing the last path component from the receiver. (read-only)
- [URLByDeletingPathExtension](deletingpathextension.md) — A URL you create by removing the path extension from the receiver, if any. (read-only)
- [URLByResolvingSymlinksInPath](resolvingsymlinksinpath.md) — A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [URLByStandardizingPath](standardizingpath.md) — A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean value that indicates whether the URL string’s path represents a directory.
