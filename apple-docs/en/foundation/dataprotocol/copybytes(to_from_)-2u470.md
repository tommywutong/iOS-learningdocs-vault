---
title: 'copyBytes(to:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/copybytes(to:from:)-2u470'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:from:)-2u470'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/copybytes%28to%3Afrom%3A%29-2u470.json'
content_hash: 'sha256:957b9722130943f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# copyBytes(to:from:)

<sub>Instance Method</sub>

Copies a range of the bytes from the type into a raw memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func copyBytes<R>(to ptr: UnsafeMutableRawBufferPointer, from range: R) -> Int where R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `ptr` — A pointer to the raw memory buffer you want to copy the bytes into.

- `range` — The range of bytes to copy.

## Return Value

The number of bytes copied.
