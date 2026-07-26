---
title: 'apply(extent:roiCallback:arguments:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cikernel/apply(extent:roicallback:arguments:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/apply(extent:roicallback:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/apply%28extent%3Aroicallback%3Aarguments%3A%29.json'
content_hash: 'sha256:0fbeb1c2da48ceea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# apply(extent:roiCallback:arguments:)

<sub>Instance Method</sub>

Creates a new image using the kernel and specified arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func apply(extent: CGRect, roiCallback callback: @escaping CIKernelROICallback, arguments args: [Any]) -> CIImage?
```

## Parameters

- `extent` — The extent of the output image.

- `callback` — A block or closure that computes the region of interest for a given rectangle of destination image pixels. See [CIKernelROICallback](../cikernelroicallback.md).

- `args` — An array of arguments to pass to the kernel routine. The type of each object in the array must be compatible with the corresponding parameter declared in the kernel routine source code. For details, see [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397).

## Return Value

A new image object describing the result of applying the kernel.

## Discussion

This method is analogous to the [CIFilter](../cifilter-swift.class.md) method [- apply:arguments:options:](<../cifilter-swift.class/apply(__arguments_options_).md>), but it does not require construction of a [CIFilter](../cifilter-swift.class.md) object, and it allows you to specify a callback for determining the kernel’s region of interest as a block or closure. As with the similar [CIFilter](../cifilter-swift.class.md) method, calling this method does not execute the kernel code—filters and their kernel code are evaluated only when rendering a final output image.

When applying a filter kernel, the region of interest (ROI) is the area of source image pixels that must be processed to produce a given area of destination image pixels. For a more detailed definition, see [The Region of Interest](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_advanced_concepts/ci.advanced_concepts.html#//apple_ref/doc/uid/TP30001185-CH9-SW12). Core Image calls your `callback` block or closure to determine the ROI when rendering the filter output. Core Image automatically splits large images into smaller tiles for rendering, so your callback may be called multiple times.

## See Also

### Applying a Kernel to Filter an Image

- [CIKernelROICallback](../cikernelroicallback.md) — The signature for a block that computes the region of interest (ROI) for a given area of destination image pixels. Core Image calls this block when applying the kernel. You specify this block when using the [- applyWithExtent:roiCallback:arguments:](<apply(extent_roicallback_arguments_).md>) method.
