---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_DualTouchTracker_m.html
archived_at: '2026-07-18T03:13:30.821323Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-ClickTracker.h.md)[Previous](LightTable-LTView.m.md)

# LightTable/DualTouchTracker.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The Dual Touch Tracker tracks the changes of two touches on a multi-touch trackpad. Tracking starts when the movement of two concurrent touches exceeds a threshold value. Tracking ends when either a third touch begins, or one of the touches are released, or touches are cancelled. The owning view must route touchesBeganWithEvent:, touchesMovedWithEvent:, touchesEndedWithEvent: and touchesCancelledWithEvent: responder messages to this tracker.
 */

#import "DualTouchTracker.h"

@interface DualTouchTracker()

@property BOOL isTracking;
@property(readwrite) NSPoint initialPoint;
@property(readwrite) NSUInteger modifiers;

- (void)releaseTouches;

@end


@implementation DualTouchTracker

- (instancetype)init {
    if (self = [super init]) {
        self.threshold = 1;
    }

    return self;
}

- (void)dealloc {
    [self releaseTouches];
}

#pragma mark NSResponder

- (void)touchesBeganWithEvent:(NSEvent *)event {
    if (!self.isEnabled) return;

    NSSet *touches = [event touchesMatchingPhase:NSTouchPhaseTouching inView:self.view];

    if (touches.count == 2) {
        self.initialPoint = [self.view convertPoint:event.locationInWindow fromView:nil]; 
        NSArray *array = touches.allObjects;
        _initialTouches[0] = array[0];
        _initialTouches[1] = array[1];

        _currentTouches[0] = _initialTouches[0];
        _currentTouches[1] = _initialTouches[1];
    } else if (touches.count > 2) {
        // More than 2 touches. Only track 2.
        if (self.isTracking) {
            [self cancelTracking];
        } else {
            [self releaseTouches];
        }

    }
}

- (void)touchesMovedWithEvent:(NSEvent *)event {
    if (!self.isEnabled) return;

    self.modifiers = event.modifierFlags;
    NSSet *touches = [event touchesMatchingPhase:NSTouchPhaseTouching inView:self.view];

    if (touches.count == 2 && _initialTouches[0]) {
        NSArray *array = touches.allObjects;

        NSTouch *touch;
        touch = array[0];
        if ([touch.identity isEqual:_initialTouches[0].identity]) {
            _currentTouches[0] = touch;
        } else {
            _currentTouches[1] = touch;
        }

        touch = array[1];
        if ([touch.identity isEqual:_initialTouches[0].identity]) {
            _currentTouches[0] = touch;
        } else {
            _currentTouches[1] = touch;
        }

        if (!self.isTracking) {
            NSPoint deltaOrigin = self.deltaOrigin;
            NSSize  deltaSize = self.deltaSize;

            if (fabs(deltaOrigin.x) > _threshold || fabs(deltaOrigin.y) > _threshold || fabs(deltaSize.width) > _threshold || fabs(deltaSize.height) > _threshold) {
                self.isTracking = YES;
                if (self.beginTrackingAction) [NSApp sendAction:self.beginTrackingAction to:self.view from:self];
            }
        } else {
            if (self.updateTrackingAction) [NSApp sendAction:self.updateTrackingAction to:self.view from:self];
        }
    }
}

- (void)touchesEndedWithEvent:(NSEvent *)event {
    if (!self.isEnabled) return;

    self.modifiers = event.modifierFlags;
    [self cancelTracking];
}

- (void)touchesCancelledWithEvent:(NSEvent *)event {
    [self cancelTracking];
}

#pragma mark InputTracker


- (void)cancelTracking {
    if (self.isTracking) {
        if (self.endTrackingAction) [NSApp sendAction:self.endTrackingAction to:self.view from:self];
        self.isTracking = NO;
        [self releaseTouches];
    }
}

#pragma mark API

@synthesize userInfo = _userInfo;
@synthesize threshold = _threshold;
@synthesize isTracking = _tracking;
@synthesize initialPoint = _initialPoint;

@synthesize beginTrackingAction = _beginTrackingAction;
@synthesize updateTrackingAction = _updateTrackingAction;
@synthesize endTrackingAction = _endTrackingAction;

@synthesize modifiers = _modifiers;

- (NSPoint)deltaOrigin {
    if (!(_initialTouches[0] && _initialTouches[1] && _currentTouches[0] && _currentTouches[1])) return NSZeroPoint;

    CGFloat x1 = MIN(_initialTouches[0].normalizedPosition.x, _initialTouches[1].normalizedPosition.x);
    CGFloat x2 = MIN(_currentTouches[0].normalizedPosition.x, _currentTouches[1].normalizedPosition.x);
    CGFloat y1 = MIN(_initialTouches[0].normalizedPosition.y, _initialTouches[1].normalizedPosition.y);
    CGFloat y2 = MIN(_currentTouches[0].normalizedPosition.y, _currentTouches[1].normalizedPosition.y);

    NSSize deviceSize = _initialTouches[0].deviceSize;
    NSPoint delta;
    delta.x = (x2 - x1) * deviceSize.width;
    delta.y = (y2 - y1) * deviceSize.height;
    return delta;
}

- (NSSize)deltaSize {
    if (!(_initialTouches[0] && _initialTouches[1] && _currentTouches[0] && _currentTouches[1])) return NSZeroSize;

    CGFloat x1,x2,y1,y2,width1,width2,height1,height2;

    x1 = MIN(_initialTouches[0].normalizedPosition.x, _initialTouches[1].normalizedPosition.x);
    x2 = MAX(_initialTouches[0].normalizedPosition.x, _initialTouches[1].normalizedPosition.x);
    width1 = x2 - x1;

    y1 = MIN(_initialTouches[0].normalizedPosition.y, _initialTouches[1].normalizedPosition.y);
    y2 = MAX(_initialTouches[0].normalizedPosition.y, _initialTouches[1].normalizedPosition.y);
    height1 = y2 - y1;

    x1 = MIN(_currentTouches[0].normalizedPosition.x, _currentTouches[1].normalizedPosition.x);
    x2 = MAX(_currentTouches[0].normalizedPosition.x, _currentTouches[1].normalizedPosition.x);
    width2 = x2 - x1;

    y1 = MIN(_currentTouches[0].normalizedPosition.y, _currentTouches[1].normalizedPosition.y);
    y2 = MAX(_currentTouches[0].normalizedPosition.y, _currentTouches[1].normalizedPosition.y);
    height2 = y2 - y1;

    NSSize deviceSize = _initialTouches[0].deviceSize;
    NSSize delta;
    delta.width = (width2 - width1) * deviceSize.width;
    delta.height = (height2 - height1) * deviceSize.height;
    return delta;
}

- (void)releaseTouches {

    _initialTouches[0] = nil;
    _initialTouches[1] = nil;
    _currentTouches[0] = nil;
    _currentTouches[1] = nil;
}

@end
```

[Next](LightTable-ClickTracker.h.md)[Previous](LightTable-LTView.m.md)

