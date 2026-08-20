---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_DualTouchTracker_h.html
archived_at: '2026-07-18T03:13:30.775173Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-InputTracker.m.md)[Previous](LightTable-main.m.md)

# LightTable/DualTouchTracker.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The Dual Touch Tracker tracks the changes of two touches on a multi-touch trackpad. Tracking starts when the movement of two concurrent touches exceeds a threshold value. Tracking ends when either a third touch begins, or one of the touches are released, or touches are cancelled. The owning view must route touchesBeganWithEvent:, touchesMovedWithEvent:, touchesEndedWithEvent: and touchesCancelledWithEvent: responder messages to this tracker. 
*/

#import "InputTracker.h"

@interface DualTouchTracker : InputTracker {
@private
    BOOL _tracking;
    NSPoint _initialPoint;
    NSUInteger _modifiers;
    CGFloat _threshold;

    NSTouch *_initialTouches[2];
    NSTouch *_currentTouches[2];

    SEL _beginTrackingAction;
    SEL _updateTrackingAction;
    SEL _endTrackingAction;

    id _userInfo;
}

// The amount of dual touch movement before tracking begins. This value is in points (72ppi). Defaults to 1.
@property CGFloat threshold;

// The location of the cursor in the view's coordinate space when the second touch began.
@property(readonly) NSPoint initialPoint;

// The modifier flags of the last event processed by the tracker. The returned value outside of the begin and end tracking actions are undefined.
@property(readonly) NSUInteger modifiers;

// The two tracked touches are considered the bounds of a rectangle. THe following methods allow you to get the change in origin or size from the inital tracking values to the current values of said rectangle. The values are in points (72ppi)
@property(readonly) NSPoint deltaOrigin;
@property(readonly) NSSize deltaSize;

// The following three properties hold the tracking callbacks on the view. Each method should have one paramenter (DragTracker *) and a void return.
@property SEL beginTrackingAction;
@property SEL updateTrackingAction;
@property SEL endTrackingAction;

// Storage for your custom object to help with tracking. For example, a pointer to the object being modified may be set as the userInfo when the beginTrackingAction method is called. 
@property(strong) id userInfo;
@end
```

[Next](LightTable-InputTracker.m.md)[Previous](LightTable-main.m.md)

