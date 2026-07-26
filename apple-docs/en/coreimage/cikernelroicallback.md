---
title: CIKernelROICallback
framework: Core Image
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cikernelroicallback
source_url: 'https://developer.apple.com/documentation/coreimage/cikernelroicallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernelroicallback.json'
content_hash: 'sha256:2663eb43940f9d61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIKernelROICallback

<sub>Type Alias</sub>

The signature for a block that computes the region of interest (ROI) for a given area of destination image pixels. Core Image calls this block when applying the kernel. You specify this block when using the [- applyWithExtent:roiCallback:arguments:](<cikernel/apply(extent_roicallback_arguments_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias CIKernelROICallback = (Int32, CGRect) -> CGRect
```

## Discussion

The block takes the following parameters:

- **index** — For a general-purpose kernel or color kernel routine that supports multiple input images, the index of the source image for which Core Image is requesting ROI information. For all other kernel routines, this parameter is always zero.
- **rect** — The rectangle in destination image pixels for which Core Image is requesting ROI information.

The block returns a [CGRect](../corefoundation/cgrect.md) structure describing the region of interest for the specified rectangle.

When applying a filter kernel, the region of interest is the area of source image pixels that must be processed to produce a given area of destination image pixels. (For a more detailed definition, see [The Region of Interest](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_advanced_concepts/ci.advanced_concepts.html#//apple_ref/doc/uid/TP30001185-CH9-SW12).) For example, a kernel that applies a blur effect in a ten-pixel radius must sample source image pixels ten pixels away in each direction from every output pixel. Thus, its region of interest is a rectangle ten pixels larger on each side than the destination rectangle:

```objc
CIKernelROICallback callback = ^(int index, CGRect rect) {
    return CGRectInset(rect, -10, -10);
};
```

If your kernel does not need the image at `index` to produce output in the rectangle `rect`, your block should return [CGRectNull](../coregraphics/cgrectnull.md).

## See Also

### Applying a Kernel to Filter an Image

- [- applyWithExtent:roiCallback:arguments:](<cikernel/apply(extent_roicallback_arguments_).md>) — Creates a new image using the kernel and specified arguments.
