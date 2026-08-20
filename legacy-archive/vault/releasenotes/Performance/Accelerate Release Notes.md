---
title: Accelerate Release Notes
apple_id: TP40001049
resource_type: Release Note
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/Performance/RN-vecLib/index.html
archived_at: '2026-07-18T02:59:02.168263Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Accelerate Framework Release Notes for OS X v10.9

#### Contents:

- [vImage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknlte)
- [OS X.9 and iOS 7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknlti)

### vImage

vImage is a high-performance framework for low-level image processing operations. It is a subframework of `Accelerate.framework`. When you link to Accelerate, you get vImage. vImage provides capabilities such as blurring, image resampling/resizing, edge detection, histograms, alpha compositing, color, and image format conversions.

> [!NOTE]
> 

### OS X.9 and iOS 7

`vImage.framework` has been extended with several major new features:

- Improved [Core Graphics Interoperability](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknltk) — see vImage/vImage_Utilities.h
- New functions for [16-bit resampling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknlts)
- New [Multidimensional Lookup Tables and piecewise gamma curves](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknltcmi)
- Improved [Conversions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknltcmy) support
- [Other Additions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanbzfvbuqmrnknltcni)

### Core Graphics Interoperability

A new header, `vImage_Utilities.h`, is added to provide a series of APIs to streamline data interchange between vImage and the rest of the system. This provides a set of interfaces to quickly and easily exchange image data with Core Graphics, through functions that convert `vImage_Buffer` objectss to `CGImageRef` objects and back. Since Core Graphics provides the underlying support for Cocoa and UIKit drawing primitives, these methods can also be used to quickly and simply exchange pixel data with these Objective C APIs, including many pixel formats not usually supported by these APIs, using bridging APIs such as `imageWithCGImage:`.

### New Types

A new type is added to aggregate several Core Graphics types typically used to describe image formats:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`vImage_CGImageFormat`** | : |  | | --- | | ``` typedef struct { ``` | | ```     uint32_t                bitsPerComponent; ``` | | ```     uint32_t                bitsPerPixel; ``` | | ```     CGColorSpaceRef         colorSpace; ``` | | ```     CGBitmapInfo            bitmapInfo; ``` | | ```     uint32_t                version; ``` | | ```     const CGFloat           *decode; ``` | | ```     CGColorRenderingIntent  renderingIntent; ``` | | ``` }vImage_CGImageFormat; ``` |  The meaning of these fields is the same as in `CGImageCreate`. |

### New Functions:

The following APIs are provided to streamline interoperability with Core Graphics, to provide for facile import and export of vImage data into formats such as PNG and JPEG, and to draw to the screen.

- `vImageBuffer_init`

  A method to streamline allocating `vImage_Buffer.data` with an optimally sized `rowBytes` value for image performance.
- `vImageBuffer_initWithCGImage`

  Initialize a `vImage_Buffer` struct with data from a `CGImageRef`.
- `vImageCreateCGImageFromBuffer`

  Create a `CGImageRef` from a `vImage_Buffer`.
- `vImageBuffer_GetSize`

  Convenience function to return size of `vImage_Buffer` as `CGSize`. Will not round up.
- `vImageCGImageFormat_GetComponentCount`

  Convenience function to return the number of color + alpha channels in an image format.
- `vImageCGImageFormat_IsEqual`

  Returns true if two CG formats are equivalent -- that is, when `vImageConvert_AnyToAny` would just be doing a copy.
- `vImageConverter_MustOperateOutOfPlace`

  Returns `true` when the source and destination images passed to `vImageConvert_AnyToAny` must not overlap.
- `vImageConvert_AnyToAny`

  A high-performance method to convert between almost any Core Graphics pixel format. The conversions are vectorized and multithreaded. The function supports alpha, endianness, format (for example, 8-bit to half-float), decode array, colorspace and rendering intent conversions, and any combination thereof. Make all your image formats “fast-path”!

### Example:

Here is an example of how to initialize a vImage_Buffer of a desired format (BGRA, 8-bit, sRGB in this case), from a file referenced by a CFURLRef. (CFURLRefs are toll-free bridged with NSURLs):

```
CFURLRef url = ...;
CGImageSourceRef imageSource = CGImageSourceCreateWithURL(url, NULL);
CGImageRef image = CGImageSourceCreateImageAtIndex( imageSource, 0, NULL );
vImage_Buffer result;
vImage_CGImageFormat format = {
    .bitsPerComponent = 8,
    .bitsPerPixel = 32,
    .bitmapInfo = kCGBitmapByteOrder32Little | kCGImageAlphaNoneSkipFirst,  //BGRX8888
    .colorSpace = NULL,    //sRGB
}; // .version, .renderingIntent and .decode all initialized to 0 per C rules
vImage_Error err = vImageBuffer_InitWithCGImage( &result, &format, NULL, image, kvImageNoFlags );
```

You may optionally elect to allocate the buffer yourself and have vImage just fill it with the correct pixels, with `kvImageNoAllocate` flag.

Likewise, creating a `CGImageRef` object from a `vImage_Buffer` object is relatively simple:

```
vImage_Buffer buf = ...;
// Declare the pixel format for the vImage_Buffer
vImage_CGImageFormat format = {
    .bitsPerComponent = 8,
    .bitsPerPixel = 32,
    .bitmapInfo = kCGBitmapByteOrderDefault | kCGImageAlphaLast,  //RGBA8888
}; // .colorspace, .version, .renderingIntent and .decode all initialized to 0 per C rules
CGImageRef image = vImageCreateCGImageFromBuffer( &buf, &format, NULL, NULL, kvImageNoFlags, &err);
```

Advanced options are available to allow your to directly use the `vImage_Buffer` object as the backing store for the new image without causing a copy. Please see the `vImage_Utilities.h` header comments for more. In addition `vImageConvert_AnyToAny` is provided to convert nearly any Core Graphics image format to nearly any other. All facets of the image format can be converted, including the colorspace. There are also a set of convenience functions for interconverting between Core Graphics and vImage coordinate spaces and determining whether two images have the same format.

### 16-bit resampling

### New Functions

High-performance routines to rotate, shear, warp, and resize 16-bit images just like 8-bit and floating-point images. Both signed and unsigned 16-bit formats are supported.

- `vImageRotate_ARGB16U` / `vImageRotate_ARGB16S`
- `vImageScale_ARGB16U` / `vImageScale_ARGB16S`
- `vImageAffineWarp_ARGB16U` / `vImageAffineWarp_ARGB16S`
- `vImageHorizontalReflect_ARGB16U` / `vImageHorizontalReflect_ARGB16S`
- `vImageVerticalReflect_ARGB16U` / `vImageVerticalReflect_ARGB16S`
- `vImageHorizontalShear_ARGB16U` / `vImageHorizontalShear_ARGB16S`
- `vImageVerticalShear_ARGB16U` / `vImageVerticalShear_ARGB16S`

### Multidimensional Lookup Tables and piecewise gamma curves

### New Functions

Multidimensional lookup tables and piecewise gamma curves (power functions with a linear segment near zero) are commonly used for color conversion. We provide high-performance routines for floating-point and 16Q12 (16-bit signed fixed point with 12 fractional bits) image formats for as many as 16 color channels.

- `vImageMultiDimensionalInterpolatedLookupTable_PlanarF`
- `vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12`
- `vImagePiecewiseGamma_Planar8` / `vImagePiecewiseGamma_Planar16Q12` / `vImagePiecewiseGamma_PlanarF`
- `vImagePiecewiseGamma_Planar8toPlanar16Q12` / `vImagePiecewiseGamma_Planar16Q12toPlanar8`
- `vImagePiecewiseGamma_Planar8toPlanarF` / `vImagePiecewiseGamma_PlanarFtoPlanar8`

We've also added several 1D lookup tables:

- `vImageLookupTable_Planar8toPlanar16`
- `vImageLookupTable_Planar8toPlanarF` / `vImageLookupTable_PlanarFtoPlanar8`
- `vImageLookupTable_8to64U`

And 16-bit support for matrix multiplication, for color conversion and color twist operations on 16-bit signed data:

- `vImageMatrixMultiply_Planar16S`

### Conversions

### New Functions

Many new conversions were added to support `vImageConvert_AnyToAny`. These are exposed for use when you already know which conversion you want and just want to call that.

- `vImageConvert_ARGB16UToARGB8888` / `vImageConvert_ARGB8888ToARGB16U`
- `vImageConvert_RGB16UToARGB8888` / `vImageConvert_ARGB8888ToRGB16U`

  (also do channel reordering and channel insertion)
- `vImageConvert_16Uto16F` / `vImageConvert_16Fto16U`
- `vImageConvert_Planar8toPlanar16F` / `vImageConvert_Planar16FtoPlanar8`
- `vImageConvert_ARGB8888toPlanarF` / `vImageConvert_ARGBFFFFtoPlanar8`
- `vImageConvert_ARGBFFFFtoRGBFFF` / `vImageConvert_RGBAFFFFtoRGBFFF` / `vImageConvert_BGRAFFFFtoRGBFFF`
- `vImageConvert_RGBFFFtoARGBFFFF` / `vImageConvert_RGBFFFtoRGBAFFFF` / `vImageConvert_RGBFFFtoBGRAFFFF`
- `vImageConvert_RGBA8888toRGB888` / `vImageConvert_BGRA8888toRGB888`
- `vImageConvert_RGB565toRGBA8888` / `vImageConvert_RGB565toBGRA8888`
- `vImageConvert_XRGB8888ToPlanar8` / `vImageConvert_BGRX8888ToPlanar8`
- `vImageConvert_XRGBFFFFToPlanarF` / `vImageConvert_BGRXFFFFToPlanarF`
- `vImageConvert_Planar16UtoARGB16U` / `vImageConvert_ARGB16UtoPlanar16U`
- `vImageConvert_Planar16UtoRGB16U` / `vImageConvert_RGB16UtoPlanar16U`
- `vImageConvert_RGB16UtoARGB16U` / `vImageConvert_RGB16UtoRGBA16U` / `vImageConvert_RGB16UtoBGRA16U`
- `vImageConvert_ARGB16UtoRGB16U` / `vImageConvert_RGBA16UtoRGB16U` / `vImageConvert_BGRA16UtoRGB16U`
- `vImageFlatten_ARGB8888` / `vImageFlatten_RGBA8888`
- `vImageFlatten_ARGB16U` / `vImageFlatten_RGBA16U`
- `vImageFlatten_ARGB16Q12` / `vImageFlatten_RGBA16Q12`
- `vImageFlatten_ARGBFFFF` / `vImageFlatten_RGBAFFFF`
- `vImageFlatten_ARGB8888ToRGB888` / `vImageFlatten_RGBA8888ToRGB888` / `vImageFlatten_BGRA8888ToRGB888`
- `vImageFlatten_ARGBFFFFToRGBFFF` / `vImageFlatten_RGBAFFFFToRGBFFF` / `vImageFlatten_BGRAFFFFToRGBFFF`
- `vImageConvert_Planar1toPlanar8` / `vImageConvert_Planar2toPlanar8` / `vImageConvert_Planar4toPlanar8`
- `vImageConvert_Indexed1toPlanar8` / `vImageConvert_Indexed2toPlanar8` / `vImageConvert_Indexed4toPlanar8`
- `vImageConvert_Planar8toPlanar1` / `vImageConvert_Planar8toPlanar2` / `vImageConvert_Planar8toPlanar4`
- `vImageConvert_Planar8toIndexed1` / `vImageConvert_Planar8toIndexed2` / `vImageConvert_Planar8toIndexed4`
- `vImageConvert_8to16Q12` / `vImageConvert_RGB888toPlanar16Q12` / `vImageConvert_ARGB8888toPlanar16Q12`
- `vImageConvert_16Q12to8` / `vImageConvert_Planar16Q12toRGB888` / `vImageConvert_Planar16Q12toARGB8888`
- `vImageConvert_16Q12toF` / `vImageConvert_Fto16Q12`
- `vImageConvert_16Q12to16U` / `vImageConvert_16Uto16Q12`
- `vImageOverwriteChannelsWithPixel_ARGB8888`
- `vImageByteSwap_Planar16U`

### Other Additions

### New Functions

A number of new functions were added to support the 16Q12 data format. 16Q12 is a signed 16-bit fixed-point format capable of representing the range from [–8,8). It has 12 bits of fractional precision. The extra precision and range are useful for preserving signal fidelity when doing nonlinear operations on 8-bit data.

- `vImagePremultipliedAlphaBlendWithPermute_ARGB8888` / `vImagePremultipliedAlphaBlendWithPermute_RGBA8888`
- `vImagePermuteChannelsWithMaskedInsert_ARGB8888` / `vImagePermuteChannelsWithMaskedInsert_ARGBFFFF`
- `vImagePremultiplyData_ARGB16Q12` / `vImagePremultiplyData_RGBA16Q12`
- `vImageUnpremultiplyData_ARGB16Q12` / `vImageUnpremultiplyData_RGBA16Q12`
- `vImageBufferFill_ARGB16U` / `vImageBufferFill_ARGB16S`
