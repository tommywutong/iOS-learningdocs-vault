---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/default
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/default.json'
content_hash: 'sha256:e182509431b68f42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# default

<sub>Type Property</sub>

The shared file manager object for the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: FileManager { get }
```

## Discussion

This method always represents the same file manager object. If you plan to use a delegate with the file manager to receive notifications about the completion of file-based operations, you should create a new instance of [FileManager](../filemanager.md) rather than using the shared object.

## See Also

### Creating a file manager

- [+ fileManagerWithAuthorization:](<init(authorization_).md>) — Initializes a file manager object that is authorized to perform privileged file system operations.
