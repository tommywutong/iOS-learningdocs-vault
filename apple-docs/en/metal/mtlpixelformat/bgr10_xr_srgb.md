---
title: MTLPixelFormat.bgr10_xr_srgb
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat/bgr10_xr_srgb
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr_srgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat/bgr10_xr_srgb.json'
content_hash: 'sha256:01c051f8ae96d5dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPixelFormat](../mtlpixelformat.md)

# MTLPixelFormat.bgr10_xr_srgb

<sub>Case</sub>

A 32-bit extended-range pixel format with sRGB conversion and three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case bgr10_xr_srgb
```

## Discussion

Pixel components are stored in blue, green, and red order, from least significant bit to most significant bit. Bits 30 and 31 are padding, and their value is `0`.

![](../../../../attachments/8b8b5ef3d46f2f39a29d9230a1a67a11/bgr10-xr-layout-1@2x.png)

<sub>Bit layout diagram showing the pixel data storage arrangement of the bgr10_xr_srgb pixel format. The blue component is stored in bits 0 to 9, the green component is stored in bits 10 to 19, the red component is stored in bits 20 to 29, and bits 30 to 31 are used as padding.</sub>

The blue, green, and red components are gamma encoded, and their values range from `-0.5271` to `1.66894`, before gamma expansion.

In order to determine a component’s value as a shader float:

- When reading a pixel, first apply the linear encoding `(xr10_value - 384) / 510.0f` and then the sRGB transform.
- When writing a pixel, first apply the sRGB transform and then the linear encoding `shader_float = (xr10_value - 384) / 510.0f`.

To display wide color values on devices with wide color displays, you set this pixel format on the [colorPixelFormat](../../metalkit/mtkview/colorpixelformat.md) property of an [MTKView](../../metalkit/mtkview.md) or the [pixelFormat](../../quartzcore/cametallayer/pixelformat.md) property of a [CAMetalLayer](../../quartzcore/cametallayer.md). Also provide an extended sRGB color space.

> [!note] Note
> Only devices with a wide color display can display color values outside the `[0.0, 1.0]` range; all other devices clamp color values to the `[0.0, 1.0]` range.

## See Also

### Extended range and wide color pixel formats

- [MTLPixelFormatBGRA10_XR](bgra10_xr.md) — A 64-bit extended-range pixel format with four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormatBGRA10_XR_sRGB](bgra10_xr_srgb.md) — A 64-bit extended-range pixel format with sRGB conversion and four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormatBGR10_XR](bgr10_xr.md) — A 32-bit extended-range pixel format with three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.
