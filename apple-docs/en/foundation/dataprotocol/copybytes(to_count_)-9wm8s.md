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
doc_path: '/documentation/foundation/dataprotocol/copybytes(to:count:)-9wm8s'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:count:)-9wm8s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/copybytes%28to%3Acount%3A%29-9wm8s.json'
content_hash: 'sha256:a85b5c9baefda13b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# copyBytes(to:count:)

<sub>Instance Method</sub>

Copies the provided number of bytes from the start of the type into a typed memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func copyBytes<DestinationType>(to ptr: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int
```

## Parameters

- `ptr` — A typed pointer to the buffer you want to copy the bytes into.

- `count` — The number of bytes to copy.

## Return Value

The number of bytes copied.
