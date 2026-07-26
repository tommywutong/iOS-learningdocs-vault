---
title: CFByteOrder
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbyteorder
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbyteorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbyteorder.json'
content_hash: 'sha256:30f323538bfce191'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFByteOrder

<sub>Type Alias</sub>

Flags that identify byte order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFByteOrder = CFIndex
```

## Topics

### Constants

- [CFByteOrderUnknown](cfbyteorderunknown.md) — The byte order is unknown.
- [CFByteOrderLittleEndian](cfbyteorderlittleendian.md) — Multi-byte values are stored with the least-significant bytes stored first. Pentium CPUs are little endian.
- [CFByteOrderBigEndian](cfbyteorderbigendian.md) — Multi-byte values are stored with the most-significant bytes stored first. PowerPC CPUs are big endian.
