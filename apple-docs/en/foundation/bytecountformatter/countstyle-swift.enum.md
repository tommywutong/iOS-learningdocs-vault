---
title: ByteCountFormatter.CountStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter/countstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/countstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/countstyle-swift.enum.json'
content_hash: 'sha256:3172b844ec263ef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# ByteCountFormatter.CountStyle

<sub>Enumeration</sub>

Specifies display of file or storage byte counts. The display style is platform specific.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CountStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSByteCountFormatterCountStyleFile](countstyle-swift.enum/file.md) — Specifies display of file byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the decimal style, but that may change over time.
- [NSByteCountFormatterCountStyleMemory](countstyle-swift.enum/memory.md) — Specifies display of memory byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the binary style, but that may change over time.
- [NSByteCountFormatterCountStyleDecimal](countstyle-swift.enum/decimal.md) — Causes 1000 bytes to be shown as 1 KB. It is better to use [NSByteCountFormatterCountStyleFile](countstyle-swift.enum/file.md) or [NSByteCountFormatterCountStyleMemory](countstyle-swift.enum/memory.md) in most cases.
- [NSByteCountFormatterCountStyleBinary](countstyle-swift.enum/binary.md) — Causes 1024 bytes to be shown as 1 KB. It is better to use [NSByteCountFormatterCountStyleFile](countstyle-swift.enum/file.md) or [NSByteCountFormatterCountStyleMemory](countstyle-swift.enum/memory.md) in most cases.

### Initializers

- [init(rawValue:)](<countstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [Units](units.md) — Specifies the units appropriate for the formatter to display. Specifying any units explicitly causes just those units to be used in showing the number.
