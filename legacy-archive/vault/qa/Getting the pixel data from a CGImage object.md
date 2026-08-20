---
title: Getting the pixel data from a CGImage object
apple_id: DTS10004216
resource_type: QA
platform: watchOS|iOS|macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2008-08-27'
source_url: https://developer.apple.com/library/archive/qa/qa1509/_index.html
archived_at: '2026-07-18T02:31:40.455324Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1509

# Getting the pixel data from a CGImage object

## Q:  How do I access the pixel data of a `CGImage` object?

A: How do I access the pixel data of a `CGImage` object?

On Mac OS X 10.5 or later, a new call has been added that allows you to obtain the actual pixel data from a `CGImage` object. This call, `CGDataProviderCopyData`, returns a CFData object that contains the pixel data from the image in question. An example of using this call to obtain pixel data from a `CGImage` is shown in Listing 1. Once you have the CFData object with your pixel information, you can call `CFDataGetBytePtr` to get a pointer to the pixel data, or `CFDataGetBytes` to copy a subrange of pixel data.

__Listing 1__  Getting raw pixel data from a `CGImage`.

```
CFDataRef CopyImagePixels(CGImageRef inImage) {     return CGDataProviderCopyData(CGImageGetDataProvider(inImage)); }
```

Prior to Mac OS X 10.5 an image's pixels are not as readily available. The only way to guarantee access to the equivalent bits is to create a bitmap context with a memory buffer you specify and then draw the `CGImage` to the context using `CGContextDrawImage`. After drawing the `CGImage` to the context you will have a copy of the data in the buffer you specified (which can also be easily accessed using the `CGBitmapContexGetData` function). The code in Listing 2 demonstrates how to do this.

For more information about creating bitmap contexts for other pixel formats, see the [Quartz 2D Programming Guide](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/index.html).

__Listing 2__  Accessing the pixel data of a `CGImage`.

```
void ManipulateImagePixelData(CGImageRef inImage) {     // Create the bitmap context     CGContextRef cgctx = CreateARGBBitmapContext(inImage);     if (cgctx == NULL)      {          // error creating context         return;     }       // Get image width, height. We'll use the entire image.     size_t w = CGImageGetWidth(inImage);     size_t h = CGImageGetHeight(inImage);     CGRect rect = {{0,0},{w,h}};       // Draw the image to the bitmap context. Once we draw, the memory      // allocated for the context for rendering will then contain the      // raw image data in the specified color space.     CGContextDrawImage(cgctx, rect, inImage);       // Now we can get a pointer to the image data associated with the bitmap     // context.     void *data = CGBitmapContextGetData (cgctx);     if (data != NULL)     {          // **** You have a pointer to the image data ****          // **** Do stuff with the data here ****      }      // When finished, release the context     CGContextRelease(cgctx);      // Free image data memory for the context     if (data)     {         free(data);     }  }  CGContextRef CreateARGBBitmapContext (CGImageRef inImage) {     CGContextRef    context = NULL;     CGColorSpaceRef colorSpace;     void *          bitmapData;     int             bitmapByteCount;     int             bitmapBytesPerRow;       // Get image width, height. We'll use the entire image.     size_t pixelsWide = CGImageGetWidth(inImage);     size_t pixelsHigh = CGImageGetHeight(inImage);      // Declare the number of bytes per row. Each pixel in the bitmap in this     // example is represented by 4 bytes; 8 bits each of red, green, blue, and     // alpha.     bitmapBytesPerRow   = (pixelsWide * 4);     bitmapByteCount     = (bitmapBytesPerRow * pixelsHigh);      // Use the generic RGB color space.     colorSpace = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB);     if (colorSpace == NULL)     {         fprintf(stderr, "Error allocating color space\n");         return NULL;     }      // Allocate memory for image data. This is the destination in memory     // where any drawing to the bitmap context will be rendered.     bitmapData = malloc( bitmapByteCount );     if (bitmapData == NULL)      {         fprintf (stderr, "Memory not allocated!");         CGColorSpaceRelease( colorSpace );         return NULL;     }      // Create the bitmap context. We want pre-multiplied ARGB, 8-bits      // per component. Regardless of what the source image format is      // (CMYK, Grayscale, and so on) it will be converted over to the format     // specified here by CGBitmapContextCreate.     context = CGBitmapContextCreate (bitmapData,                                     pixelsWide,                                     pixelsHigh,                                     8,      // bits per component                                     bitmapBytesPerRow,                                     colorSpace,                                     kCGImageAlphaPremultipliedFirst);     if (context == NULL)     {         free (bitmapData);         fprintf (stderr, "Context not created!");     }      // Make sure and release colorspace before returning     CGColorSpaceRelease( colorSpace );      return context; }
```


- [Quartz 2D Programming Guide](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/index.html)
- [Technical Q&A QA1037, 'CGBitmapContextCreate Supported Color Spaces'](https://developer.apple.com/qa/qa2001/qa1037.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-27 | Updated to refer to CGDataProviderCopyData(), available as of Mac OS X 10.5. |
| 2007-03-05 | New document that describes how to access the pixel data of a CGImage object |

