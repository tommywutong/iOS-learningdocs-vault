---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_AAPLView_m.html
archived_at: '2026-07-18T03:23:14.700455Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlideTextManager.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-GLUtils.h.md)

# Scene Kit Session WWDC 2014/Sources/AAPLView.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 AAPLView is a subclass of SCNView. The only thing it does is to force a resolution
 */

#import "AAPLView.h"

@implementation AAPLView

#if FORCE_RESOLUTION
- (NSRect) bounds
{
    CGFloat backingScaleFactor = [[self window] backingScaleFactor];
    if(backingScaleFactor == 0) backingScaleFactor = 1;

    return NSMakeRect(0, 0, floor(RESOLUTION_X / backingScaleFactor), floor(RESOLUTION_Y / backingScaleFactor));
}
#endif

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-AAPLSlideTextManager.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-GLUtils.h.md)

