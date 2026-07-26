---
title: CIWarpKernel
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciwarpkernel
source_url: 'https://developer.apple.com/documentation/coreimage/ciwarpkernel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciwarpkernel.json'
content_hash: 'sha256:e5d1d863f645904d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIWarpKernel

<sub>Class</sub>

A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIWarpKernel
```

## Overview

The kernel language routine for a warp kernel has the following characteristics:

- It uses exactly one input image.
- Its return type is `vec2` (Core Image Kernel Language) or `float2` (Metal Shading Language), specifying a position in source image coordinates.

A warp kernel routine requires no input parameters (but can use additional custom parameters you declare). Typically, a warp kernel uses the destination coordinate function to look up the coordinates of the destination pixel currently being rendered, then computes a corresponding position in source image coordinates (output using the `return` keyword). Core Image then samples from the source image at the returned coordinates to produce a pixel color for the output image. For example, the Metal Shading Language source below implements a filter that passes through its input image unchanged.

```c
#include <CoreImage/CoreImage.h>
 
extern "C" {
    namespace coreimage {
        float2 do_nothing(destination dest) {
            return dest.coord();
        }
    }
}
```

The equivalent code in Core Image Kernel Language is:

```c
kernel vec2 do_nothing() {
    return destCoord();
}
```

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Relationships

- **Inherits From**: [CIKernel](cikernel.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Kernel

- [+ kernelWithString:](<ciwarpkernel/init(source_).md>) — Creates a warp kernel object from the specified kernel source code. _(deprecated)_

### Applying a Kernel to Filter an Image

- [- applyWithExtent:roiCallback:inputImage:arguments:](<ciwarpkernel/apply(extent_roicallback_image_arguments_).md>) — Creates a new image using the kernel and the specified input image and arguments.

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
