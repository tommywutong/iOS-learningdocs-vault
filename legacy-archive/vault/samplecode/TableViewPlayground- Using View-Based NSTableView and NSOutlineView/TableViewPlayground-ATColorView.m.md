---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATColorView_m.html
archived_at: '2026-07-18T03:26:13.321459Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATComplexOutlineController.h.md)[Previous](TableViewPlayground-ATTableCellView.h.md)

# TableViewPlayground/ATColorView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic NSView subclass that supports having an animatable background color (NOTE: the animation only works when the view is layer backed).
 */

#import "ATColorView.h"

@import Quartz; // for CABasicAnimation

@implementation ATColorView

+ (id)defaultAnimationForKey:(NSString *)key {
    if ([key isEqualToString:@"backgroundColor"]) {
        return [CABasicAnimation animation];
    }
    return [super defaultAnimationForKey:key];
}

- (void)setBackgroundColor:(NSColor *)value {
    if (_backgroundColor != value) {
        _backgroundColor = value;
        self.layer.backgroundColor = _backgroundColor.CGColor;
        [self setNeedsDisplay:YES];
    }
}

- (void)drawRect:(NSRect)r {
    NSColor *color = self.backgroundColor;
    if (color) {
        [color set];
        NSRectFill(r);
    }
    if (self.drawBorder) {
        [[NSColor lightGrayColor] set];
        NSFrameRectWithWidth(self.bounds, 1.0);
    }
    if (self.window.firstResponder == self) {
        NSSetFocusRingStyle(NSFocusRingOnly);
        NSRectFill(self.bounds);
    }
}

+ (Class)cellClass {
    // The cell is a container for the target/action
    return [NSActionCell class];
}

@end
```

[Next](TableViewPlayground-ATComplexOutlineController.h.md)[Previous](TableViewPlayground-ATTableCellView.h.md)

