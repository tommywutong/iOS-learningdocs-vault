---
title: MTLReadWriteTextureTier.tier1
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlreadwritetexturetier/tier1
source_url: 'https://developer.apple.com/documentation/metal/mtlreadwritetexturetier/tier1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlreadwritetexturetier/tier1.json'
content_hash: 'sha256:a66b03899f4092cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLReadWriteTextureTier](../mtlreadwritetexturetier.md)

# MTLReadWriteTextureTier.tier1

<sub>Case</sub>

Indicates the system supports tier 1 read-write textures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case tier1
```

## Discussion

Tier 1 read-write textures support the following pixel formats:

- [MTLPixelFormatR32Float](../mtlpixelformat/r32float.md)
- [MTLPixelFormatR32Uint](../mtlpixelformat/r32uint.md)
- [MTLPixelFormatR32Sint](../mtlpixelformat/r32sint.md)

## See Also

### Enumeration cases

- [MTLReadWriteTextureTier2](tier2.md) — Indicates the system supports tier 2 read-write textures.
- [MTLReadWriteTextureTierNone](tiernone.md) — Indicates the system doesn’t support read-write textures.
