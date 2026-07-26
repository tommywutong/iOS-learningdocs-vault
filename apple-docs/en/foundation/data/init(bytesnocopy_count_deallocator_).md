---
title: 'init(bytesNoCopy:count:deallocator:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(bytesnocopy:count:deallocator:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(bytesnocopy:count:deallocator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28bytesnocopy%3Acount%3Adeallocator%3A%29.json'
content_hash: 'sha256:3d7bce7f6d69a74e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(bytesNoCopy:count:deallocator:)

<sub>Initializer</sub>

Creates a data buffer with memory content without copying the bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytesNoCopy bytes: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)
```

## Parameters

- `bytes` — A pointer to the bytes.

- `count` — The size of the bytes.

- `deallocator` — Specifies the mechanism to free the indicated buffer, or `.none`.

## Discussion

If the result is mutated and is not a unique reference, then the `Data` will still follow copy-on-write semantics. In this case, the copy will use its own deallocator. Therefore, it is usually best to only use this initializer when you either enforce immutability with `let` or ensure that no other references to the underlying data are formed.

## See Also

### Creating Populated Data

- [init()](<init().md>) — Creates an empty data buffer.
- [init(buffer:)](<init(buffer_)-75sng.md>) — Creates a data buffer with copied memory content using a buffer pointer.
- [init(buffer:)](<init(buffer_)-6xgv4.md>) — Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes:count:)](<init(bytes_count_).md>) — Creates data with copied memory content.
- [init(capacity:)](<init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [init(count:)](<init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.
