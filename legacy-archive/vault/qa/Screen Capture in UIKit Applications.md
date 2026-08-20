---
title: Screen Capture in UIKit Applications
apple_id: DTS40010193
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: null
published: '2011-03-28'
source_url: https://developer.apple.com/library/archive/qa/qa1703/_index.html
archived_at: '2026-07-18T02:34:14.636699Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1703

# Screen Capture in UIKit Applications

## Q:  How do I take a screenshot in my UIKit application?

A: Every `UIWindow` (inherited from `UIView`) and `UIView` is backed by a CALayer. The `CALayer/-renderInContext:` method lets you render a layer and its sublayers to a graphics context. So, to grab a snapshot of the entire screen, you can iterate through each window on the screen and render its layer hierarchy to a destination context. Once finished you can get the screenshot image via the `UIGraphicsGetImageFromCurrentImageContext` function, as shown below.

Note that, `CALayer/-renderInContext:` captures only your UIKit and Quartz drawing. It does not capture OpenGL ES or video content. See the following Q&A's for how to capture OpenGL ES and camera content using relevant techniques:

[OpenGL ES View Snapshot](https://developer.apple.com/library/ios/#qa/qa1704/_index.html)

[How to capture video frames from the camera as images using AV Foundation](https://developer.apple.com/library/ios/#qa/qa1702/_index.html)

[How do I take a screenshot of my app that contains both UIKit and Camera elements](https://developer.apple.com/library/ios/#qa/qa1714/_index.html)

To use Core Animation APIs, you need to add the QuartzCore framework in your Xcode project and include the QuartzCore header as shown in the following listing:

__Listing 1__  Include the QuartzCore header

```objc
#import <QuartzCore/QuartzCore.h>
```


__Listing 2__  Get a screenshot image

```objc
- (UIImage*)screenshot
{
    // Create a graphics context with the target size
    // On iOS 4 and later, use UIGraphicsBeginImageContextWithOptions to take the scale into consideration
    // On iOS prior to 4, fall back to use UIGraphicsBeginImageContext
    CGSize imageSize = [[UIScreen mainScreen] bounds].size;
    if (NULL != UIGraphicsBeginImageContextWithOptions)
        UIGraphicsBeginImageContextWithOptions(imageSize, NO, 0);
    else
        UIGraphicsBeginImageContext(imageSize);

    CGContextRef context = UIGraphicsGetCurrentContext();

    // Iterate over every window from back to front
    for (UIWindow *window in [[UIApplication sharedApplication] windows])
    {
        if (![window respondsToSelector:@selector(screen)] || [window screen] == [UIScreen mainScreen])
        {
            // -renderInContext: renders in the coordinate space of the layer,
            // so we must first apply the layer's geometry to the graphics context
            CGContextSaveGState(context);
            // Center the context around the window's anchor point
            CGContextTranslateCTM(context, [window center].x, [window center].y);
            // Apply the window's transform about the anchor point
            CGContextConcatCTM(context, [window transform]);
            // Offset by the portion of the bounds left of and above the anchor point
            CGContextTranslateCTM(context,
                                  -[window bounds].size.width * [[window layer] anchorPoint].x,
                                  -[window bounds].size.height * [[window layer] anchorPoint].y);

            // Render the layer hierarchy to the current context
            [[window layer] renderInContext:context];

            // Restore the context
            CGContextRestoreGState(context);
        }
    }

    // Retrieve the screenshot image
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();

    UIGraphicsEndImageContext();

    return image;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-03-28 | Added links to other screenshot Q&A's. Pointed out that one needs to add the QuartzCore framework and include the QuartzCore header to use Core Animation APIs. |
| 2010-07-19 | New document that demonstrates how to take a screenshot in an UIKit application |

