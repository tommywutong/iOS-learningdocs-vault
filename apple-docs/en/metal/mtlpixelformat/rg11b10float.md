---
title: MTLPixelFormat.rg11b10Float
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/rg11b10float
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/rg11b10float'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/rg11b10float.json'
content_hash: 'sha256:e276f5a71d96dd10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.rg11b10Float

<sub>Case</sub>

32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rg11b10Float
```

## Discussion

The components have no sign bit. The 10-bit float has 5 bits of mantissa and 5 bits of exponent. The 11-bit floats have 6 bits of mantissa and 5 bits of exponent.

## See Also

### Packed 32-bit pixel formats

- [MTLPixelFormatBGR10A2Unorm](bgr10a2unorm.md) — A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.
- [MTLPixelFormatRGB10A2Unorm](rgb10a2unorm.md) — A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormatRGB10A2Uint](rgb10a2uint.md) — A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormatRGB9E5Float](rgb9e5float.md) — Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.
