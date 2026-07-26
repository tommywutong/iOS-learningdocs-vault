---
title: MTLPixelFormat.pvrtc_rgba_4bpp_srgb
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlpixelformat/pvrtc_rgba_4bpp_srgb
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgba_4bpp_srgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/pvrtc_rgba_4bpp_srgb.json'
content_hash: 'sha256:13937c14245b662e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.pvrtc_rgba_4bpp_srgb

<sub>Case</sub>

A compressed format that uses PVRTC compression and 4bpp for RGBA components with a conversion between sRGB and linear space.

> [!warning] Deprecated
> Use one of the other formats with `astc`/`ASTC`, `etc2`/`ETC2`, or `bc`/`BC` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case pvrtc_rgba_4bpp_srgb
```

## Discussion

The only texture types that support this format include:

- [MTLTextureType2D](../mtltexturetype/type2d.md)
- [MTLTextureType2DArray](../mtltexturetype/type2darray.md)
- [MTLTextureTypeCube](../mtltexturetype/typecube.md)

> [!note] Note
> The format doesn’t support subimages.

## See Also

### Compressed PVRTC pixel formats

- [MTLPixelFormatPVRTC_RGB_2BPP](pvrtc_rgb_2bpp.md) — A compressed format that uses PVRTC compression and 2bpp for RGB components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGB_2BPP_sRGB](pvrtc_rgb_2bpp_srgb.md) — A compressed format that uses PVRTC compression and 2bpp for RGB components with a conversion between sRGB and linear space. _(deprecated)_
- [MTLPixelFormatPVRTC_RGB_4BPP](pvrtc_rgb_4bpp.md) — A compressed format that uses PVRTC compression and 4bpp for RGB components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGB_4BPP_sRGB](pvrtc_rgb_4bpp_srgb.md) — A compressed format that uses PVRTC compression and 4bpp for RGB components with a conversion between sRGB and linear space. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_2BPP](pvrtc_rgba_2bpp.md) — A compressed format that uses PVRTC compression and 2bpp for RGBA components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_2BPP_sRGB](pvrtc_rgba_2bpp_srgb.md) — A compressed format that uses PVRTC compression and 2bpp for RGBA components with a conversion between sRGB and linear space. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_4BPP](pvrtc_rgba_4bpp.md) — A compressed format that uses PVRTC compression and 4bpp for RGBA components. _(deprecated)_
