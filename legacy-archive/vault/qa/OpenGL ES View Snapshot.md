---
title: OpenGL ES View Snapshot
apple_id: DTS40010204
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/qa/qa1704/_index.html
archived_at: '2026-07-18T02:34:14.702651Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1704

# OpenGL ES View Snapshot

## Q:  How do I take a snapshot of my OpenGL ES view and save the result in a UIImage?

A: The OpenGL ES commands issued by your application are sent to the current rendering context (an `EAGLContext` object) which contains state information of your rendering target. To take a snapshot of your OpenGL ES view, make sure you bind to the correct context and framebuffer, and then call `glReadPixels` to obtain the pixel data from the framebuffer. You can then create a `CGImage` with the pixel data, and then a `UIImage` out of the `CGImage`.

The UIKit coordinate system (y down) is upside down to the OpenGL ES and Quartz coordinate system (y up). You should take this into account when creating the `UIImage` from the `CGImage`. In the following listing, we demonstrate how to create a flipped bitmap context using UIGraphics calls and then render the original image to it.

On iOS 4 and later, `UIGraphicsBeginImageContextWithOptions` allows you to provide with a scale factor. When setting it to your OpenGL ES view's `contentScaleFactor` property value and it is greater than 1.0, you will get the sharp, high-resolution snapshot for your OpenGL ES drawing. On iOS prior to 4, the code falls back to use `UIGraphicsBeginImageContext`.

By default, the contents of a renderbuffer are invalidated after you present them to the display. Therefore, to get defined results when reading your OpenGL ES content, you must do one of the following:

1) Call `glReadPixels` __before__ calling `EAGLContext/-presentRenderbuffer:`, or

2) Set the `CAEAGLLayer`'s retained backing property to true to retain the contents of the layer. However, this can have adverse performance implications so you are cautioned to use this setting only when necessary.

The above restrictions do not apply for offscreen, non-displayable framebuffers.

__Listing 1__  OpenGL ES view snapshot

```objc
// IMPORTANT: Call this method after you draw and before -presentRenderbuffer:.
- (UIImage*)snapshot:(UIView*)eaglview
{
    GLint backingWidth, backingHeight;

    // Bind the color renderbuffer used to render the OpenGL ES view
    // If your application only creates a single color renderbuffer which is already bound at this point,
    // this call is redundant, but it is needed if you're dealing with multiple renderbuffers.
    // Note, replace "_colorRenderbuffer" with the actual name of the renderbuffer object defined in your class.
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, _colorRenderbuffer);

    // Get the size of the backing CAEAGLLayer
    glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_WIDTH_OES, &backingWidth);
    glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_HEIGHT_OES, &backingHeight);

    NSInteger x = 0, y = 0, width = backingWidth, height = backingHeight;
    NSInteger dataLength = width * height * 4;
    GLubyte *data = (GLubyte*)malloc(dataLength * sizeof(GLubyte));

    // Read pixel data from the framebuffer
    glPixelStorei(GL_PACK_ALIGNMENT, 4);
    glReadPixels(x, y, width, height, GL_RGBA, GL_UNSIGNED_BYTE, data);

    // Create a CGImage with the pixel data
    // If your OpenGL ES content is opaque, use kCGImageAlphaNoneSkipLast to ignore the alpha channel
    // otherwise, use kCGImageAlphaPremultipliedLast
    CGDataProviderRef ref = CGDataProviderCreateWithData(NULL, data, dataLength, NULL);
    CGColorSpaceRef colorspace = CGColorSpaceCreateDeviceRGB();
    CGImageRef iref = CGImageCreate(width, height, 8, 32, width * 4, colorspace, kCGBitmapByteOrder32Big | kCGImageAlphaPremultipliedLast,
                                    ref, NULL, true, kCGRenderingIntentDefault);

    // OpenGL ES measures data in PIXELS
    // Create a graphics context with the target size measured in POINTS
    NSInteger widthInPoints, heightInPoints;
    if (NULL != UIGraphicsBeginImageContextWithOptions) {
        // On iOS 4 and later, use UIGraphicsBeginImageContextWithOptions to take the scale into consideration
        // Set the scale parameter to your OpenGL ES view's contentScaleFactor
        // so that you get a high-resolution snapshot when its value is greater than 1.0
        CGFloat scale = eaglview.contentScaleFactor;
        widthInPoints = width / scale;
        heightInPoints = height / scale;
        UIGraphicsBeginImageContextWithOptions(CGSizeMake(widthInPoints, heightInPoints), NO, scale);
    }
    else {
        // On iOS prior to 4, fall back to use UIGraphicsBeginImageContext
        widthInPoints = width;
        heightInPoints = height;
        UIGraphicsBeginImageContext(CGSizeMake(widthInPoints, heightInPoints));
    }

    CGContextRef cgcontext = UIGraphicsGetCurrentContext();

    // UIKit coordinate system is upside down to GL/Quartz coordinate system
    // Flip the CGImage by rendering it to the flipped bitmap context
    // The size of the destination area is measured in POINTS
    CGContextSetBlendMode(cgcontext, kCGBlendModeCopy);
    CGContextDrawImage(cgcontext, CGRectMake(0.0, 0.0, widthInPoints, heightInPoints), iref);

    // Retrieve the UIImage from the current context
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();

    UIGraphicsEndImageContext();

    // Clean up
    free(data);
    CFRelease(ref);
    CFRelease(colorspace);
    CGImageRelease(iref);

    return image;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-09-19 | Minor format changes. |
| 2011-03-30 | Added comments about binding the color renderbuffer. |
| 2010-07-26 | New document that demonstrates how to take a snapshot of an OpenGL ES view. |

