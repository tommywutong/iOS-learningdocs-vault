---
title: isFileURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/isfileurl
source_url: 'https://developer.apple.com/documentation/foundation/url/isfileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/isfileurl.json'
content_hash: 'sha256:73119c9f12491082'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# isFileURL

<sub>Instance Property</sub>

A Boolean that is true if the scheme is `file:`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFileURL: Bool { get }
```

## See Also

### Working with file URLs

- [hasDirectoryPath](hasdirectorypath.md) — A Boolean that is true if the URL path represents a directory.
- [withUnsafeFileSystemRepresentation(_:)](<withunsafefilesystemrepresentation(__).md>) — Passes the URL’s path in the file system representation to a closure.
- [resolveSymlinksInPath()](<resolvesymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [resolvingSymlinksInPath()](<resolvingsymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [standardize()](<standardize().md>) — Standardizes the path of a file URL.
