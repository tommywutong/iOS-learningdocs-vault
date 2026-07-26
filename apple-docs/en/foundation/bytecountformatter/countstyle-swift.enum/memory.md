---
title: ByteCountFormatter.CountStyle.memory
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/countstyle-swift.enum/memory
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/countstyle-swift.enum/memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/countstyle-swift.enum/memory.json'
content_hash: 'sha256:1780ee6875819009'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ByteCountFormatter](../../bytecountformatter.md) · [CountStyle](../countstyle-swift.enum.md)

# ByteCountFormatter.CountStyle.memory

<sub>Case</sub>

Specifies display of memory byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the binary style, but that may change over time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case memory
```

## See Also

### Constants

- [NSByteCountFormatterCountStyleFile](file.md) — Specifies display of file byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the decimal style, but that may change over time.
- [NSByteCountFormatterCountStyleDecimal](decimal.md) — Causes 1000 bytes to be shown as 1 KB. It is better to use [NSByteCountFormatterCountStyleFile](file.md) or [NSByteCountFormatterCountStyleMemory](memory.md) in most cases.
- [NSByteCountFormatterCountStyleBinary](binary.md) — Causes 1024 bytes to be shown as 1 KB. It is better to use [NSByteCountFormatterCountStyleFile](file.md) or [NSByteCountFormatterCountStyleMemory](memory.md) in most cases.
