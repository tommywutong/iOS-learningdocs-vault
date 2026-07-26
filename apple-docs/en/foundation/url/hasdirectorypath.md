---
title: hasDirectoryPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/hasdirectorypath
source_url: 'https://developer.apple.com/documentation/foundation/url/hasdirectorypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/hasdirectorypath.json'
content_hash: 'sha256:f3a7a98a50ac869b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# hasDirectoryPath

<sub>Instance Property</sub>

A Boolean that is true if the URL path represents a directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasDirectoryPath: Bool { get }
```

## See Also

### Working with file URLs

- [isFileURL](isfileurl.md) — A Boolean that is true if the scheme is `file:`.
- [withUnsafeFileSystemRepresentation(_:)](<withunsafefilesystemrepresentation(__).md>) — Passes the URL’s path in the file system representation to a closure.
- [resolveSymlinksInPath()](<resolvesymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [resolvingSymlinksInPath()](<resolvingsymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [standardize()](<standardize().md>) — Standardizes the path of a file URL.
