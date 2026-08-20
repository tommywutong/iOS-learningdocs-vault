---
title: 'ImageBrowserViewAppearance: Customizing IKImageBrowserView'
apple_id: DTS40009013
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/ImageBrowserViewAppearance/Listings/ImageBrowserAppearance_ImageBrowserBackgroundLayer_m.html
archived_at: '2026-07-18T03:12:22.792125Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImageBrowserViewAppearance: Customizing IKImageBrowserView](ImageBrowserViewAppearance-%20Customizing%20IKImageBrowserView.md)


[Next](ImageBrowserAppearance-ImageBrowserCell.m.md)[Previous](ImageBrowserAppearance-ImageBrowserView.m.md)

# ImageBrowserAppearance/ImageBrowserBackgroundLayer.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 IKImageBrowserView's background CALayer subclass for drawing a custom background image.
 */

#import "ImageBrowserBackgroundLayer.h"

@implementation ImageBrowserBackgroundLayer

// -------------------------------------------------------------------------
//    init
// -------------------------------------------------------------------------
- (instancetype)init
{
    self = [super init];
    if (self != nil)
    {
        // Needs to redraw when bounds change.
        [self setNeedsDisplayOnBoundsChange:YES];
    }

    return self;
}

// -------------------------------------------------------------------------
//    actionForKey:
//
//    Always return nil, to never animate.
// -------------------------------------------------------------------------
- (id<CAAction>)actionForKey:(NSString *)event
{
    return nil;
}

// -------------------------------------------------------------------------
//    drawInContext:
//
//    Draw a metal background that scrolls when the image browser scroll.
// -------------------------------------------------------------------------
- (void)drawInContext:(CGContextRef)context
{
    // Retreive bounds and visible rect.
    NSRect visibleRect = self.owner.visibleRect;
    NSRect bounds = self.owner.bounds;

    // Retreive background image from our bundle.
    NSURL *urlForImage =
        [[NSBundle mainBundle] URLForResource:@"metal_background" withExtension:@"tif"];
    CGImageSourceRef imageSource = CGImageSourceCreateWithURL((CFURLRef)urlForImage, NULL);
    if (imageSource != nil)
    {
        CGImageRef image = CGImageSourceCreateImageAtIndex(imageSource, 0, NULL);
        if (image != nil)
        {
            float width = (float) CGImageGetWidth(image);
            float height = (float) CGImageGetHeight(image);

            // Compute coordinates to fill the view.
            float left, top, right, bottom;

            top = bounds.size.height - NSMaxY(visibleRect);
            top = fmod(top, height);
            top = height - top;

            right = NSMaxX(visibleRect);
            bottom = -height;

            // Tile the image and take in account the offset to 'emulate' a scrolling background.
            for (top = visibleRect.size.height-top; top>bottom; top -= height)
            {
                for (left = 0; left < right; left += width)
                {
                    CGContextDrawImage(context, CGRectMake(left, top, width, height), image);
                }
            }
            CFRelease(image);
        }
        CFRelease(imageSource);
    }
}

@end
```

[Next](ImageBrowserAppearance-ImageBrowserCell.m.md)[Previous](ImageBrowserAppearance-ImageBrowserView.m.md)

