---
title: Getting images in and out of Quartz Composer compositions
apple_id: DTS10003731
resource_type: Technical Note
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2012-03-06'
source_url: https://developer.apple.com/library/archive/technotes/tn2143/_index.html
archived_at: '2026-07-26T19:54:08.458855Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2143

# Getting images in and out of Quartz Composer compositions

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Quartz Composer compositions can have inputs and outputs to pass and retrieve values to and from the composition. Those inputs are typed and accept numerical values, text strings or even images (refer to the [Quartz Composer Programming Guide](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Conceptual/QuartzComposer/qc_intro/qc_intro.html) for more information on compositions inputs and outputs and regarding how to create them). This technote focuses on how to pass and retrieve efficiently images to a composition.

[Passing images to a composition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewugsbrfvke4vcbi4yq)[NSImage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewugsbrfvke4vcbi4za)[CGImageRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewugsbrfvke4vcbi4zq)[CIImage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewugsbrfvke4vcbi42q)[CVImageBuffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewugsbrfvke4vcbi43a)[Retrieving images from a composition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewugsbrfvke4vcbi43q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnztgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Passing images to a composition

If the composition has Image inputs, you can pass images to them using the - (BOOL) setValue:(id)value forInputKey:(NSString\*)key method from the QCView or QCRenderer classes. You must pass a Quartz Composer compatible type of image. This method will return YES if it can successfully set the image on the input. Quartz Composer will retain the image you pass so you can safely release it afterwards.

Compatible types of images are:

- NSImage from AppKit (see [NSImage Reference](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/ApplicationKit/Classes/NSImage_Class/Reference/Reference.html))
- CGImageRef from Quartz 2D (see [CGImage Reference](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/CGImage/Reference/reference.html))
- CIImage from Core Image (see [CIImage Reference](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/QuartzCoreFramework/Classes/CIImage_Class/Reference/Reference.html))
- CVImageBuffer from Core Video (see [CVImageBuffer Reference](https://developer.apple.com/library/IOS/#documentation/QuartzCore/Reference/CVImageBufferRef/Reference/reference.html))

__Important:__ Always try to pass images using the closest type from their original sources as this will improve performances e.g. don't convert a CGImageRef to a CIImage or NSImage to pass it to Quartz Composer. Instead, pass the original CGImageRef directly.

Images passed to Quartz Composer as NSImages or CGImageRefs will be resized to fit in the maximum texture size on the video card (typically 2048x2048 or more). On the other hand, CIImages and CVImageBuffers bigger than the maximum texture size are not resized and may fail to display properly.

Depending on where the images to pass to Quartz Composer come from, you should use the following types:

### NSImage

Use NSImage to pass images obtained from AppKit. Note that calling -valueForInputKey:(NSString\*)key on an Image input after a call to -setValue:(id)value forInputKey:(NSString\*)key passing a NSImage, will return a different NSImage instance. The reason is that Quartz Composer performs several operations on the original NSImage like color correction or downsampling when necessary.

__Warning:__ There is an issue in Quartz Composer when passing a NSImage, that can cause its color profile information to be lost, producing a slight hue shift in the image's pixels. This is especially visible when passing / retrieving an image as an NSImage several times to / from Quartz Composer. As a consequence, NSImages should not be used to pass images to Quartz Composer when color fidelity matters (use CGImageRef instead).

### CGImageRef

Use CGImageRef when loading image files from disk through ImageIO (see /System/Library/Frameworks/ApplicationServices.framework/Frameworks/ImageIO.framework), obtaining images directly from the Quartz 2D API, or to pass raw pixels data that needs color matching.

__Listing 1__  Creating a CGImageRef from binary data or a file using ImageIO.

```
CGImageRef CreateCGImageFromData(NSData* data)
{
    CGImageRef				imageRef = NULL;
    CGImageSourceRef	sourceRef;

    sourceRef = CGImageSourceCreateWithData((CFDataRef)data, NULL);
    if(sourceRef) {
        imageRef = CGImageSourceCreateImageAtIndex(sourceRef, 0, NULL);
        CFRelease(sourceRef);
    }

    return imageRef;
}

CGImageRef CreateCGImageFromFile(NSString* path)
{
    NSURL*						url = [NSURL fileURLWithPath:path];
    CGImageRef				imageRef = NULL;
    CGImageSourceRef	sourceRef;

    sourceRef = CGImageSourceCreateWithURL((CFURLRef)url, NULL);
    if(sourceRef) {
        imageRef = CGImageSourceCreateImageAtIndex(sourceRef, 0, NULL);
        CFRelease(sourceRef);
    }

    return imageRef;
}
```

### CIImage

Use CIImage for images resulting from Core Image filters.

__Important:__ Do not wrap CGImageRefs, CVImageBuffers, raw pixels data or OpenGL textures into CIImages to pass them to Quartz Composer as this will lead to a performance hit.

### CVImageBuffer

Use CVImageBuffer for images coming from QuickTime movies, OpenGL rendering or raw pixels data. They are the optimal way to pass images from the following sources:

- QuickTime movies: create a visual context to render the movie into using the QuickTime 7 APIs (see the [QuickTime resources page](https://developer.apple.com/quicktime/)). Then pass the CVImageBuffers obtained by QTVisualContextCopyImageForTime() to the appropriate composition's Image input and release them. For best performances, it's highly recommended to use a QuickTime OpenGL texture context that uses the same OpenGL context and pixel format as a the ones used to render the composition (assuming a QCRenderer is used, as the QCView does not provide this information).
- OpenGL rendering: create a CVOpenGLBufferRef with CVOpenGLBufferCreate(), attach it to an OpenGL context with CVOpenGLBufferAttach(), perform some OpenGL rendering in that context, then call glFlush() to terminate rendering, and eventually pass the CVOpenGLBufferRef to the appropriate composition's Image input and release it (see [Core Video Reference](https://developer.apple.com/library/ios/#documentation/CoreVideo/Reference/CVFrameworkRef/_index.html) for more information on the CVOpenGLBufferRef API).
- Raw pixel data: create a CVPixelBufferRef with CVPixelBufferCreate() using a pixel format like k32ARGBPixelFormat or k8IndexedGrayPixelFormat for example (planar pixel buffers are not supported by Quartz Composer). Then write to the pixels directly using CVPixelBufferLockBaseAddress(), CVPixelBufferGetBaseAddress() and CVPixelBufferGetBytesPerRow() (don't forget to call CVPixelBufferUnlockBaseAddress() when done), and eventually pass the CVPixelBufferRef to the appropriate composition's Image input and release it (see [Core Video Reference](https://developer.apple.com/library/ios/#documentation/CoreVideo/Reference/CVFrameworkRef/_index.html) for more information on the CVPixelBufferRef API).

Creating and destroying CVOpenGLBufferRefs or CVPixelBufferRef can be a fairly expensive operation. If those buffers have constant dimensions, it's more efficient to recycle them and use appropriate buffer pools like CVOpenGLBufferPoolRef and CVPixelBufferPoolRef (see [Core Video Reference](https://developer.apple.com/library/ios/#documentation/CoreVideo/Reference/CVFrameworkRef/_index.html) for more information on the CVOpenGLBufferPoolRef and CVPixelBufferPoolRef APIs).

__Note:__ Quartz Composer considers the contents of CVImageBuffers immutable, therefor you should not attempt to modify them after passing them to Quartz Composer.

You can find sample code on how to use CVImageBuffers with Quartz Composer at /Developer/Examples/Quartz Composer/Performer.

[Back to Top](#)

## Retrieving images from a composition

If the composition has Image outputs, you can retrieve the images on them using the - (id) valueForOutputKey:(NSString\*)key method from the QCView or QCRenderer classes. This method will return the image as a NSImage or nil if there is none (or in case of an internal error). Note that -valueForOutputKey: returns a new NSImage instance each time the image on the output has changed, so you can safely retain them, and not copy them, if you need to keep around previous versions of those images.

__Note:__ The NSImages produced by Quartz Composer are in RGB format (even the ones resulting from gray-level images), and use the display colorspace.

You can pass that NSImage to a NSImageView to display it in the user interface. The NSImage can also be saved as a LZW-compressed TIFF file using the following code snippet:

__Listing 2__  Saving an NSImage as a LZW-compressed TIFF file.

```
NSImage*					image;
BOOL						success;

image = [myRenderer valueForOutputKey:@"foo"];
if(image) {
    success = [[image TIFFRepresentationUsingCompression:NSTIFFCompressionLZW factor:1.0]
        writeToFile:@"/Users/foo/bar.tiff" atomically:YES];
    if(success == NO) {
        /*
            Handle error
        */
    }
}
```

If you need to access the raw pixels contents of the NSImage, you will need to convert it to a NSBitmapImageRep using a technique like the one in this code snippet:

__Listing 3__  Accessing the raw pixels of an NSImage.

```
NSImage*					image;
NSSize						imageSize;
NSBitmapImageRep*	bitmapImage;
NSRect						imageRect;

image = [myRenderer valueForOutputKey:@"foo"];
if(image) {
    imageSize = [image size];
    imageRect = NSMakeRect(0, 0, imageSize.width, imageSize.height);
    [image lockFocus];
    bitmapImage = [[NSBitmapImageRep alloc] initWithFocusedViewRect:imageRect];
    [image unlockFocus];

    if(bitmapImage) {
        /*
            Do something with the raw pixels contents
            using [bitmapImage bitmapData] and [bitmapImage bytesPerRow]
        */
        [bitmapImage release];
    }
}
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-03-06 | Fixed links. |
| 2005-10-04 | Fixed a typo in the NSImage to NSBitmapImageRep conversion code. |
| 2005-06-24 | New document that describes how to efficiently pass images into and out of Quartz Composer |

