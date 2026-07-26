---
title: 'init(bitmapRepresentation:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/init(bitmaprepresentation:)'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/init(bitmaprepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/init%28bitmaprepresentation%3A%29.json'
content_hash: 'sha256:b684cd76c972bf7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# init(bitmapRepresentation:)

<sub>Initializer</sub>

Initialize with a bitmap representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitmapRepresentation data: Data)
```

## Parameters

- `data` — The bitmap representation.

## Discussion

This method is useful for creating a character set object with data from a file or other external data source.
