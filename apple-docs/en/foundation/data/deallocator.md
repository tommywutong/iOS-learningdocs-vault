---
title: Data.Deallocator
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/data/deallocator
source_url: 'https://developer.apple.com/documentation/foundation/data/deallocator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/deallocator.json'
content_hash: 'sha256:1653efa0f5afee5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# Data.Deallocator

<sub>Enumeration</sub>

A deallocator you use to customize how the backing store is deallocated for data created with the no-copy initializer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Deallocator
```

## Topics

### Enumeration Cases

- [Data.Deallocator.custom(_:)](<deallocator/custom(__).md>) — A custom deallocator.
- [Data.Deallocator.free](deallocator/free.md) — Use `free`.
- [Data.Deallocator.none](deallocator/none.md) — Do nothing upon deallocation.
- [Data.Deallocator.unmap](deallocator/unmap.md) — Use `munmap`.
- [Data.Deallocator.virtualMemory](deallocator/virtualmemory.md)

## See Also

### Creating Data from Raw Memory

- [init(bytes:count:)](<init(bytes_count_).md>) — Creates data with copied memory content.
- [init(buffer:)](<init(buffer_)-75sng.md>) — Creates a data buffer with copied memory content using a buffer pointer.
- [init(buffer:)](<init(buffer_)-6xgv4.md>) — Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy:count:deallocator:)](<init(bytesnocopy_count_deallocator_).md>) — Creates a data buffer with memory content without copying the bytes.
