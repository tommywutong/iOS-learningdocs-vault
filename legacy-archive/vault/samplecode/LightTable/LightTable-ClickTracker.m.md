---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_ClickTracker_m.html
archived_at: '2026-07-18T03:13:30.573870Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-InputTrackers.h.md)[Previous](LightTable-MyDocument.m.md)

# LightTable/ClickTracker.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The Click Tracker informs the view of single and double clicks. A single click is defined as a mouse down with a clickCount less than or equal to 1. A double click is a mouse up with a clickCount equal to 2. Tip: A view can easily change its behavior in response to a click by changing the action property. The owning view must route mouseDown: and mouseUp: responder messages to this tracker.
 */

#import "ClickTracker.h"


@implementation ClickTracker
@synthesize action = _action;
@synthesize doubleAction = _doubleAction;
@synthesize location = _location;
@synthesize modifiers = _modifiers;

- (void)mouseDown:(NSEvent *)event {
    self.location = event.locationInWindow; // [self.view convertPoint:event.locationInWindow fromView:nil]; // [self.view convertPointFromBase:[event locationInWindow]];
    if (event.clickCount <= 1) {
        self.modifiers = event.modifierFlags;
        if (self.isEnabled && self.action) {
            [NSApp sendAction:self.action to:self.view from:self];
        }
    }
}

- (void)mouseUp:(NSEvent *)event {
    if (event.clickCount == 2) {
        self.modifiers = event.modifierFlags;
        if(self.isEnabled && self.doubleAction) {
            [NSApp sendAction:self.doubleAction to:self.view from:self];
        }
    }
}
@end
```

[Next](LightTable-InputTrackers.h.md)[Previous](LightTable-MyDocument.m.md)

