---
title: CIColorKernel
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorkernel
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorkernel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorkernel.json'
content_hash: 'sha256:ca7b132c53f8ffe6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColorKernel

<sub>Class</sub>

A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIColorKernel
```

## Overview

The kernel language routine for a color kernel has the following characteristics:

- Its return type is `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language); that is, it returns a pixel color for the output image.
- It may use zero or more input images. Each input image is represented by a parameter of type `__sample` (Core Image Kernel Language) or `sample_t` (Metal Shading Language), which can be treated as a single pixel color of type `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language);.

A color kernel routine receives as input single-pixel colors (one sampled from each input image) and computes a final pixel color (output using the `return` keyword). For example, the Metal Shading Language source below implements a filter that passes through its input image unchanged.

```c
#include <CoreImage/CoreImage.h>
 
extern "C" {
    namespace coreimage {
        float4 do_nothing(sample_t s) {
            return s;
        }
    }
}
```

The equivalent code in Core Image Kernel Language is:

```c
kernel vec4 do_nothing(__sample s) {
    return s.rgba;
}
```

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Relationships

- **Inherits From**: [CIKernel](cikernel.md)

- **Inherited By**: [CIBlendKernel](ciblendkernel.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Kernel

- [+ kernelWithString:](<cicolorkernel/init(source_).md>) — Creates a color kernel object from the specified kernel source code. _(deprecated)_

### Applying a Kernel to Filter an Image

- [- applyWithExtent:arguments:](<cicolorkernel/apply(extent_arguments_).md>) — Creates a new image using the kernel and specified arguments.

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
