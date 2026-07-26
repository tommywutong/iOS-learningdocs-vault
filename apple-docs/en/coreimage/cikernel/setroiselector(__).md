---
title: 'setROISelector(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cikernel/setroiselector(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/setroiselector(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/setroiselector%28_%3A%29.json'
content_hash: 'sha256:6cf96f03866dee45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# setROISelector(_:)

<sub>Instance Method</sub>

Sets the selector Core Image uses to query the region of interest for image processing with the kernel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setROISelector(_ method: Selector)
```

## Parameters

- `method` — A selector name.

## Discussion

> [!important] Important
> This method is not supported in iOS, and not recommended in macOS 10.11 and later. Supply and use a block-based ROI callback instead using the [- applyWithExtent:roiCallback:arguments:](<apply(extent_roicallback_arguments_).md>) method. The discussion below applies only to OS X v10.10 and earlier.

When applying a filter kernel, the region of interest (ROI) is the area of source image pixels that must be processed to produce a given area of destination image pixels. For a more detailed definition, see [The Region of Interest](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_advanced_concepts/ci.advanced_concepts.html#//apple_ref/doc/uid/TP30001185-CH9-SW12).

The `aMethod` argument must use the signature that is defined for the `regionOf:destRect:userInfo:` method, which is as follows:

`- (CGRect) regionOf:(int)samplerIndex destRect:(CGRect)r userInfo:obj;`

where:

- `samplerIndex` defines the sampler to query
- `destRect` is the extent of the region, in working space coordinates, to render.
- `userInfo` is the object associated with the `kCIApplyOptionUserInfo` option when the kernel is applied to its arguments (with the [- apply:arguments:options:](<../cifilter-swift.class/apply(__arguments_options_).md>) method of a [CIFilter](../cifilter-swift.class.md) object using the kernel). The `userInfo` is important because instance variables can’t be used by the defining class. Instance variables must be passed through the `userInfo` argument.

The `regionOf:destRect:userInfo:` method of the CIFilter object is called by the framework. This method returns the rectangle that contains the region of the sampler that the kernel needs to render the specified destination rectangle.

A sample `regionOf:destRect:userInfo:` method might look as follows:

```objc
- (CGRect)regionOf:(int)sampler destRect:(CGRect)r userInfo:params
{
  float scale = fabs ([params X]);
  return CGRectInset (r, scale * -1.3333, scale * -1.3333);
}
```

If your kernel does not need the image at `index` to produce output in the rectangle `rect`, your method should return [CGRectNull](../../coregraphics/cgrectnull.md).

In the filter code, you set the selector using the following:

`[kernel setROISelector:@selector(regionOf:destRect:userInfo:)`]

Alternatively, use the [- applyWithExtent:roiCallback:arguments:](<apply(extent_roicallback_arguments_).md>) method to directly apply a kernel to create an output image, specifying the ROI callback as a block or closure.

## See Also

### Related Documentation

- [- applyWithExtent:roiCallback:arguments:](<apply(extent_roicallback_arguments_).md>) — Creates a new image using the kernel and specified arguments.
- [- apply:arguments:options:](<../cifilter-swift.class/apply(__arguments_options_).md>) — Produces a [CIImage](../ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.
