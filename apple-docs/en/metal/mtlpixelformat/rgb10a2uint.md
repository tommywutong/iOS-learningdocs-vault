---
title: MTLPixelFormat.rgb10a2Uint
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/rgb10a2uint
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/rgb10a2uint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/rgb10a2uint.json'
content_hash: 'sha256:df0a76a3308480bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.rgb10a2Uint

<sub>Case</sub>

A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rgb10a2Uint
```

## Discussion

Pixel data is stored in red, green, blue, and alpha order, from least significant bit to most significant bit.

![](../../../../attachments/1480c4a8ab5793367e5dc130522ae2d1/rgb10a2-layout-1@2x.png)

<sub>Bit layout diagram showing the pixel data storage arrangement of the rgb10a2Uint pixel format. The red component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the blue component is stored in bits 20 to 29, and the alpha component is stored in bits 30 to 31.</sub>

## See Also

### Packed 32-bit pixel formats

- [MTLPixelFormatBGR10A2Unorm](bgr10a2unorm.md) — A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.
- [MTLPixelFormatRGB10A2Unorm](rgb10a2unorm.md) — A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormatRG11B10Float](rg11b10float.md) — 32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.
- [MTLPixelFormatRGB9E5Float](rgb9e5float.md) — Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.
