---
title: CIFilterShape
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifiltershape
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltershape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltershape.json'
content_hash: 'sha256:5c07df082ea7ffff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFilterShape

<sub>Class</sub>

A description of the bounding shape of a filter and the domain of definition for a filter operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIFilterShape
```

## Overview

You use `CIFilterShape` objects in conjunction with Core Image classes, such as [CIFilter](cifilter-swift.class.md), [CIKernel](cikernel.md), and [CISampler](cisampler.md), to create custom filters.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Filter Shape

- [- initWithRect:](<cifiltershape/init(rect_).md>) — Initializes a filter shape object with a rectangle.

### Inspecting a Filter Shape

- [extent](cifiltershape/extent.md) — The extent of the filter shape.

### Modifying a Filter Shape

- [- insetByX:Y:](<cifiltershape/insetby(x_y_).md>) — Modifies a filter shape object so that it is inset by the specified x and y values.
- [- intersectWith:](<cifiltershape/intersect(with_)-8iw.md>) — Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [- intersectWithRect:](<cifiltershape/intersect(with_)-2o2n8.md>) — Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [- transformBy:interior:](<cifiltershape/transform(by_interior_).md>) — Creates a filter shape that results from applying a transform to the current filter shape.
- [- unionWith:](<cifiltershape/union(with_)-52mnd.md>) — Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [- unionWithRect:](<cifiltershape/union(with_)-75ebo.md>) — Creates a filter shape that results from the union of the current filter shape and a rectangle.

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
