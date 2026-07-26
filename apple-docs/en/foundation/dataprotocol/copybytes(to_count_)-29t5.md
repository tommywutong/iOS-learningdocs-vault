---
title: 'copyBytes(to:count:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dataprotocol/copybytes(to:count:)-29t5'
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:count:)-29t5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/copybytes%28to%3Acount%3A%29-29t5.json'
content_hash: 'sha256:159afe32ac4266e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# copyBytes(to:count:)

<sub>Instance Method</sub>

Copies the provided number of bytes from the start of the type into a raw memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int
```

## Parameters

- `to` — A  pointer to the raw memory buffer you want to copy the bytes into.

- `count` — The number of bytes to copy.

## Return Value

The number of bytes copied.

## Discussion

The following example copies the number of bytes that `count` identified from the beginning of the raw memory buffer into the provided raw memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.withUnsafeMutableBytes { destBufferPtr in
    let count = source.copyBytes(to: destBufferPtr, count: 2)
    // count == 2
}
// dest = [0x00, 0x01, 0xFF, 0xFF, 0xFF, 0xFF]
```

## Default Implementations

### DataProtocol Implementations

- [copyBytes(to:count:)](<copybytes(to_count_)-45x1l.md>) — Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [copyBytes(to:count:)](<copybytes(to_count_)-9wm8s.md>) — Copies the provided number of bytes from the start of the type into a typed memory buffer.

## See Also

### Copying Underlying Bytes

- [copyBytes(to:)](<copybytes(to_)-52wps.md>) — Copies the bytes of data from the type into a typed memory buffer.
- [copyBytes(to:)](<copybytes(to_)-3mk27.md>) — Copies the bytes of data from the type into a raw memory buffer.
- [copyBytes(to:count:)](<copybytes(to_count_)-6krsm.md>) — Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-1ol47.md>) — Copies a range of the bytes from the type into a typed memory buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-1y839.md>) — Copies a range of the bytes from the type into a raw memory buffer.
