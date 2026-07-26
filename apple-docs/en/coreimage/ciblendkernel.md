---
title: CIBlendKernel
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciblendkernel
source_url: 'https://developer.apple.com/documentation/coreimage/ciblendkernel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciblendkernel.json'
content_hash: 'sha256:4db76cb2d6a3cfa7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIBlendKernel

<sub>Class</sub>

A GPU-based image-processing routine that is optimized for blending two images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIBlendKernel
```

## Overview

The blend kernel function has the following characteristics:

- It has two arguments of type `__sample` (Core Image Kernel Language) or `sample_t` (Metal Shading Language), representing the foreground and background images.
- Its return type is `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language); that is, it returns a pixel color for the output image.

A blend kernel routine receives as input single-pixel colors (one sampled from each input image) and computes a final pixel color (output using the return keyword). For example, the Metal Shading Language source below implements a filter that returns the average of its two input images.

```c
#include <CoreImage/CoreImage.h>
 
float4 averageBlend(sample_t foreground, sample_t background) {
    return (foreground + background) / 2.0;
}
```

Generally, the extent of the output image is the union of the extents of the foreground and background images.

## Relationships

- **Inherits From**: [CIColorKernel](cicolorkernel.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Kernel

- [+ kernelWithString:](<ciblendkernel/init(source_).md>) — Creates a custom blend kernel from a program string. _(deprecated)_

### Applying a Kernel to Filter an Image

- [- applyWithForeground:background:](<ciblendkernel/apply(foreground_background_).md>) — Creates a new image using the blend kernel and specified foreground and background images.

### Builtin Blend Kernels

- [clear](ciblendkernel/clear.md) — A blend kernel that returns a clear color.
- [color](ciblendkernel/color.md) — A blend kernel that uses the luminance values of the background with the hue and saturation values of the foreground image.
- [colorBurn](ciblendkernel/colorburn.md) — A blend kernel that darkens the background image samples to reflect the foreground image samples.
- [colorDodge](ciblendkernel/colordodge.md) — A blend kernel that brightens the background image samples to reflect the foreground image samples.
- [componentAdd](ciblendkernel/componentadd.md) — A blend kernel that adds color components to achieve a brightening effect.
- [componentMax](ciblendkernel/componentmax.md) — A blend kernel that creates an image using the maximum values of two input images.
- [componentMin](ciblendkernel/componentmin.md) — A blend kernel that creates an image using the minimum values of two input images.
- [componentMultiply](ciblendkernel/componentmultiply.md) — A blend kernel that multiplies the color components of its input images.
- [darken](ciblendkernel/darken.md) — A blend kernel that creates an image using the darker values of two input images.
- [darkerColor](ciblendkernel/darkercolor.md) — A blend kernel that creates an image using the darker color of two input images.
- [destination](ciblendkernel/destination.md) — A blend kernel that returns the background input image.
- [destinationAtop](ciblendkernel/destinationatop.md) — A blend kernel that places the background over the foreground and crops based on the visibility of the foreground.
- [destinationIn](ciblendkernel/destinationin.md) — A blend kernel that places the background over the foreground and crops based on the visibility of both.
- [destinationOut](ciblendkernel/destinationout.md) — A blend kernel that uses the background image to define what to take out of the foreground image.
- [destinationOver](ciblendkernel/destinationover.md) — A blend kernel that places the background image over the input foreground image.
- [difference](ciblendkernel/difference.md) — A blend kernel that creates an image using the difference between the background and foreground images.
- [divide](ciblendkernel/divide.md) — A blend kernel that divides the background image sample color with the foreground image sample color.
- [exclusion](ciblendkernel/exclusion.md) — A blend kernel that produces an effect similar to difference blending but with lower contrast.
- [exclusiveOr](ciblendkernel/exclusiveor.md) — A blend kernel that returns either the foreground or background image if the other contains a clear color.
- [hardLight](ciblendkernel/hardlight.md) — A blend kernel that either multiplies or screens colors, depending on the source image sample color.
- [hardMix](ciblendkernel/hardmix.md) — A blend kernel that adds two images together, setting each color channel value to either 0 or 1.
- [hue](ciblendkernel/hue.md) — A blend kernel that uses the luminance and saturation values of the background image with the hue of the foreground image.
- [lighten](ciblendkernel/lighten.md) — A blend kernel that creates an image using the lighter values of two input images.
- [lighterColor](ciblendkernel/lightercolor.md) — A blend kernel that creates an image using the lighter color of two input images.
- [linearBurn](ciblendkernel/linearburn.md) — A blend kernel that darkens the background image samples to reflect the foreground image samples while also increasing contrast.
- [linearDodge](ciblendkernel/lineardodge.md) — A blend kernel that lightens the background image samples to reflect the foreground image samples while also increasing contrast.
- [linearLight](ciblendkernel/linearlight.md) — A blend kernel that burns or dodges colors by changing brightness, depending on the blend color.
- [luminosity](ciblendkernel/luminosity.md) — A blend kernel that uses the hue and saturation of the background image with the luminance of the foreground image.
- [multiply](ciblendkernel/multiply.md) — A blend kernel that multiplies the background image sample color with the foreground image sample color.
- [overlay](ciblendkernel/overlay.md) — A blend kernel that either multiplies or screens the foreground image samples with the background image samples, depending on the background color.
- [pinLight](ciblendkernel/pinlight.md) — A blend kernel that conditionally replaces background image samples with source image samples depending on the brightness of the source image samples.
- [saturation](ciblendkernel/saturation.md) — A blend kernel that uses the luminance and hue values of the background image with the saturation of the foreground image.
- [screen](ciblendkernel/screen.md) — A blend kernel that multiplies the inverse of the foreground image samples with the inverse of the background image samples.
- [softLight](ciblendkernel/softlight.md) — A blend kernel that either darkens or lightens colors, depending on the foreground image sample color.
- [source](ciblendkernel/source.md) — A blend kernel that returns the foreground input image.
- [sourceAtop](ciblendkernel/sourceatop.md) — A blend kernel that places the foreground over the background and crops based on the visibility of the background.
- [sourceIn](ciblendkernel/sourcein.md) — A blend kernel that places the foreground over the background and crops based on the visibility of both.
- [sourceOut](ciblendkernel/sourceout.md) — A blend kernel that uses the foreground image to define what to take out of the background image.
- [sourceOver](ciblendkernel/sourceover.md) — A blend kernel that places the foreground image over the input background image.
- [subtract](ciblendkernel/subtract.md) — A blend kernel that subtracts the background image sample color from the foreground image sample color.
- [vividLight](ciblendkernel/vividlight.md) — A blend kernel that burns or dodges colors by changing contrast, depending on the blend color.

### Instance Methods

- [- applyWithForeground:background:colorSpace:](<ciblendkernel/apply(foreground_background_colorspace_).md>)

## See Also

### Custom Filters

- [Writing Custom Kernels](writing-custom-kernels.md) — Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [CIKernel](cikernel.md) — A GPU-based image-processing routine used to create custom Core Image filters.
- [CIColorKernel](cicolorkernel.md) — A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [CIWarpKernel](ciwarpkernel.md) — A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [CISampler](cisampler.md) — An object that retrieves pixel samples for processing by a filter kernel.
- [CIFilterShape](cifiltershape.md) — A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [CIFormat](ciformat.md) — Pixel data formats for image input, output, and processing.
