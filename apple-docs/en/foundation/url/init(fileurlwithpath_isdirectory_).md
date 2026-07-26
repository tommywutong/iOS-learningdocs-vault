---
title: 'init(fileURLWithPath:isDirectory:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 8.0+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/url/init(fileurlwithpath:isdirectory:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(fileurlwithpath:isdirectory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28fileurlwithpath%3Aisdirectory%3A%29.json'
content_hash: 'sha256:1c9e8285687b6c30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(fileURLWithPath:isDirectory:)

<sub>Initializer</sub>

Creates a file URL that references the local file or directory at the given path.

> [!warning] Deprecated
> Use [init(filePath:directoryHint:relativeTo:)](<init(filepath_directoryhint_relativeto_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fileURLWithPath path: String, isDirectory: Bool)
```

## Parameters

- `path` — The location in the file system.

- `isDirectory` — A Boolean value that indicates whether the location is a directory.

## Discussion

If the path is an empty string, the system interprets it as “.”.

> [!note] Note
> This method avoids file system I/O to determine if the path is to a directory. When you know that information, prefer this method to initializers without the parameter.

## See Also

### Creating a file URL from a string path

- [init(filePath:directoryHint:relativeTo:)](<init(filepath_directoryhint_relativeto_).md>) — Creates a file URL that references a path you specify as a string.
- [DirectoryHint](directoryhint.md) — A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath:)](<init(fileurlwithpath_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:relativeTo:)](<init(fileurlwithpath_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithPath:isDirectory:relativeTo:)](<init(fileurlwithpath_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithFileSystemRepresentation:isDirectory:relativeTo:)](<init(fileurlwithfilesystemrepresentation_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName:)](<init(filereferenceliteralresourcename_).md>) — Creates a URL from a playground file literal.
- [init(filePath:directoryHint:)](<init(filepath_directoryhint_).md>) — Creates a file URL that references a file path.
