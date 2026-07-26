---
title: CIKernel
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cikernel
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel.json'
content_hash: 'sha256:96715bc824c32625'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIKernel

<sub>Class</sub>

A GPU-based image-processing routine used to create custom Core Image filters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIKernel
```

## Overview

> [!note] Note
> If your custom filter uses both color and geometry information, but does not require processing both at the same time, you can improve performance by separating your image processing code: use a [CIColorKernel](cicolorkernel.md) object for the color processing step and a [CIWarpKernel](ciwarpkernel.md) object for the geometry processing step.

The kernel language routine for a general-purpose filter kernel has the following characteristics:

- Its return type is `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language); that is, it returns a pixel color for the output image.
- It may use zero or more input images. Each input image is represented by a parameter of type `sampler`.

A kernel routine typically produces its output by calculating source image coordinates (using the `destCoord` and `samplerTransform` functions or the `samplerTransform` function), samples from the source images (using the `sample` function), and computes a final pixel color (output using the `return` keyword). For example, the Metal Shading Language source below implements a filter that passes through its input image unchanged.

```c
#include <CoreImage/CoreImage.h>
 
extern "C" {
    namespace coreimage {
        float4 do_nothing(sampler src) {
            return src.sample(src.coord());
        }
    }
}
```

The equivalent code in Core Image Kernel Language is:

```c
kernel vec4 do_nothing(sampler image) {
    vec2 dc = destCoord();
    return sample(image, samplerTransform(image, dc));
}
```

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [CIColorKernel](cicolorkernel.md), [CIWarpKernel](ciwarpkernel.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Kernel Using Metal Shading Language

- [+ kernelWithFunctionName:fromMetalLibraryData:error:](<cikernel/init(functionname_frommetallibrarydata_).md>) — Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [+ kernelWithFunctionName:fromMetalLibraryData:outputPixelFormat:error:](<cikernel/init(functionname_frommetallibrarydata_outputpixelformat_).md>) — Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [+ kernelNamesFromMetalLibraryData:](<cikernel/kernelnames(frommetallibrarydata_).md>) — Return an array of strings containing the names of all of the kernels contained in the Metal library.
- [+ kernelsWithMetalString:error:](<cikernel/kernels(withmetalstring_).md>) — Load kernels from a Metal language string.

### Getting a Kernel Name

- [name](cikernel/name.md) — The name of the kernel routine.

### Identifying the Region of Interest for the Kernel

- [- setROISelector:](<cikernel/setroiselector(__).md>) — Sets the selector Core Image uses to query the region of interest for image processing with the kernel.

### Applying a Kernel to Filter an Image

- [- applyWithExtent:roiCallback:arguments:](<cikernel/apply(extent_roicallback_arguments_).md>) — Creates a new image using the kernel and specified arguments.
- [CIKernelROICallback](cikernelroicallback.md) — The signature for a block that computes the region of interest (ROI) for a given area of destination image pixels. Core Image calls this block when applying the kernel. You specify this block when using the [- applyWithExtent:roiCallback:arguments:](<cikernel/apply(extent_roicallback_arguments_).md>) method.

### Deprecated

- [+ kernelWithString:](<cikernel/init(source_).md>) — Creates a single kernel object. _(deprecated)_
- [+ kernelsWithString:](<cikernel/makekernels(source_).md>) — Creates and returns and array of  `CIKernel` objects. _(deprecated)_

### Initializers

- [init(string:)](<cikernel/init(string_).md>) _(deprecated)_

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CIBlendKernel](ciblendkernel.md) — A GPU-based image-processing routine that is optimized for blending two images.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
