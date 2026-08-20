---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_image_data/tq_image_data.html
archived_at: '2026-07-15T05:24:32.254505Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Next](Masking.md)[Previous](Converting%20PICT%20Data.md)

# Working With Bitmap Image Data

A Quartz image ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref) data type) is an abstract representation of a bitmap image that encapsulates image data together with information about how to interpret and draw the data. A Quartz image is immutable—that is, you cannot “draw into” a Quartz image or change its attributes. You use Quartz images to work with bitmap data in a device-independent manner while taking advantage of built-in Quartz features such as color management, anti-aliasing, and interpolation.

This chapter provides strategies for performing the following tasks:

- [Moving Bits to the Screen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wueqsdizdeiqsc) outlines the functions you can use to move bits, should you really need to do so.
- [Getting Image Data and Creating an Image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wugssci5feqq2i) discusses strategies for obtaining bitmap image data.
- [Changing Pixel Depth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wueqsdi5aucrkg) discusses why changing pixel depth is not an issue in Quartz.
- [Drawing Subimages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wueqsdinbemsse) shows a variety of ways that you can use Quartz to draw a portion of an image.
- [Resizing Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wueqsdizfeiscc) gives information on changing the size or scaling of an image.

The Quartz imaging model does not provide the same sort of bit-copying functionality as QuickDraw because Quartz is not based on bitmap graphics. Most of the time you’ll want to adopt strategies that are not bit-based. However if you really need to draw bits, Quartz has the capability. To draw bits, create a bitmap graphics context and draw into it. You can then create an image from the bitmap graphics context by calling the function [CGBitmapContextCreateImage](https://developer.apple.com/documentation/coregraphics/cgcontext/1454225-makeimage) (available starting in Mac OS X v10.4). To draw the image to screen, call [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage), supplying the appropriate windows graphics context.

Drawing to a bitmap graphics context, caching the drawing to a CGImage, and then drawing the image to a window graphics context is faster than copying the bits back from the backing store. (Note that you can no longer assume that window back buffers are in main memory.) Keep in mind that the source pixels of a CGImage are immutable.

Quartz image data can originate from three types of sources: a URL that specifies a location, a CFData object, which is a simple allocated buffer, and raw data, for which you provide a pointer and a set of callbacks that take care of memory management for the data.

To obtain image data from a data source, you use either a data provider (prior to Mac OS X v10.4) or an image source (starting in Mac OS X v.10.4). You can think of data providers and image sources as “data managers.” Quartz uses a data manager to obtain the source image data. The data manager handles the messy details of supplying bytes in their correct sequence—for example, a JPEG data provider might handle the task of decompressing the image data.

Here is the general procedure for getting image data from a data source and creating an image from it:

1. Create the data manager. If your application runs only in Mac OS X v10.4, use one of the CGImageSource creation functions. If your image data is in a common format (JPEG, PNG, and so forth) you can use the function `CGImageSourceCreateWithURL`. If your image data is in a nonstandard or proprietary format, you’ll need to set up a data provider along with callbacks for managing the data. For more information, see [Data Management](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_data_mgr/dq_data_mgr.html#//apple_ref/doc/uid/TP30001066-CH216) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
2. Supply the data manager to an image creation function. If you’ve created an image source, you supply the CGImageSource object to the function [CGImageSourceCreateImageAtIndex](https://developer.apple.com/documentation/imageio/1465011-cgimagesourcecreateimageatindex). Image source indexes are zero based, so if your image file contains only one image, supply `0`. If you’ve created a data provider, you supply it as a parameter to an image creation function ([CGImageCreate](https://developer.apple.com/documentation/coregraphics/cgimage/1455149-init), [CGImageCreateWithJPEGDataProvider](https://developer.apple.com/documentation/coregraphics/cgimage/1454920-init), or [CGImageCreateWithPNGDataProvider](https://developer.apple.com/documentation/coregraphics/cgimage/1454993-init)). For a description of all the image creation functions in Quartz, see [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_images/dq_images.html#//apple_ref/doc/uid/TP30001066-CH212) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

To draw the newly created Quartz image in a graphics context, you call [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage) and specify the destination rectangle for the image. This function does not have a parameter for a source rectangle; if you want to crop the image or extract a subimage, you’ll need to write some additional code—see [Drawing Subimages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wueqsdinbemsse).

When you move image data from QuickDraw to Quartz, you might notice that the pixels in an image drawn in a Quartz graphics context look different from the pixels in the same image in QuickDraw. Changes are due to factors such as:

- Anti-aliasing around the edges of the image
- Image interpolation due to scaling
- Alpha-based blending of image pixels with background pixels
- Color matching, if the image and context color spaces are different
- Color adjustments to match the display hardware

For historical reasons, QuickDraw supports pixel formats with depths that range from 1 through 32 bits. When copying pixels between ports that have different formats and depths, the `CopyBits` function automatically converts each source pixel to the destination depth. (When the depth is reduced, `CopyBits` also uses dithering to maintain image quality.)

Applications that run on older systems can sometimes save memory and improve rendering performance by using `CopyBits` to reduce the depth of images that are drawn. Modern hardware has plenty of memory and rendering horsepower, and there is no longer any motivation to reduce image depth.

Mac OS X supports direct displays with pixel depths of 16 or 32, and Quartz bitmap contexts support 16-bit and 32-bit pixel formats. Quartz requires these higher depths to ensure that images can always be rendered faithfully on any destination device.

In QuickDraw, you can use `CopyBits` to move a rectangular section of the source pixel map to the destination pixel map. This feature allows you to crop an image by copying a subimage.

Some applications have used this feature as a way to optimize the storage, management, and retrieval of small images. These applications assemble and cache numerous small images in a single offscreen buffer and use `CopyBits` to copy them to the screen as needed. For example, a game could cache all the images used on each level of play, making image management easier and improving performance.

Unlike `CopyBits`, [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage) does not allow you to specify a source rectangle. However, there are some good solutions in Quartz for drawing subimages of larger images. In Mac OS X v10.4 and later, you can use the function [CGImageCreateWithImageInRect](https://developer.apple.com/documentation/coregraphics/cgimage/1454683-cropping) to create a subimage to draw. Otherwise, you can draw a subimage using a clip, a bitmap context, or a custom data provider.

Introduced in Mac OS X v10.4, the function [CGImageCreateWithImageInRect](https://developer.apple.com/documentation/coregraphics/cgimage/1454683-cropping) uses a source rectangle to create a subimage from an existing Quartz image. Because the subimage is also a Quartz image ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)), Quartz can cache the subimage for better drawing performance. To draw the subimage, you use the function [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage).

For more information and a code example, see [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_images/dq_images.html#//apple_ref/doc/uid/TP30001066-CH212) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

This approach draws the entire image into a graphics context and clips the drawing to get the desired subimage. As in `CopyBits`, you specify source and destination rectangles. The source rectangle defines the desired subimage, and the destination rectangle determines the clip. The full image is drawn into a third drawing rectangle, which is carefully constructed so that [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage) translates and scales the image appropriately to get the desired effect. You should specify the source rectangle in image units and the destination rectangle in user space units.

Listing 5-1 shows how you could implement this solution. A detailed explanation of each numbered line of code follows the listing.

A drawback to this approach is that clipping an image may introduce anti-aliased edges when the subimage is rendered. For information on controlling anti-aliasing in a context, see [Graphics Contexts](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_context/dq_context.html#//apple_ref/doc/uid/TP30001066-CH203) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

__Listing 5-1__  A routine that draws a subimage by clipping, translating, and scaling

```
void MyDrawSubImage (
    CGContextRef context, CGImageRef image, CGRect src, CGRect dst)
{
    /* the default drawing rectangle */
    float w = (float) CGImageGetWidth(image);
    float h = (float) CGImageGetHeight(image);
    CGRect drawRect = CGRectMake (0, 0, w, h);// 1

    if (!CGRectEqualToRect (src, dst))
    {// 2
        float sx = CGRectGetWidth(dst) / CGRectGetWidth(src);
        float sy = CGRectGetHeight(dst) / CGRectGetHeight(src);
        float dx = CGRectGetMinX(dst) - (CGRectGetMinX(src) * sx);
        float dy = CGRectGetMinY(dst) - (CGRectGetMinY(src) * sy);
        drawRect = CGRectMake (dx, dy, w*sx, h*sy);
    }

    CGContextSaveGState (context);// 3
    CGContextClipToRect (context, dst);// 4
    CGContextDrawImage (context, drawRect, image);// 5
    CGContextRestoreGState (context);
}
```

Here’s what the code does:

1. Defines the drawing rectangle. If the source and destination rectangles are identical, the default values are correct.
2. The source and destination rectangles are different, so the image needs to be scaled and translated. This code block adjusts the drawing rectangle so that [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage) performs the desired transformation; Quartz draws the image to fit the destination rectangle.
3. Pushes the current graphics state onto the state stack, in preparation for changing the clipping area.
4. Sets the clipping area to the destination rectangle.
5. Draws the image such that the desired subimage is visible in the clipping area.

You can use a bitmap context to draw a subimage by following these steps:

1. Call the function [CGBitmapContextCreate](https://developer.apple.com/documentation/coregraphics/cgcontext/1455939-init) to create a bitmap that’s large enough for the subimage data and that uses the appropriate pixel format for the source image data. The pixel format of the bitmap context must be one of the supported formats—for more information, see [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_images/dq_images.html#//apple_ref/doc/uid/TP30001066-CH212) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
2. Create a drawing rectangle. You will want to draw the image so that Quartz writes into the bitmap precisely the subimage data that’s wanted. To accomplish this, draw the full image into a rectangle of the same size, and then translate the rectangle so that the origin of the subimage is aligned with the origin in the bitmap context.
3. Draw the source image into the bitmap context by calling the function [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage). The drawing rectangle is translated such that the bitmap ends up containing precisely the pixel data in the subimage.

After drawing the source image in the bitmap context, you use the context data to create a Quartz image that represents the subimage. In Mac OS X v10.4 and later, you can use the function [CGBitmapContextCreateImage](https://developer.apple.com/documentation/coregraphics/cgcontext/1454225-makeimage) to create this image. You can draw the image in any graphics context or save it for later use.

In this method, you create a custom data provider that supplies the bytes in the subimage and use this data provider to create a Quartz image ([CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)). To use this method, you need to have direct access to the source image data.

One way to implement this method is to write a set of callback functions for a sequential-access data provider. Your `GetBytes` callback function needs to extract the pixel values in a subimage from the full bitmap and supply these bytes to the caller. When you create a data provider that uses your callbacks, you can also pass private information, such as the base address of the bitmap and the subimage rectangle. Quartz passes this information to your callbacks.

For each different subimage you want to draw, be sure to create a new data provider, and a new Quartz image to represent the subimage.

In QuickDraw, the `CopyBits` function is often used to change the size or scale of an image, vertically or horizontally or both. Pixels are averaged during shrinking.

In Quartz, you can resize an image by drawing the image into a smaller or larger destination rectangle. Given the dimensions of the source image, you compute the dimensions of the destination rectangle needed to achieve the desired scaling. Then you use [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage) to draw the image in the destination rectangle.

Quartz also allows you to scale (as well as rotate, skew, and translate) all subsequent drawing in a graphics context—including images—using an affine transformation.

Quartz draws images using an interpolation (or pixel-smoothing) algorithm that provides high-quality results when the image is scaled. When you create a Quartz image, you specify whether interpolation should be used when the image is drawn in a Quartz context. You can also use the function [CGContextSetInterpolationQuality](https://developer.apple.com/documentation/coregraphics/1455656-cgcontextsetinterpolationquality) to set the level of interpolation quality in the context. This parameter is merely a hint to the context—not all contexts support all interpolation quality levels.

In _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_, see:

- [Bitmap Images and Image Masks](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_images/dq_images.html#//apple_ref/doc/uid/TP30001066-CH212), which shows how to work with images and image masks.
- [Data Management](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_data_mgr/dq_data_mgr.html#//apple_ref/doc/uid/TP30001066-CH216), which discusses strategies for getting data into and out of Quartz using data providers, image sources, and image destinations.

See these reference documents:

- _[CGImage Reference](https://developer.apple.com/documentation/coregraphics/cgimage)_
- _[CGImageDestination Reference](https://developer.apple.com/documentation/imageio/cgimagedestination)_
- _[CGImageSource Reference](https://developer.apple.com/documentation/imageio/cgimagesource-r84)_
- _[CGDataConsumer Reference](https://developer.apple.com/documentation/coregraphics/cgdataconsumer)_
- _[CGDataProvider Reference](https://developer.apple.com/documentation/coregraphics/cgdataprovider)_

[Next](Masking.md)[Previous](Converting%20PICT%20Data.md)

