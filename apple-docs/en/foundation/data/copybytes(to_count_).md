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
doc_path: '/documentation/foundation/data/copybytes(to:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/copybytes(to:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/copybytes%28to%3Acount%3A%29.json'
content_hash: 'sha256:6ead41045d450fbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# copyBytes(to:count:)

<sub>Instance Method</sub>

Copies the contents of the data to memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyBytes(to pointer: UnsafeMutablePointer<UInt8>, count: Int)
```

## Parameters

- `pointer` — A pointer to the buffer you wish to copy the bytes into.

- `count` — The number of bytes to copy.

## Discussion

> [!warning] Warning
> This method does not verify that the contents at pointer have enough space to hold `count` bytes.

## See Also

### Accessing Underlying Memory

- [withUnsafeBytes(_:)](<withunsafebytes(__).md>) — Accesses the raw bytes in the data’s buffer.
- [withUnsafeMutableBytes(_:)](<withunsafemutablebytes(__)-7ac1g.md>) — Mutates the raw bytes in the data’s buffer.
- [copyBytes(to:from:)](<copybytes(to_from_)-8qk4r.md>) — Copies a subset of the contents of the data to memory.
- [copyBytes(to:from:)](<copybytes(to_from_)-4o6zj.md>) — Copies the bytes in a range from the data into a buffer.
