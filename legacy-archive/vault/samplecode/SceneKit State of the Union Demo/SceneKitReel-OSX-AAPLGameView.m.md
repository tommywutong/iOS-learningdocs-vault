---
title: SceneKit State of the Union Demo
apple_id: TP40014550
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: SceneKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitReel/Listings/SceneKitReel_OSX_AAPLGameView_m.html
archived_at: '2026-07-18T03:23:12.308291Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit State of the Union Demo](SceneKit%20State%20of%20the%20Union%20Demo.md)


[Next](SceneKitReel-OSX-AAPLGameView.h.md)[Previous](SceneKitReel-OSX-AAPLAppDelegate.m.md)

# SceneKitReel-OSX/AAPLGameView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Game view declaration.
 */

#import "AAPLGameView.h"

@implementation AAPLGameView {
    IBOutlet AAPLGameViewController *_gameViewController;
    NSPoint _clickLocation;
}

// forward click event to the game view controller
- (void)mouseDown:(NSEvent *)theEvent
{
    _clickLocation = [self convertPoint:theEvent.locationInWindow fromView:nil];

    [_gameViewController gestureDidBegin];

    if (theEvent.clickCount == 2) {
        [_gameViewController handleDoubleTapAtPoint:_clickLocation];
    }
    else {
        if (!(theEvent.modifierFlags & NSAlternateKeyMask)) {
            [_gameViewController handleTapAtPoint:_clickLocation];
        }
    }

    [super mouseDown:theEvent];
}

// forward drag event to the view controller as "pan" events
- (void)mouseDragged:(NSEvent *)theEvent
{
    if (theEvent.modifierFlags & NSAlternateKeyMask) {
        NSPoint p = [self convertPoint:theEvent.locationInWindow fromView:nil];
        [_gameViewController tiltCameraWithOffset:CGPointMake(p.x - _clickLocation.x, p.y - _clickLocation.y)];
    }
    else {
        [_gameViewController handlePanAtPoint:[self convertPoint:theEvent.locationInWindow fromView:nil]];
    }

    [super mouseDragged:theEvent];
}

// forward mouse up events as "end gesture"
- (void)mouseUp:(NSEvent *)theEvent
{
    [_gameViewController gestureDidEnd];
    [super mouseUp:theEvent];
}

@end
```

[Next](SceneKitReel-OSX-AAPLGameView.h.md)[Previous](SceneKitReel-OSX-AAPLAppDelegate.m.md)

