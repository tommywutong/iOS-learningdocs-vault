---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideReferTo2013_m.html
archived_at: '2026-07-18T03:23:18.177734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter2.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreateAScene2.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideReferTo2013.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Chapter 2 slide : Scene Graph
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideReferTo2013 : AAPLSlide
@end

@implementation AAPLSlideReferTo2013

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"Related Sessions";

    // load the "related.png" image and show it mapped on a plane
    SCNNode *relatedImage = [SCNNode asc_planeNodeWithImageNamed:@"related.png" size:35 isLit:NO];
    relatedImage.position = SCNVector3Make(0, 10, 0);
    relatedImage.castsShadow = NO;
    [self.groundNode addChildNode:relatedImage];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter2.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideCreateAScene2.m.md)

