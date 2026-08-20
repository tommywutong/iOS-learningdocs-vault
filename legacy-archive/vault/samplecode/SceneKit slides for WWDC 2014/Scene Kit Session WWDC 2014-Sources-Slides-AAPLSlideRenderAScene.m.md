---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideRenderAScene_m.html
archived_at: '2026-07-18T03:23:18.216230Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideJavascript.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCloning.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideRenderAScene.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shows how to set a scene to a renderer.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideRenderAScene : AAPLSlide
@end

@implementation AAPLSlideRenderAScene

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"Displaying the Scene";

    [self.textManager addBullet:@"Assign the scene to the renderer" atLevel:0];
    [self.textManager addBullet:@"Modifications of the scene graph are automatically reflected" atLevel:0];

    [self.textManager addCode:
     @"// Assign the scene \n"
     @"aSCNView.#scene# = aScene;"];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideJavascript.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCloning.m.md)

