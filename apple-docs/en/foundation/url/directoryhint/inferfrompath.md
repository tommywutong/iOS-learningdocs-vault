---
title: URL.DirectoryHint.inferFromPath
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/directoryhint/inferfrompath
source_url: 'https://developer.apple.com/documentation/foundation/url/directoryhint/inferfrompath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/directoryhint/inferfrompath.json'
content_hash: 'sha256:a4a24eb407a128bd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [DirectoryHint](../directoryhint.md)

# URL.DirectoryHint.inferFromPath

<sub>Case</sub>

A hint that directs a URL call to infer whether a path references a directory based on whether it has a trailing slash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case inferFromPath
```

## See Also

### Hints

- [URL.DirectoryHint.isDirectory](isdirectory.md) — A hint that specifies that a given path is a directory.
- [URL.DirectoryHint.notDirectory](notdirectory.md) — A hint that specifies that a given path isn’t a directory.
- [URL.DirectoryHint.checkFileSystem](checkfilesystem.md) — A hint that directs a URL call to consult the file system to determine whether the path references a directory.
