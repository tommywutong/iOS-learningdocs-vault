---
title: 'init(_:isDirectory:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（16.0 起废弃）, iPadOS 14.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 11.0+（13.0 起废弃）, tvOS 14.0+（16.0 起废弃）, watchOS 7.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/url/init(_:isdirectory:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(_:isdirectory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28_%3Aisdirectory%3A%29.json'
content_hash: 'sha256:4d1f3e0d3640df8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(_:isDirectory:)

<sub>Initializer</sub>

Creates a file URL that references the local file or directory at the file path you specify.

> [!warning] Deprecated
> Use init?(filePath:directoryHint:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
init?(_ path: FilePath, isDirectory: Bool)
```

## Parameters

- `path` — The location in the file system.

- `isDirectory` — A Boolean value that indicates whether the location is a directory.

## Discussion

> [!note] Note
> This method avoids file system I/O to determine if the path is to a directory. When you know that information, prefer this method to initializers without the parameter.

## See Also

### Creating a file URL from a file path

- [init(_:)](<init(__).md>) — Creates a file URL that references the local file or directory at the file path you specify. _(deprecated)_
- [FilePath](../../system/filepath.md) — Represents a location in the file system.
