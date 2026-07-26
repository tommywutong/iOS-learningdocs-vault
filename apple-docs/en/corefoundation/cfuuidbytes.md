---
title: CFUUIDBytes
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfuuidbytes
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuidbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuidbytes.json'
content_hash: 'sha256:3ea706a42d18d9ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUIDBytes

<sub>Structure</sub>

A 128-bit struct that represents a UUID as raw bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFUUIDBytes
```

## Overview

This structure can be obtained from a CFUUID object using the [CFUUIDGetUUIDBytes](<cfuuidgetuuidbytes(__).md>) function. This structure can be passed to functions that expect a raw UUID.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfuuidbytes/init().md>)
- [init(byte0:byte1:byte2:byte3:byte4:byte5:byte6:byte7:byte8:byte9:byte10:byte11:byte12:byte13:byte14:byte15:)](<cfuuidbytes/init(byte0_byte1_byte2_byte3_byte4_byte5_byte6_byte7_byte8_byte9_byte10_byte11_byte12_byte13_byte14_byte15_).md>)

### Instance Properties

- [byte0](cfuuidbytes/byte0.md) — The first byte.
- [byte1](cfuuidbytes/byte1.md) — The second byte.
- [byte10](cfuuidbytes/byte10.md) — The eleventh byte.
- [byte11](cfuuidbytes/byte11.md) — The twelfth byte.
- [byte12](cfuuidbytes/byte12.md) — The thirteenth byte.
- [byte13](cfuuidbytes/byte13.md) — The fourteenth byte.
- [byte14](cfuuidbytes/byte14.md) — The fifteenth byte.
- [byte15](cfuuidbytes/byte15.md) — The sixteenth byte.
- [byte2](cfuuidbytes/byte2.md) — The third byte.
- [byte3](cfuuidbytes/byte3.md) — The fourth byte.
- [byte4](cfuuidbytes/byte4.md) — The fifth byte.
- [byte5](cfuuidbytes/byte5.md) — The sixth byte.
- [byte6](cfuuidbytes/byte6.md) — The seventh byte.
- [byte7](cfuuidbytes/byte7.md) — The eighth byte.
- [byte8](cfuuidbytes/byte8.md) — The ninth byte.
- [byte9](cfuuidbytes/byte9.md) — The tenth byte.
