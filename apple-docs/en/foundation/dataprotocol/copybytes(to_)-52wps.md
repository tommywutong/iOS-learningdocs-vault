---
title: 'copyBytes(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/copybytes(to:)-52wps'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:)-52wps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/copybytes%28to%3A%29-52wps.json'
content_hash: 'sha256:44ade079201ed890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# copyBytes(to:)

<sub>Instance Method</sub>

Copies the bytes of data from the type into a typed memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func copyBytes<DestinationType>(to ptr: UnsafeMutableBufferPointer<DestinationType>) -> Int
```

## Parameters

- `ptr` — A typed pointer to the buffer you want to copy the bytes into.

## Return Value

The number of bytes copied.

## Discussion

The following example copies the bytes from a typed memory buffer into the provided typed memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.withUnsafeMutableBufferPointer { typedMemBuffer in
    let count = source.copyBytes(to: typedMemBuffer)
    // count == 3
}
// dest = [0x00, 0x01, 0x02, 0xFF, 0xFF, 0xFF]
```

## See Also

### Copying Underlying Bytes

- [copyBytes(to:)](<copybytes(to_)-3mk27.md>) — Copies the bytes of data from the type into a raw memory buffer.
- [copyBytes(to:count:)](<copybytes(to_count_)-6krsm.md>) — Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [copyBytes(to:count:)](<copybytes(to_count_)-29t5.md>) — Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-1ol47.md>) — Copies a range of the bytes from the type into a typed memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-1y839.md>) — Copies a range of the bytes from the type into a raw memory buffer.
