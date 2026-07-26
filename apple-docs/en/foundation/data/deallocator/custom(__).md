---
title: 'Data.Deallocator.custom(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/deallocator/custom(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/deallocator/custom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/deallocator/custom%28_%3A%29.json'
content_hash: 'sha256:399a63513e68feae'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Data](../../data.md) · [Deallocator](../deallocator.md)

# Data.Deallocator.custom(_:)

<sub>Case</sub>

A custom deallocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case custom((UnsafeMutableRawPointer, Int) -> Void)
```

## See Also

### Enumeration Cases

- [Data.Deallocator.free](free.md) — Use `free`.
- [Data.Deallocator.none](none.md) — Do nothing upon deallocation.
- [Data.Deallocator.unmap](unmap.md) — Use `munmap`.
- [Data.Deallocator.virtualMemory](virtualmemory.md)
