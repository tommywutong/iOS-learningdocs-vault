---
title: 'init(buffer:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(buffer:)-6xgv4'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(buffer:)-6xgv4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28buffer%3A%29-6xgv4.json'
content_hash: 'sha256:cece2091f0c6db60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(buffer:)

<sub>Initializer</sub>

Creates a data buffer with copied memory content using a mutable buffer pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)
```

## Parameters

- `buffer` — A buffer pointer to copy. The size is calculated from `SourceType` and `buffer.count`.

## See Also

### Creating Populated Data

- [init()](<init().md>) — Creates an empty data buffer.
- [init(buffer:)](<init(buffer_)-75sng.md>) — Creates a data buffer with copied memory content using a buffer pointer.
- [init(bytes:count:)](<init(bytes_count_).md>) — Creates data with copied memory content.
- [init(bytesNoCopy:count:deallocator:)](<init(bytesnocopy_count_deallocator_).md>) — Creates a data buffer with memory content without copying the bytes.
- [init(capacity:)](<init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [init(count:)](<init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.
