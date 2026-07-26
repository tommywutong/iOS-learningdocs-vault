---
title: 'copyBytes(to:count:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/copybytes(to:count:)-45x1l'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:count:)-45x1l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/copybytes%28to%3Acount%3A%29-45x1l.json'
content_hash: 'sha256:7f109a1414e8a73d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# copyBytes(to:count:)

<sub>Instance Method</sub>

Copies the provided number of bytes from the start of the type into a raw memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func copyBytes(to ptr: UnsafeMutableRawBufferPointer, count: Int) -> Int
```

## Parameters

- `ptr` — A pointer to the raw memory buffer you want to copy the bytes into.

- `count` — The number of bytes to copy.

## Return Value

The number of bytes copied.
