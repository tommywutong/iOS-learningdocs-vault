---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_masks/tq_masks.html
archived_at: '2026-07-15T05:24:32.279487Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Next](Updating%20Regions.md)[Previous](Working%20With%20Bitmap%20Image%20Data.md)

# Masking

In QuickDraw, masking can be accomplished using bitmaps that to determine how color information is copied from the pixels in a source image to the corresponding pixels in a destination image. Masks are passed to the QuickDraw functions `CopyMask` and `CopyDeepMask` in the `maskBits` parameter. Masks can have a depth of up to 8 bits per component.

QuickDraw uses the following compositing formula to compute the contribution of each color component in the source and destination pixels:

`(1 – mask) x source + (mask) x destination`

In this formula, the mask values are normalized to range from 0 through 1. High mask values reduce the contribution of source pixels—in effect, the mask contains “inverse alpha” information with respect to the source bitmap.

Quartz supports two kinds of masks:

- An _image mask_. This is a specialized image ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)), created by calling the function [CGImageMaskCreate](https://developer.apple.com/documentation/coregraphics/1455089-cgimagemaskcreate), that contains only inverse alpha information. Image masks can have a depth of up to 8 bits per pixel. Quartz image masks are a direct analogue of QuickDraw masks; the same compositing formula is used to apply mask values to source and destination color values, but on a per pixel basis:

  `(1 – mask) x source + (mask) x destination`

  For more information about image masks, see [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_images/dq_images.html#//apple_ref/doc/uid/TP30001066-CH212) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- A _masking image_. In Mac OS X v10.4 and later, you can mask an image with another image by calling the function [CGImageCreateWithMask](https://developer.apple.com/documentation/coregraphics/1456337-cgimagecreatewithmask) and supplying an image as the `mask` parameter rather than an image mask. Use an image as a mask when you want to achieve an effect opposite of what you get when you mask an image with an image mask. Source samples of an image that is used as a mask operate as alpha values. An image sample value (S):

  - Equal to 1 paints the corresponding image sample at full coverage.
  - Equal to 0 blocks painting the corresponding image sample.
  - Greater than 0 and less than 1 allows painting the corresponding image sample with an alpha value of S.

Starting in Mac OS X v10.4, you can use the function `CGImageCreateWithMask` to mask an image with either an image mask or an image. The function `CGImageCreateWithMaskingColors` is used for chroma key masking. Masks can also be intersected with the current clipping area in a graphics context using the function `CGContextClipToMask`.

In the QuickDraw functions `CopyBits` and `CopyDeepMask`, the mask region parameter prevents some of the pixels in the source image from being copied to the destination, similar to the clipping region in a graphics port. A procedure that uses this type of binary mask might look like this:

1. Use `CalcCMask` or `SeedCFill` to create a bitmap of the mask.
2. Use `BitmapToRegion` to create a mask region.
3. Use `CopyBits`, passing the mask region as the last parameter.

Prior to Mac OS X v10.4, there is no direct support in Quartz for combining an image with a mask at runtime. To apply a clipping mask to an image, the recommended solution is to set up the clipping area in the context before drawing the image. This approach works well whenever you can specify the shape of the clipping mask using a graphics path.

When it’s difficult to construct a path to specify the desired clip, you can use the alpha channel in an image as a built-in clipping mask. (The alpha channel is an extra component that determines the color opacity of each sample or pixel in an image. When the image is drawn, the alpha channel is used to control how the image is blended or composited with background color.) When a mask is an integral part of an image, as in a game sprite, you can use a photo editing application to transfer the mask into the alpha channel of the image permanently.

In Mac OS X v10.4, Quartz provides some new solutions for applications that need to apply clipping masks to images:

- The function [CGContextClipToMask](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask) intersects the clipping area in a context with a mask. In this solution, all subsequent drawing is affected.
- The function [CGImageCreateWithMask](https://developer.apple.com/documentation/coregraphics/1456337-cgimagecreatewithmask) combines an image with a clipping mask. The mask can be a grayscale image that serves as an alpha mask, or an Quartz image mask that contains inverse alpha information.

Both solutions use masks that are bitmap images with a pixel depth of up to 8 bits. Typically, the mask is the same size as the image to which it is applied.

For more information about using masks, see [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_images/dq_images.html#//apple_ref/doc/uid/TP30001066-CH212) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

In _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_, see:

- [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_data_mgr/dq_data_mgr.html#//apple_ref/doc/uid/TP30001066-CH216)

See these reference documents:

- _[CGContext Reference](https://developer.apple.com/documentation/coregraphics/cgcontext)_
- _[CGImage Reference](https://developer.apple.com/documentation/coregraphics/cgimage)_

[Next](Updating%20Regions.md)[Previous](Working%20With%20Bitmap%20Image%20Data.md)

