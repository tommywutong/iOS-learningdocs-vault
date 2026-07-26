---
title: URL.DirectoryHint
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/directoryhint
source_url: 'https://developer.apple.com/documentation/foundation/url/directoryhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/directoryhint.json'
content_hash: 'sha256:371dbffcc6116839'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# URL.DirectoryHint

<sub>Enumeration</sub>

A hint to URL file APIs for handling paths that may reference directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DirectoryHint
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Hints

- [URL.DirectoryHint.isDirectory](directoryhint/isdirectory.md) — A hint that specifies that a given path is a directory.
- [URL.DirectoryHint.notDirectory](directoryhint/notdirectory.md) — A hint that specifies that a given path isn’t a directory.
- [URL.DirectoryHint.checkFileSystem](directoryhint/checkfilesystem.md) — A hint that directs a URL call to consult the file system to determine whether the path references a directory.
- [URL.DirectoryHint.inferFromPath](directoryhint/inferfrompath.md) — A hint that directs a URL call to infer whether a path references a directory based on whether it has a trailing slash.

## See Also

### Creating a file URL from a string path

- [init(filePath:directoryHint:relativeTo:)](<init(filepath_directoryhint_relativeto_).md>) — Creates a file URL that references a path you specify as a string.
- [init(fileURLWithPath:)](<init(fileurlwithpath_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:isDirectory:)](<init(fileurlwithpath_isdirectory_).md>) — Creates a file URL that references the local file or directory at the given path. _(deprecated)_
- [init(fileURLWithPath:relativeTo:)](<init(fileurlwithpath_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithPath:isDirectory:relativeTo:)](<init(fileurlwithpath_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory at the given path, relative to a base URL. _(deprecated)_
- [init(fileURLWithFileSystemRepresentation:isDirectory:relativeTo:)](<init(fileurlwithfilesystemrepresentation_isdirectory_relativeto_).md>) — Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName:)](<init(filereferenceliteralresourcename_).md>) — Creates a URL from a playground file literal.
- [init(filePath:directoryHint:)](<init(filepath_directoryhint_).md>) — Creates a file URL that references a file path.
