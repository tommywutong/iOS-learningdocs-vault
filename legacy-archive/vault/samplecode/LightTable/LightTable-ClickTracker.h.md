---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_ClickTracker_h.html
archived_at: '2026-07-18T03:13:30.519764Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTMaskLayer.h.md)[Previous](LightTable-DualTouchTracker.m.md)

# LightTable/ClickTracker.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The Click Tracker informs the view of single and double clicks. A single click is defined as a mouse down with a clickCount less than or equal to 1. A double click is a mouse up with a clickCount equal to 2. Tip: A view can easily change its behavior in response to a click by changing the action property. The owning view must route mouseDown: and mouseUp: responder messages to this tracker. 
*/

#import "InputTracker.h"


@interface ClickTracker : InputTracker {
    SEL _action;
    SEL _doubleAction;

    NSPoint _location;
    NSUInteger _modifiers;
}

// The method to call on the view in response to a click.
@property SEL action;

// The method to call on the view in response to a double click. The method should have one paramenter (ClickTracker *) and a void return.
@property SEL doubleAction;

// The location of the cursor in the view's coordinate space during a click action.
@property NSPoint location;

// The modifier flags of the last event processed by the tracker. The returned value outside of the scope of the action or doubleAction callbacks is undefined.
@property NSUInteger modifiers;

@end
```

[Next](LightTable-LTMaskLayer.h.md)[Previous](LightTable-DualTouchTracker.m.md)

