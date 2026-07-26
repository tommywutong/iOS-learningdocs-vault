---
title: MTLPixelFormat
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpixelformat
source_url: 'https://developer.apple.com/documentation/metal/mtlpixelformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpixelformat.json'
content_hash: 'sha256:487dd9a20c4f0c47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPixelFormat

<sub>Enumeration</sub>

The data formats that describe the organization and characteristics of individual pixels in a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLPixelFormat
```

## Overview

There are three varieties of pixel formats: ordinary, packed, and compressed. For ordinary and packed formats, the name of the pixel format specifies the order of components (such as `R`, `RG`, `RGB`, `RGBA`, `BGRA`), bits per component (such as `8`, `16`, `32`), and data type for the component (such as `Float`, `Sint`, `Snorm`, `Uint`, `Unorm`). If the pixel format name has the `_sRGB` suffix, then reading and writing pixel data applies sRGB gamma compression and decompression. The alpha component of sRGB pixel formats is always treated as a linear value. For compressed formats, the name of the pixel format specifies a compression family (such as `ASTC`, `BC`, `EAC`, `ETC2`, `PVRTC`).

> [!note] Note
> Pixel format availability and capabilities vary by feature set. See [Pixel Format Capabilities](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for more information.

### Storage characteristics

The number and size of each pixel component determines the storage size of each pixel format. For example, the storage size of [MTLPixelFormatBGRA8Unorm](mtlpixelformat/bgra8unorm.md) is 32 bits (four 8-bit components) and the storage size of [MTLPixelFormatBGR5A1Unorm](mtlpixelformat/bgr5a1unorm.md) is 16 bits (three 5-bit components and one 1-bit component).

For normalized signed integer formats (`Snorm`), values in the range `[-1.0, 1.0]` map to `[MIN_INT, MAX_INT]`, where `MIN_INT` is the most negative integer and `MAX_INT` is the most positive integer for the number of bits in the storage size. Positive values and zero distribute uniformly in the range `[0.0, 1.0]`, and negative integer values greater than `(MIN_INT + 1)` distribute uniformly in the range `(-1.0, 0.0)`.

> [!important] Important
> For `Snorm` formats, the values `MIN_INT` and `(MIN_INT + 1)` both map to `-1.0`.

For normalized unsigned integer formats (`Unorm`), values in the range `[0.0, 1.0]` are uniformly mapped to `[0, MAX_UINT]`, where `MAX_UINT` is the largest unsigned integer for the number of bits in the storage size.

Metal stores format data in little-endian byte order, with the least-significant byte at the lowest memory address. For formats with components that are themselves byte-aligned and more than one byte, Metal also stores each component in little-endian byte order.

See Table 7.7 in the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) (PDF) for details on pixel format normalization.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Ordinary 8-bit pixel formats

- [MTLPixelFormatA8Unorm](mtlpixelformat/a8unorm.md) — Ordinary format with one 8-bit normalized unsigned integer component.
- [MTLPixelFormatR8Unorm](mtlpixelformat/r8unorm.md) — Ordinary format with one 8-bit normalized unsigned integer component.
- [MTLPixelFormatR8Unorm_sRGB](mtlpixelformat/r8unorm_srgb.md) — Ordinary format with one 8-bit normalized unsigned integer component with conversion between sRGB and linear space.
- [MTLPixelFormatR8Snorm](mtlpixelformat/r8snorm.md) — Ordinary format with one 8-bit normalized signed integer component.
- [MTLPixelFormatR8Uint](mtlpixelformat/r8uint.md) — Ordinary format with one 8-bit unsigned integer component.
- [MTLPixelFormatR8Sint](mtlpixelformat/r8sint.md) — Ordinary format with one 8-bit signed integer component.

### Ordinary 16-bit pixel formats

- [MTLPixelFormatR16Unorm](mtlpixelformat/r16unorm.md) — Ordinary format with one 16-bit normalized unsigned integer component.
- [MTLPixelFormatR16Snorm](mtlpixelformat/r16snorm.md) — Ordinary format with one 16-bit normalized signed integer component.
- [MTLPixelFormatR16Uint](mtlpixelformat/r16uint.md) — Ordinary format with one 16-bit unsigned integer component.
- [MTLPixelFormatR16Sint](mtlpixelformat/r16sint.md) — Ordinary format with one 16-bit signed integer component.
- [MTLPixelFormatR16Float](mtlpixelformat/r16float.md) — Ordinary format with one 16-bit floating-point component.
- [MTLPixelFormatRG8Unorm](mtlpixelformat/rg8unorm.md) — Ordinary format with two 8-bit normalized unsigned integer components.
- [MTLPixelFormatRG8Unorm_sRGB](mtlpixelformat/rg8unorm_srgb.md) — Ordinary format with two 8-bit normalized unsigned integer components with conversion between sRGB and linear space.
- [MTLPixelFormatRG8Snorm](mtlpixelformat/rg8snorm.md) — Ordinary format with two 8-bit normalized signed integer components.
- [MTLPixelFormatRG8Uint](mtlpixelformat/rg8uint.md) — Ordinary format with two 8-bit unsigned integer components.
- [MTLPixelFormatRG8Sint](mtlpixelformat/rg8sint.md) — Ordinary format with two 8-bit signed integer components.

### Packed 16-bit pixel formats

- [MTLPixelFormatB5G6R5Unorm](mtlpixelformat/b5g6r5unorm.md) — Packed 16-bit format with normalized unsigned integer color components: 5 bits for blue, 6 bits for green, 5 bits for red, packed into 16 bits.
- [MTLPixelFormatA1BGR5Unorm](mtlpixelformat/a1bgr5unorm.md) — Packed 16-bit format with normalized unsigned integer color components: 5 bits each for BGR and 1 for alpha, packed into 16 bits.
- [MTLPixelFormatABGR4Unorm](mtlpixelformat/abgr4unorm.md) — Packed 16-bit format with normalized unsigned integer color components: 4 bits each for ABGR, packed into 16 bits.
- [MTLPixelFormatBGR5A1Unorm](mtlpixelformat/bgr5a1unorm.md) — Packed 16-bit format with normalized unsigned integer color components: 5 bits each for BGR and 1 for alpha, packed into 16 bits.

### Ordinary 32-bit pixel formats

- [MTLPixelFormatR32Uint](mtlpixelformat/r32uint.md) — Ordinary format with one 32-bit unsigned integer component.
- [MTLPixelFormatR32Sint](mtlpixelformat/r32sint.md) — Ordinary format with one 32-bit signed integer component.
- [MTLPixelFormatR32Float](mtlpixelformat/r32float.md) — Ordinary format with one 32-bit floating-point component.
- [MTLPixelFormatRG16Unorm](mtlpixelformat/rg16unorm.md) — Ordinary format with two 16-bit normalized unsigned integer components.
- [MTLPixelFormatRG16Snorm](mtlpixelformat/rg16snorm.md) — Ordinary format with two 16-bit normalized signed integer components.
- [MTLPixelFormatRG16Uint](mtlpixelformat/rg16uint.md) — Ordinary format with two 16-bit unsigned integer components.
- [MTLPixelFormatRG16Sint](mtlpixelformat/rg16sint.md) — Ordinary format with two 16-bit signed integer components.
- [MTLPixelFormatRG16Float](mtlpixelformat/rg16float.md) — Ordinary format with two 16-bit floating-point components.
- [MTLPixelFormatRGBA8Unorm](mtlpixelformat/rgba8unorm.md) — Ordinary format with four 8-bit normalized unsigned integer components in RGBA order.
- [MTLPixelFormatRGBA8Unorm_sRGB](mtlpixelformat/rgba8unorm_srgb.md) — Ordinary format with four 8-bit normalized unsigned integer components in RGBA order with conversion between sRGB and linear space.
- [MTLPixelFormatRGBA8Snorm](mtlpixelformat/rgba8snorm.md) — Ordinary format with four 8-bit normalized signed integer components in RGBA order.
- [MTLPixelFormatRGBA8Uint](mtlpixelformat/rgba8uint.md) — Ordinary format with four 8-bit unsigned integer components in RGBA order.
- [MTLPixelFormatRGBA8Sint](mtlpixelformat/rgba8sint.md) — Ordinary format with four 8-bit signed integer components in RGBA order.
- [MTLPixelFormatBGRA8Unorm](mtlpixelformat/bgra8unorm.md) — Ordinary format with four 8-bit normalized unsigned integer components in BGRA order.
- [MTLPixelFormatBGRA8Unorm_sRGB](mtlpixelformat/bgra8unorm_srgb.md) — Ordinary format with four 8-bit normalized unsigned integer components in BGRA order with conversion between sRGB and linear space.

### Packed 32-bit pixel formats

- [MTLPixelFormatBGR10A2Unorm](mtlpixelformat/bgr10a2unorm.md) — A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit blue, 10-bit green, 10-bit red, and 2-bit alpha.
- [MTLPixelFormatRGB10A2Unorm](mtlpixelformat/rgb10a2unorm.md) — A 32-bit packed pixel format with four normalized unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormatRGB10A2Uint](mtlpixelformat/rgb10a2uint.md) — A 32-bit packed pixel format with four unsigned integer components: 10-bit red, 10-bit green, 10-bit blue, and 2-bit alpha.
- [MTLPixelFormatRG11B10Float](mtlpixelformat/rg11b10float.md) — 32-bit format with floating-point color components, 11 bits each for red and green and 10 bits for blue.
- [MTLPixelFormatRGB9E5Float](mtlpixelformat/rgb9e5float.md) — Packed 32-bit format with floating-point color components: 9 bits each for RGB and 5 bits for an exponent shared by RGB, packed into 32 bits.

### Ordinary 64-bit pixel formats

- [MTLPixelFormatRG32Uint](mtlpixelformat/rg32uint.md) — Ordinary format with two 32-bit unsigned integer components.
- [MTLPixelFormatRG32Sint](mtlpixelformat/rg32sint.md) — Ordinary format with two 32-bit signed integer components.
- [MTLPixelFormatRG32Float](mtlpixelformat/rg32float.md) — Ordinary format with two 32-bit floating-point components.
- [MTLPixelFormatRGBA16Unorm](mtlpixelformat/rgba16unorm.md) — Ordinary format with four 16-bit normalized unsigned integer components in RGBA order.
- [MTLPixelFormatRGBA16Snorm](mtlpixelformat/rgba16snorm.md) — Ordinary format with four 16-bit normalized signed integer components in RGBA order.
- [MTLPixelFormatRGBA16Uint](mtlpixelformat/rgba16uint.md) — Ordinary format with four 16-bit unsigned integer components in RGBA order.
- [MTLPixelFormatRGBA16Sint](mtlpixelformat/rgba16sint.md) — Ordinary format with four 16-bit signed integer components in RGBA order.
- [MTLPixelFormatRGBA16Float](mtlpixelformat/rgba16float.md) — Ordinary format with four 16-bit floating-point components in RGBA order.

### Ordinary 128-bit pixel formats

- [MTLPixelFormatRGBA32Uint](mtlpixelformat/rgba32uint.md) — Ordinary format with four 32-bit unsigned integer components in RGBA order.
- [MTLPixelFormatRGBA32Sint](mtlpixelformat/rgba32sint.md) — Ordinary format with four 32-bit signed integer components in RGBA order.
- [MTLPixelFormatRGBA32Float](mtlpixelformat/rgba32float.md) — Ordinary format with four 32-bit floating-point components in RGBA order.

### Compressed PVRTC pixel formats

- [MTLPixelFormatPVRTC_RGB_2BPP](mtlpixelformat/pvrtc_rgb_2bpp.md) — A compressed format that uses PVRTC compression and 2bpp for RGB components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGB_2BPP_sRGB](mtlpixelformat/pvrtc_rgb_2bpp_srgb.md) — A compressed format that uses PVRTC compression and 2bpp for RGB components with a conversion between sRGB and linear space. _(deprecated)_
- [MTLPixelFormatPVRTC_RGB_4BPP](mtlpixelformat/pvrtc_rgb_4bpp.md) — A compressed format that uses PVRTC compression and 4bpp for RGB components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGB_4BPP_sRGB](mtlpixelformat/pvrtc_rgb_4bpp_srgb.md) — A compressed format that uses PVRTC compression and 4bpp for RGB components with a conversion between sRGB and linear space. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_2BPP](mtlpixelformat/pvrtc_rgba_2bpp.md) — A compressed format that uses PVRTC compression and 2bpp for RGBA components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_2BPP_sRGB](mtlpixelformat/pvrtc_rgba_2bpp_srgb.md) — A compressed format that uses PVRTC compression and 2bpp for RGBA components with a conversion between sRGB and linear space. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_4BPP](mtlpixelformat/pvrtc_rgba_4bpp.md) — A compressed format that uses PVRTC compression and 4bpp for RGBA components. _(deprecated)_
- [MTLPixelFormatPVRTC_RGBA_4BPP_sRGB](mtlpixelformat/pvrtc_rgba_4bpp_srgb.md) — A compressed format that uses PVRTC compression and 4bpp for RGBA components with a conversion between sRGB and linear space. _(deprecated)_

### Compressed EAC/ETC pixel formats

- [MTLPixelFormatEAC_R11Unorm](mtlpixelformat/eac_r11unorm.md) — Compressed format using EAC compression with one normalized unsigned integer component.
- [MTLPixelFormatEAC_R11Snorm](mtlpixelformat/eac_r11snorm.md) — Compressed format using EAC compression with one normalized signed integer component.
- [MTLPixelFormatEAC_RG11Unorm](mtlpixelformat/eac_rg11unorm.md) — Compressed format using EAC compression with two normalized unsigned integer components.
- [MTLPixelFormatEAC_RG11Snorm](mtlpixelformat/eac_rg11snorm.md) — Compressed format using EAC compression with two normalized signed integer components.
- [MTLPixelFormatEAC_RGBA8](mtlpixelformat/eac_rgba8.md) — Compressed format using EAC compression with four 8-bit components.
- [MTLPixelFormatEAC_RGBA8_sRGB](mtlpixelformat/eac_rgba8_srgb.md) — Compressed format using EAC compression with four 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormatETC2_RGB8](mtlpixelformat/etc2_rgb8.md) — Compressed format using ETC2 compression with three 8-bit components.
- [MTLPixelFormatETC2_RGB8_sRGB](mtlpixelformat/etc2_rgb8_srgb.md) — Compressed format using ETC2 compression with three 8-bit components with conversion between sRGB and linear space.
- [MTLPixelFormatETC2_RGB8A1](mtlpixelformat/etc2_rgb8a1.md) — Compressed format using ETC2 compression with four 8-bit components.
- [MTLPixelFormatETC2_RGB8A1_sRGB](mtlpixelformat/etc2_rgb8a1_srgb.md) — Compressed format using ETC2 compression with four 8-bit components with conversion between sRGB and linear space.

### Compressed ASTC pixel formats

- [MTLPixelFormatASTC_4x4_sRGB](mtlpixelformat/astc_4x4_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 4, and a block height of 4.
- [MTLPixelFormatASTC_5x4_sRGB](mtlpixelformat/astc_5x4_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 5, and a block height of 4.
- [MTLPixelFormatASTC_5x5_sRGB](mtlpixelformat/astc_5x5_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 5, and a block height of 5.
- [MTLPixelFormatASTC_6x5_sRGB](mtlpixelformat/astc_6x5_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 6, and a block height of 5.
- [MTLPixelFormatASTC_6x6_sRGB](mtlpixelformat/astc_6x6_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 6, and a block height of 6.
- [MTLPixelFormatASTC_8x5_sRGB](mtlpixelformat/astc_8x5_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 8, and a block height of 5.
- [MTLPixelFormatASTC_8x6_sRGB](mtlpixelformat/astc_8x6_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 8, and a block height of 6.
- [MTLPixelFormatASTC_8x8_sRGB](mtlpixelformat/astc_8x8_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 8, and a block height of 8.
- [MTLPixelFormatASTC_10x5_sRGB](mtlpixelformat/astc_10x5_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 5.
- [MTLPixelFormatASTC_10x6_sRGB](mtlpixelformat/astc_10x6_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 6.
- [MTLPixelFormatASTC_10x8_sRGB](mtlpixelformat/astc_10x8_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 8.
- [MTLPixelFormatASTC_10x10_sRGB](mtlpixelformat/astc_10x10_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 10, and a block height of 10.
- [MTLPixelFormatASTC_12x10_sRGB](mtlpixelformat/astc_12x10_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 12, and a block height of 10.
- [MTLPixelFormatASTC_12x12_sRGB](mtlpixelformat/astc_12x12_srgb.md) — ASTC-compressed format with low-dynamic-range content, conversion between sRGB and linear space, a block width of 12, and a block height of 12.
- [MTLPixelFormatASTC_4x4_LDR](mtlpixelformat/astc_4x4_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 4, and a block height of 4.
- [MTLPixelFormatASTC_5x4_LDR](mtlpixelformat/astc_5x4_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 5, and a block height of 4.
- [MTLPixelFormatASTC_5x5_LDR](mtlpixelformat/astc_5x5_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 5, and a block height of 5.
- [MTLPixelFormatASTC_6x5_LDR](mtlpixelformat/astc_6x5_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 6, and a block height of 5.
- [MTLPixelFormatASTC_6x6_LDR](mtlpixelformat/astc_6x6_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 6, and a block height of 6.
- [MTLPixelFormatASTC_8x5_LDR](mtlpixelformat/astc_8x5_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 8, and a block height of 5.
- [MTLPixelFormatASTC_8x6_LDR](mtlpixelformat/astc_8x6_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 8, and a block height of 6.
- [MTLPixelFormatASTC_8x8_LDR](mtlpixelformat/astc_8x8_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 8, and a block height of 8.
- [MTLPixelFormatASTC_10x5_LDR](mtlpixelformat/astc_10x5_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 5.
- [MTLPixelFormatASTC_10x6_LDR](mtlpixelformat/astc_10x6_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 6.
- [MTLPixelFormatASTC_10x8_LDR](mtlpixelformat/astc_10x8_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 8.
- [MTLPixelFormatASTC_10x10_LDR](mtlpixelformat/astc_10x10_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 10, and a block height of 10.
- [MTLPixelFormatASTC_12x10_LDR](mtlpixelformat/astc_12x10_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 12, and a block height of 10.
- [MTLPixelFormatASTC_12x12_LDR](mtlpixelformat/astc_12x12_ldr.md) — ASTC-compressed format with low-dynamic-range content, a block width of 12, and a block height of 12.
- [MTLPixelFormatASTC_4x4_HDR](mtlpixelformat/astc_4x4_hdr.md) — ASTC-compressed format with high-dynamic-range content, a block width of 4, and a block height of 4.
- [MTLPixelFormatASTC_5x4_HDR](mtlpixelformat/astc_5x4_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 5, and a block height of 4.
- [MTLPixelFormatASTC_5x5_HDR](mtlpixelformat/astc_5x5_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 5, and a block height of 5.
- [MTLPixelFormatASTC_6x5_HDR](mtlpixelformat/astc_6x5_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 6, and a block height of 5.
- [MTLPixelFormatASTC_6x6_HDR](mtlpixelformat/astc_6x6_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 6, and a block height of 6.
- [MTLPixelFormatASTC_8x5_HDR](mtlpixelformat/astc_8x5_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 8, and a block height of 5.
- [MTLPixelFormatASTC_8x6_HDR](mtlpixelformat/astc_8x6_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 8, and a block height of 6.
- [MTLPixelFormatASTC_8x8_HDR](mtlpixelformat/astc_8x8_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 8, and a block height of 8.
- [MTLPixelFormatASTC_10x5_HDR](mtlpixelformat/astc_10x5_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 5.
- [MTLPixelFormatASTC_10x6_HDR](mtlpixelformat/astc_10x6_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 6.
- [MTLPixelFormatASTC_10x8_HDR](mtlpixelformat/astc_10x8_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 8.
- [MTLPixelFormatASTC_10x10_HDR](mtlpixelformat/astc_10x10_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 10, and a block height of 10.
- [MTLPixelFormatASTC_12x10_HDR](mtlpixelformat/astc_12x10_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 12, and a block height of 10.
- [MTLPixelFormatASTC_12x12_HDR](mtlpixelformat/astc_12x12_hdr.md) — ASTC-compressed format with high-dynamic range content, a block width of 12, and a block height of 12.

### Compressed BC pixel formats

- [MTLPixelFormatBC1_RGBA](mtlpixelformat/bc1_rgba.md) — Compressed format with two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormatBC1_RGBA_sRGB](mtlpixelformat/bc1_rgba_srgb.md) — Compressed format with two 16-bit color components and one 32-bit descriptor component, with conversion between sRGB and linear space.
- [MTLPixelFormatBC2_RGBA](mtlpixelformat/bc2_rgba.md) — Compressed format with two 64-bit chunks. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormatBC2_RGBA_sRGB](mtlpixelformat/bc2_rgba_srgb.md) — Compressed format with two 64-bit chunks, with conversion between sRGB and linear space. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormatBC3_RGBA](mtlpixelformat/bc3_rgba.md) — Compressed format with two 64-bit chunks. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormatBC3_RGBA_sRGB](mtlpixelformat/bc3_rgba_srgb.md) — Compressed format with two 64-bit chunks, with conversion between sRGB and linear space. The first chunk contains two 8-bit alpha components and one 48-bit descriptor component. The second chunk contains two 16-bit color components and one 32-bit descriptor component.
- [MTLPixelFormatBC4_RUnorm](mtlpixelformat/bc4_runorm.md) — Compressed format with one normalized unsigned integer component.
- [MTLPixelFormatBC4_RSnorm](mtlpixelformat/bc4_rsnorm.md) — Compressed format with one normalized signed integer component.
- [MTLPixelFormatBC5_RGUnorm](mtlpixelformat/bc5_rgunorm.md) — Compressed format with two normalized unsigned integer components.
- [MTLPixelFormatBC5_RGSnorm](mtlpixelformat/bc5_rgsnorm.md) — Compressed format with two normalized signed integer components.
- [MTLPixelFormatBC6H_RGBFloat](mtlpixelformat/bc6h_rgbfloat.md) — Compressed format with four floating-point components.
- [MTLPixelFormatBC6H_RGBUfloat](mtlpixelformat/bc6h_rgbufloat.md) — Compressed format with four unsigned floating-point components.
- [MTLPixelFormatBC7_RGBAUnorm](mtlpixelformat/bc7_rgbaunorm.md) — Compressed format with four normalized unsigned integer components.
- [MTLPixelFormatBC7_RGBAUnorm_sRGB](mtlpixelformat/bc7_rgbaunorm_srgb.md) — Compressed format with four normalized unsigned integer components, with conversion between sRGB and linear space.

### YUV pixel formats

- [MTLPixelFormatGBGR422](mtlpixelformat/gbgr422.md) — A pixel format where the red and green components are subsampled horizontally.
- [MTLPixelFormatBGRG422](mtlpixelformat/bgrg422.md) — A pixel format where the red and green components are subsampled horizontally.

### Depth and stencil pixel formats

- [MTLPixelFormatDepth16Unorm](mtlpixelformat/depth16unorm.md) — A pixel format for a depth-render target that has a 16-bit normalized, unsigned-integer component.
- [MTLPixelFormatDepth32Float](mtlpixelformat/depth32float.md) — A pixel format with one 32-bit floating-point component, used for a depth render target.
- [MTLPixelFormatStencil8](mtlpixelformat/stencil8.md) — A pixel format with an 8-bit unsigned integer component, used for a stencil render target.
- [MTLPixelFormatDepth24Unorm_Stencil8](mtlpixelformat/depth24unorm_stencil8.md) — A 32-bit combined depth and stencil pixel format with a 24-bit normalized unsigned integer for depth and an 8-bit unsigned integer for stencil. _(deprecated)_
- [MTLPixelFormatDepth32Float_Stencil8](mtlpixelformat/depth32float_stencil8.md) — A 40-bit combined depth and stencil pixel format with a 32-bit floating-point value for depth and an 8-bit unsigned integer for stencil.
- [MTLPixelFormatX32_Stencil8](mtlpixelformat/x32_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 32-bit depth and 8-bit stencil value.
- [MTLPixelFormatX24_Stencil8](mtlpixelformat/x24_stencil8.md) — A stencil pixel format used to read the stencil value from a texture with a combined 24-bit depth and 8-bit stencil value. _(deprecated)_

### Extended range and wide color pixel formats

- [MTLPixelFormatBGRA10_XR](mtlpixelformat/bgra10_xr.md) — A 64-bit extended-range pixel format with four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormatBGRA10_XR_sRGB](mtlpixelformat/bgra10_xr_srgb.md) — A 64-bit extended-range pixel format with sRGB conversion and four fixed-point components of 10-bit blue, 10-bit green, 10-bit red, and 10-bit alpha.
- [MTLPixelFormatBGR10_XR](mtlpixelformat/bgr10_xr.md) — A 32-bit extended-range pixel format with three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.
- [MTLPixelFormatBGR10_XR_sRGB](mtlpixelformat/bgr10_xr_srgb.md) — A 32-bit extended-range pixel format with sRGB conversion and three fixed-point components of 10-bit blue, 10-bit green, and 10-bit red.

### Sentinel values

- [MTLPixelFormatInvalid](mtlpixelformat/invalid.md) — The default value of the pixel format for the `MTLRenderPipelineState`. You cannot create a texture with this value.

### Enumeration Cases

- [MTLPixelFormatUnspecialized](mtlpixelformat/unspecialized.md)

### Initializers

- [init(rawValue:)](<mtlpixelformat/init(rawvalue_).md>)

## See Also

### Texture basics

- [Understanding color-renderable pixel format sizes](understanding-color-renderable-pixel-format-sizes.md) — Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing texture data](optimizing-texture-data.md) — Optimize a texture’s data to improve GPU or CPU access.
- [MTLTexture](mtltexture.md) — A resource that holds formatted image data.
- [MTLTextureCompressionType](mtltexturecompressiontype.md)
- [MTLTextureDescriptor](mtltexturedescriptor.md) — An instance that you use to configure new Metal texture instances.
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — An object that creates textures from existing data in common image formats.
- [MTLSharedTextureHandle](mtlsharedtexturehandle.md) — A texture handle that can be shared across process address space boundaries.
