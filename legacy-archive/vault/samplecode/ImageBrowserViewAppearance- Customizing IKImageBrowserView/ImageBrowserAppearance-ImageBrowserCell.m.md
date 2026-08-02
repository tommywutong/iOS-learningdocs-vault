---
title: 'ImageBrowserViewAppearance: Customizing IKImageBrowserView'
apple_id: DTS40009013
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/ImageBrowserViewAppearance/Listings/ImageBrowserAppearance_ImageBrowserCell_m.html
archived_at: '2026-07-18T03:12:22.925102Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImageBrowserViewAppearance: Customizing IKImageBrowserView](ImageBrowserViewAppearance-%20Customizing%20IKImageBrowserView.md)


[Next](ImageBrowserAppearance-ImageBrowserController.m.md)[Previous](ImageBrowserAppearance-ImageBrowserBackgroundLayer.m.md)

# ImageBrowserAppearance/ImageBrowserCell.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 IKImageBrowserView's IKImageBrowserCell subclass for drawing its fancy appearance.
 */

#import "ImageBrowserCell.h"

//---------------------------------------------------------------------------------
// setBundleImageOnLayer
//
// Utility function that creates, and sets the image (from the bundle) on the layer.
//---------------------------------------------------------------------------------
static void setBundleImageOnLayer(CALayer *layer, CFStringRef imageName)
{
    CGImageRef image = NULL;
    NSString *path =
        [[NSBundle mainBundle] pathForResource:((__bridge NSString *)imageName).stringByDeletingPathExtension
                                        ofType:((__bridge NSString *)imageName).pathExtension];
    if (!path)
    {
        return;
    }

    CGImageSourceRef imageSource = CGImageSourceCreateWithURL((CFURLRef)[NSURL fileURLWithPath:path], NULL);
    if (!imageSource)
    {
        return;
    }

    image = CGImageSourceCreateImageAtIndex(imageSource, 0, NULL);
    if (!image)
    {
        CFRelease(imageSource);
        return;
    }

    layer.contents = (__bridge id)image;

    CFRelease(imageSource);
    CFRelease(image);
}


#pragma mark -

@implementation ImageBrowserCell

//---------------------------------------------------------------------------------
// layerForType:
//
// Provides the layers for the given types.
//---------------------------------------------------------------------------------
- (CALayer *)layerForType:(NSString*) type
{
    CGColorRef color;

    // retrieve some usefull rects
    NSRect frame = [self frame];
    NSRect imageFrame = [self imageFrame];
    NSRect relativeImageFrame =
        NSMakeRect(imageFrame.origin.x - frame.origin.x,
                   imageFrame.origin.y - frame.origin.y,
                   imageFrame.size.width,
                   imageFrame.size.height);

    // place holder layer
    if (type == IKImageBrowserCellPlaceHolderLayer)
    {
        // create a place holder layer
        CALayer *layer = [CALayer layer];
        layer.frame = CGRectMake(0, 0, frame.size.width, frame.size.height);

        CALayer *placeHolderLayer = [CALayer layer];
        placeHolderLayer.frame = *(CGRect*) &relativeImageFrame;

        CGFloat fillComponents[4] = {1.0, 1.0, 1.0, 0.3};
        CGFloat strokeComponents[4] = {1.0, 1.0, 1.0, 0.9};
        CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();

        // set a background color
        color = CGColorCreate(colorSpace, fillComponents);
        placeHolderLayer.backgroundColor = color;
        CFRelease(color);

        // set a stroke color
        color = CGColorCreate(colorSpace, strokeComponents);
        placeHolderLayer.borderColor = color;
        CFRelease(color);

        placeHolderLayer.borderWidth = 2.0;
        placeHolderLayer.cornerRadius = 10;
        CFRelease(colorSpace);

        [layer addSublayer:placeHolderLayer];

        return layer;
    }

    // foreground layer
    if (type == IKImageBrowserCellForegroundLayer)
    {
        // no foreground layer on place holders
        if ([self cellState] != IKImageStateReady)
        {
            return nil;
        }

        // create a foreground layer that will contain several childs layer
        CALayer *layer = [CALayer layer];
        layer.frame = CGRectMake(0, 0, frame.size.width, frame.size.height);

        NSRect imageContainerFrame = [self imageContainerFrame];
        NSRect relativeImageContainerFrame =
            NSMakeRect(imageContainerFrame.origin.x - frame.origin.x,
                       imageContainerFrame.origin.y - frame.origin.y,
                       imageContainerFrame.size.width,
                       imageContainerFrame.size.height);

        // add a glossy overlay
        CALayer *glossyLayer = [CALayer layer];
        glossyLayer.frame = *(CGRect *) &relativeImageContainerFrame;
        setBundleImageOnLayer(glossyLayer, CFSTR("glossy.png"));
        [layer addSublayer:glossyLayer];

        // add a pin icon
        CALayer *pinLayer = [CALayer layer];
        setBundleImageOnLayer(pinLayer, CFSTR("pin.tiff"));
        pinLayer.frame = CGRectMake((frame.size.width/2)-5, frame.size.height - 17, 24, 30);
        [layer addSublayer:pinLayer];

        return layer;
    }

    // selection layer
    if (type == IKImageBrowserCellSelectionLayer)
    {
        // create a selection layer
        CALayer *selectionLayer = [CALayer layer];
        selectionLayer.frame = CGRectMake(0, 0, frame.size.width, frame.size.height);

        CGFloat fillComponents[4] = {1.0, 0, 0.5, 0.3};
        CGFloat strokeComponents[4] = {1.0, 0.0, 0.5, 1.0};

        // set a background color
        CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
        color = CGColorCreate(colorSpace, fillComponents);
        selectionLayer.backgroundColor = color;
        CFRelease(color);

        // set a border color
        color = CGColorCreate(colorSpace, strokeComponents);
        CFRelease(colorSpace);
        selectionLayer.borderColor = color;
        CFRelease(color);

        selectionLayer.borderWidth = 2.0;
        selectionLayer.cornerRadius = 5;

        return selectionLayer;
    }

    // Background layer.
    if (type == IKImageBrowserCellBackgroundLayer)
    {
        // No background layer on place holders.
        if ([self cellState] != IKImageStateReady)
        {
            return nil;
        }

        CALayer *layer = [CALayer layer];
        layer.frame = CGRectMake(0, 0, frame.size.width, frame.size.height);

        NSRect backgroundRect = NSMakeRect(0, 0, frame.size.width, frame.size.height);      

        CALayer *photoBackgroundLayer = [CALayer layer];
        photoBackgroundLayer.frame = *(CGRect*) &backgroundRect;

        CGFloat fillComponents[4] = {0.95, 0.95, 0.95, 1.0};
        CGFloat strokeComponents[4] = {0.2, 0.2, 0.2, 0.5};

        CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();

        color = CGColorCreate(colorSpace, fillComponents);
        photoBackgroundLayer.backgroundColor = color;
        CFRelease(color);

        color = CGColorCreate(colorSpace, strokeComponents);
        photoBackgroundLayer.borderColor = color;
        CFRelease(color);

        photoBackgroundLayer.borderWidth = 1.0;
        photoBackgroundLayer.shadowOpacity = 0.5;
        photoBackgroundLayer.cornerRadius = 3;

        CFRelease(colorSpace);

        [layer addSublayer:photoBackgroundLayer];

        return layer;
    }

    return nil;
}

//---------------------------------------------------------------------------------
// imageFrame
//
// Define where the image should be drawn.
//---------------------------------------------------------------------------------
- (NSRect)imageFrame
{
    // Get default imageFrame and aspect ratio.
    NSRect imageFrame = [super imageFrame];

    if (imageFrame.size.height == 0 || imageFrame.size.width == 0)
    {
        return NSZeroRect;
    }

    float aspectRatio =  imageFrame.size.width / imageFrame.size.height;

    // Compute the rectangle included in container with a margin of at least 10 pixel at the bottom,
    // 5 pixel at the top and keep a correct  aspect ratio.
    NSRect container = [self imageContainerFrame];
    container = NSInsetRect(container, 8, 8);

    if (container.size.height <= 0)
    {
        return NSZeroRect;
    }

    float containerAspectRatio = container.size.width / container.size.height;

    if (containerAspectRatio > aspectRatio){
        imageFrame.size.height = container.size.height;
        imageFrame.origin.y = container.origin.y;
        imageFrame.size.width = imageFrame.size.height * aspectRatio;
        imageFrame.origin.x = container.origin.x + (container.size.width - imageFrame.size.width)*0.5;
    }
    else
    {
        imageFrame.size.width = container.size.width;
        imageFrame.origin.x = container.origin.x;       
        imageFrame.size.height = imageFrame.size.width / aspectRatio;
        imageFrame.origin.y = container.origin.y + container.size.height - imageFrame.size.height;
    }

    // Round it.
    imageFrame.origin.x = floorf(imageFrame.origin.x);
    imageFrame.origin.y = floorf(imageFrame.origin.y);
    imageFrame.size.width = ceilf(imageFrame.size.width);
    imageFrame.size.height = ceilf(imageFrame.size.height);

    return imageFrame;
}

//---------------------------------------------------------------------------------
// imageContainerFrame
//
// Override the default image container frame.
//---------------------------------------------------------------------------------
- (NSRect)imageContainerFrame
{
    NSRect container = super.frame;

    // Make the image container 15 pixels up.
    container.origin.y += 15;
    container.size.height -= 15;

    return container;
}

//---------------------------------------------------------------------------------
// titleFrame
//
// Override the default frame for the title.
//---------------------------------------------------------------------------------
- (NSRect)titleFrame
{
    // Get the default frame for the title.
    NSRect titleFrame = [super titleFrame];

    // Move the title inside the 'photo' background image.
    NSRect container = [self frame];
    titleFrame.origin.y = container.origin.y + 3;

    // Make sure the title has a 7px margin with the left/right borders.
    float margin = titleFrame.origin.x - (container.origin.x + 7);
    if (margin < 0)
    {
        titleFrame = NSInsetRect(titleFrame, -margin, 0);
    }

    return titleFrame;
}

//---------------------------------------------------------------------------------
// selectionFrame
//
// Make the selection frame a little bit larger than the default one.
//---------------------------------------------------------------------------------
- (NSRect)selectionFrame
{
    return NSInsetRect([self frame], -5, -5);
}

@end
```

[Next](ImageBrowserAppearance-ImageBrowserController.m.md)[Previous](ImageBrowserAppearance-ImageBrowserBackgroundLayer.m.md)

