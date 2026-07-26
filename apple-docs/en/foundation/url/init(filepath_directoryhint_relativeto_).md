---
title: 'init(filePath:directoryHint:relativeTo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(filepath:directoryhint:relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(filepath:directoryhint:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28filepath%3Adirectoryhint%3Arelativeto%3A%29.json'
content_hash: 'sha256:13dfe728e09ba5e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(filePath:directoryHint:relativeTo:)

<sub>Initializer</sub>

Creates a file URL that references a path you specify as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(filePath path: String, directoryHint: URL.DirectoryHint = .inferFromPath, relativeTo base: URL? = nil)
```

## Parameters

- `path` — The location in the file system, as a string.

- `directoryHint` — A hint to the initializer to indicate whether the path is a directory, or to instruct the initializer to make this determination.

- `base` — A URL that provides a file system location that the path extends.

## See Also

### Creating a file URL from a string path

- [DirectoryHint](directoryhint.md) — A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath:)](<init(fileurlwithpath_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:isDirectory:)](<init(fileurlwithpath_isdirectory_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:relativeTo:)](<init(fileurlwithpath_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithPath:isDirectory:relativeTo:)](<init(fileurlwithpath_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithFileSystemRepresentation:isDirectory:relativeTo:)](<init(fileurlwithfilesystemrepresentation_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName:)](<init(filereferenceliteralresourcename_).md>) — Creates a URL from a playground file literal.
- [init(filePath:directoryHint:)](<init(filepath_directoryhint_).md>) — Creates a file URL that references a file path.
