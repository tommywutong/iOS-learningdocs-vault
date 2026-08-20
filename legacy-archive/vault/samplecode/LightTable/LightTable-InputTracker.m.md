---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_InputTracker_m.html
archived_at: '2026-07-18T03:13:30.938550Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-AppDelegate.m.md)[Previous](LightTable-DualTouchTracker.h.md)

# LightTable/InputTracker.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Input Trackers are a technique to factor the various input tracking needs of a view without using tracking loops or complicated internal variables. A view creates an array of all the trackers it needs and routes all of the appropriate NSResponderMethods to the Input Tracker array. The tracker will then call back the view with the methods set supplied by the view when something interesting happens. For some trackers, this may be as simple as click or double click. For other trackers this may be a set of begin/update/end methods. Typically, in the begin callback implementation, the view will disable all of its trackers except for the one that issued the callback. Then, upon the end callback, the view will enable all of its trackers again. This way, other input will be ignored until this tracker has completed.
 */

#import "InputTracker.h"


@implementation InputTracker

- (instancetype)init {
    if(self = [super init]) {
        self.isEnabled = YES;
    }
    return self;
}

#pragma mark API

@synthesize view = _view;
@synthesize isEnabled = _enabled;

- (void)setIsEnabled:(BOOL)enabled {
    if (_enabled && !enabled)  {
        [self cancelTracking];
    }
    _enabled = enabled;
}

- (BOOL)isEnabled {
    return _enabled;
}

- (void)cancelTracking {
}
@end
```

[Next](LightTable-AppDelegate.m.md)[Previous](LightTable-DualTouchTracker.h.md)

