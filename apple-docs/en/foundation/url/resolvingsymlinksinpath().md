---
title: resolvingSymlinksInPath()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/resolvingsymlinksinpath()
source_url: 'https://developer.apple.com/documentation/foundation/url/resolvingsymlinksinpath()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/resolvingsymlinksinpath%28%29.json'
content_hash: 'sha256:a3cbb8c4401fa61e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# resolvingSymlinksInPath()

<sub>Instance Method</sub>

Resolves any symlinks in the path of a file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resolvingSymlinksInPath() -> URL
```

## Discussion

If the `isFileURL` is false, this method returns `self`.

## See Also

### Working with file URLs

- [isFileURL](isfileurl.md) — A Boolean that is true if the scheme is `file:`.
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean that is true if the URL path represents a directory.
- [withUnsafeFileSystemRepresentation(_:)](<withunsafefilesystemrepresentation(__).md>) — Passes the URL’s path in the file system representation to a closure.
- [resolveSymlinksInPath()](<resolvesymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [standardize()](<standardize().md>) — Standardizes the path of a file URL.
