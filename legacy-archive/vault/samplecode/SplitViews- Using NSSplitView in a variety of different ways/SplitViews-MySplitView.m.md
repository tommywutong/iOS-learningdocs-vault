---
title: 'SplitViews: Using NSSplitView in a variety of different ways'
apple_id: DTS40011336
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/SplitViews/Listings/SplitViews_MySplitView_m.html
archived_at: '2026-07-18T03:25:20.589609Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SplitViews: Using NSSplitView in a variety of different ways](SplitViews-%20Using%20NSSplitView%20in%20a%20variety%20of%20different%20ways.md)


[Next](SplitViews-ActivityView.h.md)[Previous](SplitViews-AppDelegate.m.md)

# SplitViews/MySplitView.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  Cust NSSplitView for drawing a custom divider. 
 */

#import "MySplitView.h"

@interface MySplitView ()

@property (strong) NSImage *image;

@end

#pragma mark -

@implementation MySplitView

// -------------------------------------------------------------------------------
//  awakeFromNib
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    _image = [NSImage imageNamed:@"HorizDividerHandle"];
}

// -------------------------------------------------------------------------------
//  dividerThickness
// -------------------------------------------------------------------------------
- (CGFloat)dividerThickness
{
    return 30.0;
}

// -------------------------------------------------------------------------------
//  drawDividerInRect:Rect
// -------------------------------------------------------------------------------
- (void)drawDividerInRect:(NSRect)rect
{
    NSRect targetRect = NSMakeRect(0, 0, rect.size.width, rect.size.height);
    targetRect.origin.y -= (rect.size.height - self.image.size.height) / 2;
    targetRect.origin.x -= (rect.size.width - self.image.size.width) / 2;

    [self lockFocus];
    [self.image drawInRect:rect fromRect:targetRect operation:NSCompositeSourceOver fraction:1.0];
    [self unlockFocus];
}

@end
```

[Next](SplitViews-ActivityView.h.md)[Previous](SplitViews-AppDelegate.m.md)

