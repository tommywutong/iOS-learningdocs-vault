---
title: 'resetBytes(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/mutabledataprotocol/resetbytes(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/mutabledataprotocol/resetbytes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/mutabledataprotocol/resetbytes%28in%3A%29.json'
content_hash: 'sha256:c488b04e4ed1c4d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MutableDataProtocol](../mutabledataprotocol.md)

# resetBytes(in:)

<sub>Instance Method</sub>

Replaces the contents of the data buffer with zeros for the provided range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func resetBytes<R>(in range: R) where R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `range` — The range of bytes to replace with zeros.

## Discussion

The following example sets the bytes to zero for the bytes identified by the provided range:

```swift
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.resetBytes(in: 1...3)
// dest = [0xFF, 0x00, 0x00, 0x00, 0xFF, 0xFF]
```

## Default Implementations

### MutableDataProtocol Implementations

- [resetBytes(in:)](<resetbytes(in_)-9ix6g.md>) — Replaces the contents of the data buffer with zeros for the provided range.
