---
title: 'appendingPathComponent(_:isDirectory:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/appendingpathcomponent(_:isdirectory:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/appendingpathcomponent(_:isdirectory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/appendingpathcomponent%28_%3Aisdirectory%3A%29.json'
content_hash: 'sha256:adfdd94560727dca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# appendingPathComponent(_:isDirectory:)

<sub>Instance Method</sub>

Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingPathComponent(_ pathComponent: String, isDirectory: Bool) -> URL?
```

## Parameters

- `pathComponent` — The path component to add to the URL.

- `isDirectory` — If [true](../../swift/true.md), a trailing slash is appended after `pathComponent`.

## Return Value

A new URL with `pathComponent` appended.

## Discussion

If the original URL does not end with a forward slash and `pathComponent` does not begin with a forward slash, a forward slash is inserted between the two parts of the returned URL, unless the original URL is the empty string.

## See Also

### Modifying and Converting a File URL

- [filePathURL](filepathurl.md) — A file path URL that points to the same resource as the URL object. (read-only)
- [- fileReferenceURL](<filereferenceurl().md>) — Returns a new file reference URL that points to the same resource as the receiver.
- [- URLByAppendingPathComponent:](<appendingpathcomponent(__).md>) — Returns a new URL by appending a path component to the original URL.
- [- URLByAppendingPathComponent:conformingToType:](<appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [- URLByAppendingPathExtension:](<appendingpathextension(__).md>) — Returns a new URL by appending a path extension to the original URL.
- [- URLByAppendingPathExtensionForType:](<appendingpathextension(for_).md>) — Returns a URL by appending the path extension for a uniform type identifier.
- [URLByDeletingLastPathComponent](deletinglastpathcomponent.md) — A URL you create by removing the last path component from the receiver. (read-only)
- [URLByDeletingPathExtension](deletingpathextension.md) — A URL you create by removing the path extension from the receiver, if any. (read-only)
- [URLByResolvingSymlinksInPath](resolvingsymlinksinpath.md) — A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [URLByStandardizingPath](standardizingpath.md) — A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean value that indicates whether the URL string’s path represents a directory.
