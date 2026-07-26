---
title: 'fileURL(withFileSystemRepresentation:isDirectory:relativeTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/fileurl(withfilesystemrepresentation:isdirectory:relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/fileurl(withfilesystemrepresentation:isdirectory:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/fileurl%28withfilesystemrepresentation%3Aisdirectory%3Arelativeto%3A%29.json'
content_hash: 'sha256:9fcc1bb3b23c6ffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# fileURL(withFileSystemRepresentation:isDirectory:relativeTo:)

<sub>Type Method</sub>

Returns a new URL object initialized with a C string representing a local file system path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fileURL(withFileSystemRepresentation path: UnsafePointer<CChar>, isDirectory isDir: Bool, relativeTo baseURL: URL?) -> URL
```

## Parameters

- `path` — A null-terminated C string in file system representation containing the path to represent as a URL. If this path is a relative path, it is treated as being relative to the current working directory.

- `isDir` — [true](../../swift/true.md) if the last path part is a directory, otherwise [false](../../swift/false.md).

- `baseURL` — The base URL for the new URL object. This must be a file URL. If `path` is absolute, this URL is ignored.

## Return Value

Returns the new object.

## Discussion

The file system representation format is described in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

## See Also

### Creating a URL object

- [- initWithString:](<init(string_).md>) — Initializes an NSURL object with a provided URL string.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithString:relativeToURL:](<init(string_relativeto_).md>) — Initializes an NSURL object with a base URL and a relative string.
- [+ fileURLWithPath:isDirectory:](<fileurl(withpath_isdirectory_).md>) — Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [- initFileURLWithPath:isDirectory:](<init(fileurlwithpath_isdirectory_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPath:relativeToURL:](<fileurl(withpath_relativeto_).md>) — Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [- initFileURLWithPath:relativeToURL:](<init(fileurlwithpath_relativeto_).md>) — Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [+ fileURLWithPath:isDirectory:relativeToURL:](<fileurl(withpath_isdirectory_relativeto_).md>) — Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [- initFileURLWithPath:isDirectory:relativeToURL:](<init(fileurlwithpath_isdirectory_relativeto_).md>) — Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [+ fileURLWithPath:](<fileurl(withpath_).md>) — Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [- initFileURLWithPath:](<init(fileurlwithpath_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPathComponents:](<fileurl(withpathcomponents_).md>) — Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [+ URLByResolvingAliasFileAtURL:options:error:](<init(resolvingaliasfileat_options_).md>) — Returns a new URL made by resolving the alias file at `url`.
- [- initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_).md>) — Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [- getFileSystemRepresentation:maxLength:](<getfilesystemrepresentation(__maxlength_).md>) — Fills the provided buffer with a C string representing a local file system path.
