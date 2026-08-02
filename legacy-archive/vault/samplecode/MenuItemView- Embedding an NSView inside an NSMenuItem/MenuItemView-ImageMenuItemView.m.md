---
title: 'MenuItemView: Embedding an NSView inside an NSMenuItem'
apple_id: DTS10004136
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MenuItemView/Listings/MenuItemView_ImageMenuItemView_m.html
archived_at: '2026-07-18T03:14:34.428617Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuItemView: Embedding an NSView inside an NSMenuItem](MenuItemView-%20Embedding%20an%20NSView%20inside%20an%20NSMenuItem.md)


[Next](MenuItemView-SliderView.h.md)[Previous](MenuItemView-TrackView.m.md)

# MenuItemView/ImageMenuItemView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The NSView that draws a picture as its background, used for menu item views that want a background image.
 */

#import "ImageMenuItemView.h"

@interface ImageMenuItemView ()

@property (strong) NSImage *myImage;

@end

#pragma mark -

@implementation ImageMenuItemView

// -------------------------------------------------------------------------------
//  awakeFromNib:
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    [super awakeFromNib];
    [self setupBackgroundImage];
}

// -------------------------------------------------------------------------------
//  setupBackgroundImage:
//
//  Setup the picture background for this view.
// -------------------------------------------------------------------------------
- (void)setupBackgroundImage
{
    // load the image to draw in the view's background, if not already allocated
    if (self.myImage == nil)
    {
        _myImage = [NSImage imageNamed:@"LakeDonPedro"];
    }
}

// -------------------------------------------------------------------------------
//  drawRect:rect
// -------------------------------------------------------------------------------
- (void)drawRect:(NSRect)rect
{   
    // draw the image for this view's background
    [self.myImage drawInRect:NSMakeRect(self.bounds.origin.x, self.bounds.origin.y, self.frame.size.width, self.frame.size.height)
                    fromRect:NSMakeRect(0, 0, self.myImage.size.width, self.myImage.size.height)
                   operation:NSCompositingOperationCopy
                    fraction:1.0];
}

@end
```

[Next](MenuItemView-SliderView.h.md)[Previous](MenuItemView-TrackView.m.md)

