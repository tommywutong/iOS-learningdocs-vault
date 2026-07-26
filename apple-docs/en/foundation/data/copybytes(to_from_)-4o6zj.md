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
doc_path: '/documentation/foundation/data/copybytes(to:from:)-4o6zj'
source_url: 'https://developer.apple.com/documentation/foundation/data/copybytes(to:from:)-4o6zj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/copybytes%28to%3Afrom%3A%29-4o6zj.json'
content_hash: 'sha256:60fb80d4235799f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# copyBytes(to:from:)

<sub>Instance Method</sub>

Copies the bytes in a range from the data into a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyBytes<DestinationType>(to buffer: UnsafeMutableBufferPointer<DestinationType>, from range: Range<Data.Index>? = nil) -> Int
```

## Parameters

- `buffer` — A buffer to copy the data into.

- `range` — A range in the data to copy into the buffer. If the range is empty, this function will return 0 without copying anything. If the range is nil, as much data as will fit into `buffer` is copied.

## Return Value

Number of bytes copied into the destination buffer.

## Discussion

If the count of the range is greater than `MemoryLayout<DestinationType>.stride * buffer.count` then only the first `N` bytes will be copied into the buffer.Precondition: The range must be within the bounds of the data. Otherwise `fatalError` is called.

## See Also

### Accessing Underlying Memory

- [withUnsafeBytes(_:)](<withunsafebytes(__).md>) — Accesses the raw bytes in the data’s buffer.
- [withUnsafeMutableBytes(_:)](<withunsafemutablebytes(__)-7ac1g.md>) — Mutates the raw bytes in the data’s buffer.
- [copyBytes(to:count:)](<copybytes(to_count_).md>) — Copies the contents of the data to memory.
- [copyBytes(to:from:)](<copybytes(to_from_)-8qk4r.md>) — Copies a subset of the contents of the data to memory.
