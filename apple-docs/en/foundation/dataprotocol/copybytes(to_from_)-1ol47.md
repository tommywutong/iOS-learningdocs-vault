---
title: 'copyBytes(to:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/copybytes(to:from:)-1ol47'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:from:)-1ol47'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/copybytes%28to%3Afrom%3A%29-1ol47.json'
content_hash: 'sha256:ffcad7ca9760b94a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# copyBytes(to:from:)

<sub>Instance Method</sub>

Copies a range of the bytes from the type into a typed memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int where R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `to` — A typed pointer to the buffer you want to copy the bytes into.

- `from` — The range of bytes to copy.

## Return Value

The number of bytes copied.

## Discussion

The following example copies the source bytes that the provided range identifies into the beginning of the specified typed memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.withUnsafeMutableBufferPointer { typedMemBuffer in
    source.copyBytes(to: typedMemBuffer, from: 1...2)
}
// dest = [0x01, 0x02, 0xFF, 0xFF, 0xFF, 0xFF]

```

## Default Implementations

### DataProtocol Implementations

- [copyBytes(to:from:)](<copybytes(to_from_)-2u470.md>) — Copies a range of the bytes from the type into a raw memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-44inx.md>) — Copies a range of the bytes from the type into a typed memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-9bgoo.md>) — Copies a range of the bytes from the type into a typed memory buffer.

## See Also

### Copying Underlying Bytes

- [copyBytes(to:)](<copybytes(to_)-52wps.md>) — Copies the bytes of data from the type into a typed memory buffer.
- [copyBytes(to:)](<copybytes(to_)-3mk27.md>) — Copies the bytes of data from the type into a raw memory buffer.
- [copyBytes(to:count:)](<copybytes(to_count_)-6krsm.md>) — Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [copyBytes(to:count:)](<copybytes(to_count_)-29t5.md>) — Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-1y839.md>) — Copies a range of the bytes from the type into a raw memory buffer.
