---
title: CISampler
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisampler
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler.json'
content_hash: 'sha256:d061186f301fae5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CISampler

<sub>Class</sub>

An object that retrieves pixel samples for processing by a filter kernel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CISampler
```

## Overview

The `CISampler` class retrieves samples of images for processing by a [CIKernel](cikernel.md) object. A `CISampler` object defines a coordinate transform, and modes for interpolation and wrapping. You use `CISampler` objects in conjunction with other Core Image classes, such as  [CIFilter](cifilter-swift.class.md), `CIKernel`, and [CIFilterShape](cifiltershape.md), to create custom filters.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Sampler

- [- initWithImage:](<cisampler/init(image_).md>) — Initializes a sampler with an image object.
- [- initWithImage:options:](<cisampler/init(image_options_).md>) — Initializes the sampler with an image object using options specified in a dictionary.

### Getting Information About the Sampler Object

- [definition](cisampler/definition.md) — The domain of definition (DOD) of the sampler
- [extent](cisampler/extent.md) — The rectangle that specifies the extent of the sampler

### Constants

- [Sampler Option Keys](sampler-option-keys.md) — Keys for creating a sampler.
- [Sampler Option Values](sampler-option-values.md) — Values for sampler option keys.

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
