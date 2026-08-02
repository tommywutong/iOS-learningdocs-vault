---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideEnd_m.html
archived_at: '2026-07-18T03:23:16.391423Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideMaterialProperties.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideShadows.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideEnd.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Last slide.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideEnd : AAPLSlide
@end

@implementation AAPLSlideEnd

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    SCNNode *imageNode = [SCNNode asc_planeNodeWithImageNamed:@"wwdc.png" size:19 isLit:NO];
    imageNode.position = SCNVector3Make(0, 30, 0);
    imageNode.castsShadow = NO;
    [self.contentNode addChildNode:imageNode];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideMaterialProperties.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideShadows.m.md)

