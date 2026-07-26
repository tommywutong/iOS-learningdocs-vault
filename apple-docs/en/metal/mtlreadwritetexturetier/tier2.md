---
title: MTLReadWriteTextureTier.tier2
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlreadwritetexturetier/tier2
source_url: 'https://developer.apple.com/documentation/metal/mtlreadwritetexturetier/tier2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlreadwritetexturetier/tier2.json'
content_hash: 'sha256:1c4468d4c2ece256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLReadWriteTextureTier](../mtlreadwritetexturetier.md)

# MTLReadWriteTextureTier.tier2

<sub>Case</sub>

Indicates the system supports tier 2 read-write textures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case tier2
```

## Discussion

Tier 2 read-write textures support the following pixel formats (in addition to [MTLReadWriteTextureTier1](tier1.md)):

- [MTLPixelFormatRGBA32Float](../mtlpixelformat/rgba32float.md)
- [MTLPixelFormatRGBA32Uint](../mtlpixelformat/rgba32uint.md)
- [MTLPixelFormatRGBA32Sint](../mtlpixelformat/rgba32sint.md)
- [MTLPixelFormatRGBA16Float](../mtlpixelformat/rgba16float.md)
- [MTLPixelFormatRGBA16Uint](../mtlpixelformat/rgba16uint.md)
- [MTLPixelFormatRGBA16Sint](../mtlpixelformat/rgba16sint.md)
- [MTLPixelFormatRGBA8Unorm](../mtlpixelformat/rgba8unorm.md)
- [MTLPixelFormatRGBA8Uint](../mtlpixelformat/rgba8uint.md)
- [MTLPixelFormatRGBA8Sint](../mtlpixelformat/rgba8sint.md)
- [MTLPixelFormatR16Float](../mtlpixelformat/r16float.md)
- [MTLPixelFormatR16Uint](../mtlpixelformat/r16uint.md)
- [MTLPixelFormatR16Sint](../mtlpixelformat/r16sint.md)
- [MTLPixelFormatR8Unorm](../mtlpixelformat/r8unorm.md)
- [MTLPixelFormatR8Uint](../mtlpixelformat/r8uint.md)
- [MTLPixelFormatR8Sint](../mtlpixelformat/r8sint.md)

## See Also

### Enumeration cases

- [MTLReadWriteTextureTier1](tier1.md) — Indicates the system supports tier 1 read-write textures.
- [MTLReadWriteTextureTierNone](tiernone.md) — Indicates the system doesn’t support read-write textures.
