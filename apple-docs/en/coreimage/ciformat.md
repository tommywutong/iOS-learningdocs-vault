---
title: CIFormat
framework: Core Image
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciformat
source_url: 'https://developer.apple.com/documentation/coreimage/ciformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciformat.json'
content_hash: 'sha256:dfede873829cc984'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFormat

<sub>Structure</sub>

Pixel data formats for image input, output, and processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CIFormat
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Image Formats

- [kCIFormatA16](ciformat/a16.md) — A 16-bit-per-pixel, fixed-point pixel format in which the sole component is alpha.
- [kCIFormatA8](ciformat/a8.md) — An 8-bit-per-pixel, fixed-point pixel format in which the sole component is alpha.
- [kCIFormatABGR8](ciformat/abgr8.md) — A 32-bit-per-pixel, fixed-point pixel format in which the alpha value precedes the blue, green, and red color components.
- [kCIFormatARGB8](ciformat/argb8.md) — A 32-bit-per-pixel, fixed-point pixel format in which the alpha value precedes the red, green, and blue color components.
- [kCIFormatAf](ciformat/af.md) — A 32-bit-per-pixel, full-width floating-point pixel format in which the sole component is alpha.
- [kCIFormatAh](ciformat/ah.md) — A 16-bit-per-pixel, half-width floating-point pixel format in which the sole component is alpha.
- [kCIFormatBGRA8](ciformat/bgra8.md) — A 32-bit-per-pixel, fixed-point pixel format in which the blue, green, and red color components precede the alpha value.
- [kCIFormatR16](ciformat/r16.md) — A 16-bit-per-pixel, fixed-point pixel format in which the sole component is a red color value.
- [kCIFormatR8](ciformat/r8.md) — An 8-bit-per-pixel, fixed-point pixel format in which the sole component is a red color value.
- [kCIFormatRG16](ciformat/rg16.md) — A 32-bit-per-pixel, fixed-point pixel format with only red and green color components.
- [kCIFormatRG8](ciformat/rg8.md) — A 16-bit-per-pixel, fixed-point pixel format with only red and green color components.
- [kCIFormatRGB10](ciformat/rgb10.md)
- [kCIFormatRGBA16](ciformat/rgba16.md) — A 64-bit-per-pixel, fixed-point pixel format.
- [kCIFormatRGBX16](ciformat/rgbx16.md)
- [kCIFormatRGBA8](ciformat/rgba8.md) — A 32-bit-per-pixel, fixed-point pixel format in which the red, green, and blue color components precede the alpha value.
- [kCIFormatRGBAf](ciformat/rgbaf.md) — A 128-bit-per-pixel, floating-point pixel format.
- [kCIFormatRGBXf](ciformat/rgbxf.md)
- [kCIFormatRGBAh](ciformat/rgbah.md) — A 64-bit-per-pixel, floating-point pixel format.
- [kCIFormatRGBXh](ciformat/rgbxh.md)
- [kCIFormatRGf](ciformat/rgf.md) — A 64-bit-per-pixel, floating-point pixel format with only red and green color components.
- [kCIFormatRGh](ciformat/rgh.md) — A 32-bit-per-pixel, floating-point pixel format with only red and green color components.
- [kCIFormatRf](ciformat/rf.md) — A 32-bit-per-pixel, floating-point pixel format in which the sole component is a red color value.
- [kCIFormatRh](ciformat/rh.md) — A 16-bit-per-pixel, floating-point pixel format in which the sole component is a red color value.
- [kCIFormatL16](ciformat/l16.md) — A 16-bit-per-pixel, fixed-point pixel format in which the sole component is luminance.
- [kCIFormatL8](ciformat/l8.md) — An 8-bit-per-pixel, fixed-point pixel format in which the sole component is luminance.
- [kCIFormatLA16](ciformat/la16.md) — A 32-bit-per-pixel, fixed-point pixel format with only 16-bit luminance and alpha components.
- [kCIFormatLA8](ciformat/la8.md) — A 16-bit-per-pixel, fixed-point pixel format with only 8-bit luminance and alpha components.
- [kCIFormatLAf](ciformat/laf.md) — A 64-bit-per-pixel, full-width floating-point pixel format with 32-bit luminance and alpha components.
- [kCIFormatLAh](ciformat/lah.md) — A 32-bit-per-pixel, half-width floating-point pixel format with 16-bit luminance and alpha components.
- [kCIFormatLf](ciformat/lf.md) — A 32-bit-per-pixel, full-width floating-point pixel format in which the sole component is luminance.
- [kCIFormatLh](ciformat/lh.md) — A 16-bit-per-pixel, half-width floating-point pixel format in which the sole component is luminance.

### Initializers

- [init(rawValue:)](<ciformat/init(rawvalue_).md>)

### Type Properties

- [kCIFormatRGBX8](ciformat/rgbx8.md)

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
