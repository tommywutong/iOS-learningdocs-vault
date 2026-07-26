---
title: 'init(bytes:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(bytes:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(bytes:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28bytes%3Acount%3A%29.json'
content_hash: 'sha256:2fbbba834648c36f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(bytes:count:)

<sub>Initializer</sub>

Creates data with copied memory content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytes: UnsafeRawPointer, count: Int)
```

## Parameters

- `bytes` — A pointer to the memory to copy.

- `count` — The number of bytes to copy.

## See Also

### Creating Populated Data

- [init()](<init().md>) — Creates an empty data buffer.
- [init(buffer:)](<init(buffer_)-75sng.md>) — Creates a data buffer with copied memory content using a buffer pointer.
- [init(buffer:)](<init(buffer_)-6xgv4.md>) — Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy:count:deallocator:)](<init(bytesnocopy_count_deallocator_).md>) — Creates a data buffer with memory content without copying the bytes.
- [init(capacity:)](<init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [init(count:)](<init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.
