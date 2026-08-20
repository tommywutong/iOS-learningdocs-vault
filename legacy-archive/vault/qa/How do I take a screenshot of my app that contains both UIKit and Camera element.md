---
title: How do I take a screenshot of my app that contains both UIKit and Camera elements?
apple_id: DTS40010302
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: null
published: '2013-05-14'
source_url: https://developer.apple.com/library/archive/qa/qa1714/_index.html
archived_at: '2026-07-18T02:34:27.155917Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1714

# How do I take a screenshot of my app that contains both UIKit and Camera elements?

## Q:  How do I programmatically take a screenshot of my app that contains both UIKit and Camera elements?

A: As described in _[Screen Capture in UIKit Applications](https://developer.apple.com/library/archive/qa/qa1703/_index.html#//apple_ref/doc/uid/DTS40010193)_, the `-[CALayer renderInContext:]` method lets you render a layer and its sublayers to a graphics context. However, it does not render the content from the camera that is being displayed on the screen. To capture both the camera content and the overlay view, you need to:

1. Capture the contents of your camera view as described in _[How to capture video frames from the camera as images using AV Foundation on iOS](https://developer.apple.com/library/archive/qa/qa1702/_index.html#//apple_ref/doc/uid/DTS40010192)_ or by using `UIImagePickerController's` methods _[(UIImagePickerController Class Reference)](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)_ to take a picture.
2. Draw that captured camera content yourself into the graphics context that you are rendering your UIKit elements.

__Listing 1__  Capturing an image using AV Foundation as described in Technical Q&A QA1702 and then drawing the camera overlay view on top of it

```objc
// Render the UIView into the CGContextRef using the
// -[CALayer renderInContext:] method
- (void)renderView:(UIView*)view inContext:(CGContextRef)context
{
    // -renderInContext: renders in the coordinate space of the layer,
    // so we must first apply the layer's geometry to the graphics context
    CGContextSaveGState(context);
    // Center the context around the window's anchor point
    CGContextTranslateCTM(context, [view center].x, [view center].y);
    // Apply the window's transform about the anchor point
    CGContextConcatCTM(context, [view transform]);
    // Offset by the portion of the bounds left of and above the anchor point
    CGContextTranslateCTM(context,
                          -[view bounds].size.width * [[view layer] anchorPoint].x,
                          -[view bounds].size.height * [[view layer] anchorPoint].y);

    // Render the layer hierarchy to the current context
    [[view layer] renderInContext:context];

    // Restore the context
    CGContextRestoreGState(context);
}

// capture the camera content using AV Foundation as described in Technical Q&A QA1702
// Delegate routine that is called when a sample buffer was written
- (void)captureOutput:(AVCaptureOutput *)captureOutput
didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer
       fromConnection:(AVCaptureConnection *)connection
{
    // Create a UIImage from the sample buffer data
    UIImage *image = [self imageFromSampleBuffer:sampleBuffer];

    // Create a graphics context with the target size
    CGSize imageSize = [[UIScreen mainScreen] bounds].size;
    UIGraphicsBeginImageContextWithOptions(imageSize, NO, 0);

    CGContextRef context = UIGraphicsGetCurrentContext();


    // Draw the image returned by the camera sample buffer into the context.
    // Draw it into the same sized rectangle as the view that is displayed on the screen.
    float menubarUIOffset = 44.0;
    UIGraphicsPushContext(context);
    [image drawInRect:CGRectMake(0, 0, imageSize.width, imageSize.height-menubarUIOffset)];
    UIGraphicsPopContext();


    // Render the camera overlay view into the graphic context that we created above.
    [self renderView:overlay.view inContext:context];

    // Retrieve the screenshot image containing both the camera content and the overlay view
    UIImage *screenshot = UIGraphicsGetImageFromCurrentImageContext();

    UIGraphicsEndImageContext();

}
```


__Listing 2__  Capturing an image using UIImagePickerController and then drawing the camera overlay view on top of it

```objc
// Render the UIView into the CGContextRef using the
// CALayer/-renderInContext: method
- (void)renderView:(UIView*)view inContext:(CGContextRef)context
{
    // -renderInContext: renders in the coordinate space of the layer,
    // so we must first apply the layer's geometry to the graphics context
    CGContextSaveGState(context);
    // Center the context around the window's anchor point
    CGContextTranslateCTM(context, [view center].x, [view center].y);
    // Apply the window's transform about the anchor point
    CGContextConcatCTM(context, [view transform]);
    // Offset by the portion of the bounds left of and above the anchor point
    CGContextTranslateCTM(context,
                          -[view bounds].size.width * [[view layer] anchorPoint].x,
                          -[view bounds].size.height * [[view layer] anchorPoint].y);

    // Render the layer hierarchy to the current context
    [[view layer] renderInContext:context];

    // Restore the context
    CGContextRestoreGState(context);
}

// this get called when an image has been taken from the camera
- (void)imagePickerController:(UIImagePickerController *)picker didFinishPickingMediaWithInfo:(NSDictionary *)info
{
    UIImage *image = [info valueForKey:UIImagePickerControllerOriginalImage];

    CGSize imageSize = [[UIScreen mainScreen] bounds].size;
    if (NULL != UIGraphicsBeginImageContextWithOptions)
        UIGraphicsBeginImageContextWithOptions(imageSize, NO, 0);
    else
        UIGraphicsBeginImageContext(imageSize);

    CGContextRef context = UIGraphicsGetCurrentContext();


    // Draw the image returned by the camera sample buffer into the context.
    // Draw it into the same sized rectangle as the view that is displayed on the screen.
    float menubarUIOffset = 44.0;
    UIGraphicsPushContext(context);
    [image drawInRect:CGRectMake(0, 0, imageSize.width, imageSize.height-menubarUIOffset)];
    UIGraphicsPopContext();

    // Render the camera overlay view into the graphic context that we created above.
    [self renderView:overlay.view inContext:context];

    // Retrieve the screenshot image containing both the camera content and the overlay view
    UIImage *screenshot = UIGraphicsGetImageFromCurrentImageContext();

    UIGraphicsEndImageContext();

}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-05-14 | Minor Content Update. |
| 2010-09-09 | New document that demonstrates how to take a screenshot in app that contains both UIKit and Camera elements. |

