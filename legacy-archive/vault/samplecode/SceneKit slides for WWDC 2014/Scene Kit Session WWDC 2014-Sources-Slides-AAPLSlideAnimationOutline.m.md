---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideAnimationOutline_m.html
archived_at: '2026-07-18T03:23:15.050333Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideActions.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideLight.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideAnimationOutline.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The different ways to manipulate objects.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideAnimationOutline : AAPLSlide
@end

@implementation AAPLSlideAnimationOutline

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"Animating a Scene";
    self.textManager.subtitle = @"Outline";

    [self.textManager addBullet:@"Per-frame updates" atLevel:0];
    [self.textManager addBullet:@"Animations" atLevel:0];
    [self.textManager addBullet:@"Actions" atLevel:0];
    [self.textManager addBullet:@"Physics" atLevel:0];
    [self.textManager addBullet:@"Constraints" atLevel:0];
    [self.textManager addBullet:@"Morphing" atLevel:0];
    [self.textManager addBullet:@"Skinning" atLevel:0];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideActions.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideLight.m.md)

