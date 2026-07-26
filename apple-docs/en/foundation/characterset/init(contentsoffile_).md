---
title: 'init(contentsOfFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:1f41b767ed0c04bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Initialize with the contents of a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOfFile file: String)
```

## Parameters

- `file` — The file to read.

## Discussion

Returns `nil` if there was an error reading the file.
