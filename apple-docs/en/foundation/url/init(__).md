---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（16.0 起废弃）, iPadOS 14.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 11.0+（13.0 起废弃）, tvOS 14.0+（16.0 起废弃）, watchOS 7.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/url/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28_%3A%29.json'
content_hash: 'sha256:889e1ad0f2377b40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(_:)

<sub>Initializer</sub>

Creates a file URL that references the local file or directory at the file path you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
init?(_ path: FilePath)
```

## Parameters

- `path` — The location in the file system.

## Discussion

This method may perform file system I/O to determine if the path is to a directory. If you know the path is to a directory, use [init(_:isDirectory:)](<init(__isdirectory_).md>) to avoid the file system I/O.

## See Also

### Creating a file URL from a file path

- [init(_:isDirectory:)](<init(__isdirectory_).md>) — Creates a file URL that references the local file or directory at the file path you specify. _(deprecated)_
- [FilePath](../../system/filepath.md) — Represents a location in the file system.
