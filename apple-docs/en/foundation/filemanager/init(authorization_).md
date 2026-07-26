---
title: 'init(authorization:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.14+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/init(authorization:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/init(authorization:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/init%28authorization%3A%29.json'
content_hash: 'sha256:9d0c0b12fa9b41bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# init(authorization:)

<sub>Initializer</sub>

Initializes a file manager object that is authorized to perform privileged file system operations.

<sub>macOS</sub>

```swift
convenience init(authorization: NSWorkspace.Authorization)
```

## See Also

### Creating a file manager

- [defaultManager](default.md) — The shared file manager object for the process.
