---
title: 'ImageBrowserViewAppearance: Customizing IKImageBrowserView'
apple_id: DTS40009013
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/ImageBrowserViewAppearance/Listings/ImageBrowserAppearance_ImageBrowserView_m.html
archived_at: '2026-07-18T03:12:23.576442Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImageBrowserViewAppearance: Customizing IKImageBrowserView](ImageBrowserViewAppearance-%20Customizing%20IKImageBrowserView.md)


[Next](ImageBrowserAppearance-ImageBrowserBackgroundLayer.m.md)[Previous](ImageBrowserAppearance-ImageBrowserView.h.md)

# ImageBrowserAppearance/ImageBrowserView.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 IKImageBrowserView subclass used to override newCellForRepresentedItem.
 */

#import "ImageBrowserView.h"
#import "ImageBrowserCell.h"

@interface ImageBrowserView ()

@property NSRect lastVisibleRect;

@end


#pragma mark -

@implementation ImageBrowserView

//---------------------------------------------------------------------------------
// newCellForRepresentedItem:
//
// Allocate and return our own cell class for the specified item. The returned cell must not be autoreleased.
//---------------------------------------------------------------------------------
- (IKImageBrowserCell *)newCellForRepresentedItem:(id)cell
{
    return [[ImageBrowserCell alloc] init];
}

//---------------------------------------------------------------------------------
// drawRect:
//
// Override draw rect and force the background layer to redraw if the view did resize or did scroll.
//---------------------------------------------------------------------------------
- (void)drawRect:(NSRect)rect
{
    // retrieve the visible area
    NSRect visibleRect = self.visibleRect;

    // compare with the visible rect at the previous frame
    if (!NSEqualRects(visibleRect, self.lastVisibleRect))
    {
        // we did scroll or resize, redraw the background
        [[self backgroundLayer] setNeedsDisplay];

        // update last visible rect
        _lastVisibleRect = visibleRect;
    }

    [super drawRect:rect];
}

@end
```

[Next](ImageBrowserAppearance-ImageBrowserBackgroundLayer.m.md)[Previous](ImageBrowserAppearance-ImageBrowserView.h.md)

