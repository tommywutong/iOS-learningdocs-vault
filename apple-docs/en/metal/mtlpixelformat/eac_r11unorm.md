---
title: MTLPixelFormat.eac_r11Unorm
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/eac_r11unorm
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/eac_r11unorm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/eac_r11unorm.json'
content_hash: 'sha256:cc76a3da56799424'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.eac_r11Unorm

<sub>Case</sub>

Compressed format using EAC compression with one normalized unsigned integer component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case eac_r11Unorm
```

## Discussion

Only [MTLTextureType2D](../mtltexturetype/type2d.md), [MTLTextureType2DArray](../mtltexturetype/type2darray.md), and [MTLTextureTypeCube](../mtltexturetype/typecube.md) textures are supported.

## See Also

### Compressed EAC/ETC pixel formats

- [MTLPixelFormatEAC_R11Snorm](eac_r11snorm.md) — Compressed format using EAC compression with one normalized signed integer component.
- [MTLPixelFormatEAC_RG11Unorm](eac_rg11unorm.md) — Compressed format using EAC compression with two normalized unsigned integer components.
- [MTLPixelFormatEAC_RG11Snorm](eac_rg11snorm.md) — Compressed format using EAC compression with two normalized signed integer components.
- [MTLPixelFormatEAC_RGBA8](eac_rgba8.md) — Compressed format using EAC compression with four 8-bit components.
- [MTLPixelFormatEAC_RGBA8_sRGB](eac_rgba8_srgb.md) — Compressed format using EAC compression with four 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormatETC2_RGB8](etc2_rgb8.md) — Compressed format using ETC2 compression with three 8-bit components.
- [MTLPixelFormatETC2_RGB8_sRGB](etc2_rgb8_srgb.md) — Compressed format using ETC2 compression with three 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormatETC2_RGB8A1](etc2_rgb8a1.md) — Compressed format using ETC2 compression with four 8-bit components.
- [MTLPixelFormatETC2_RGB8A1_sRGB](etc2_rgb8a1_srgb.md) — Compressed format using ETC2 compression with four 8-bit components with conversion between sRGB and linear space.
