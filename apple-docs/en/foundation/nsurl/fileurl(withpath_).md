---
title: 'fileURL(withPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/fileurl(withpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/fileurl(withpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/fileurl%28withpath%3A%29.json'
content_hash: 'sha256:c9c0621f38b4a19c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# fileURL(withPath:)

<sub>Type Method</sub>

Initializes and returns a newly created NSURL object as a file URL with a specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fileURL(withPath path: String) -> URL
```

## Parameters

- `path` — The path that the NSURL object will represent. `path` should be a valid system path, and must not be an empty path. If `path` begins with a tilde, it must first be expanded with [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md). If `path` is a relative path, it is treated as being relative to the current working directory.

## Return Value

An NSURL object initialized with `path`.

## Discussion

This method assumes that `path` is a directory if it ends with a slash. If `path` does not end with a slash, the method examines the file system to determine if `path` is a file or a directory. If `path` exists in the file system and is a directory, the method appends a trailing slash. If `path` does not exist in the file system, the method assumes that it represents a file and does not append a trailing slash.

As an alternative, consider using [+ fileURLWithPath:isDirectory:](<fileurl(withpath_isdirectory_).md>), which allows you to explicitly specify whether the returned `NSURL` object represents a file or directory.

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
- [- initFileURLWithPath:](<init(fileurlwithpath_).md>) — Initializes a newly created NSURL referencing the local file or directory at `path`.
- [+ fileURLWithPathComponents:](<fileurl(withpathcomponents_).md>) — Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [+ URLByResolvingAliasFileAtURL:options:error:](<init(resolvingaliasfileat_options_).md>) — Returns a new URL made by resolving the alias file at `url`.
- [- initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_).md>) — Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [+ fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:](<fileurl(withfilesystemrepresentation_isdirectory_relativeto_).md>) — Returns a new URL object initialized with a C string representing a local file system path.
- [- getFileSystemRepresentation:maxLength:](<getfilesystemrepresentation(__maxlength_).md>) — Fills the provided buffer with a C string representing a local file system path.
