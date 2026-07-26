---
title: 'init(fileReferenceLiteralResourceName:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(filereferenceliteralresourcename:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(filereferenceliteralresourcename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28filereferenceliteralresourcename%3A%29.json'
content_hash: 'sha256:b11e85c94cd34e13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(fileReferenceLiteralResourceName:)

<sub>Initializer</sub>

Creates a URL from a playground file literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fileReferenceLiteralResourceName name: String)
```

## Parameters

- `name` — The playground file literal name, as a string.

## See Also

### Creating a file URL from a string path

- [init(filePath:directoryHint:relativeTo:)](<init(filepath_directoryhint_relativeto_).md>) — Creates a file URL that references a path you specify as a string.
- [DirectoryHint](directoryhint.md) — A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath:)](<init(fileurlwithpath_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:isDirectory:)](<init(fileurlwithpath_isdirectory_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:relativeTo:)](<init(fileurlwithpath_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithPath:isDirectory:relativeTo:)](<init(fileurlwithpath_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithFileSystemRepresentation:isDirectory:relativeTo:)](<init(fileurlwithfilesystemrepresentation_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(filePath:directoryHint:)](<init(filepath_directoryhint_).md>) — Creates a file URL that references a file path.
