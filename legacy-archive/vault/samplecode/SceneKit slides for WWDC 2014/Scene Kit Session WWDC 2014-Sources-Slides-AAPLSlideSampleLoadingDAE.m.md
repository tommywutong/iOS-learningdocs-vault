---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Sources_Slides_AAPLSlideSampleLoadingDAE_m.html
archived_at: '2026-07-18T03:23:18.324716Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter3.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideMaterialLayer.m.md)

# Scene Kit Session WWDC 2014/Sources/Slides/AAPLSlideSampleLoadingDAE.m

```objc
/*
 Copyright (C) 2014-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shows how to load a scene from a dae file.
 */

#import "AAPLPresentationViewController.h"
#import "AAPLSlideTextManager.h"
#import "AAPLSlide.h"
#import "Utils.h"

@interface AAPLSlideSampleLoadingDae : AAPLSlide
@end

@implementation AAPLSlideSampleLoadingDae

- (void)setupSlideWithPresentationViewController:(AAPLPresentationViewController *)presentationViewController {
    self.textManager.title = @"Loading a DAE";
    self.textManager.subtitle = @"Sample code";

    [self.textManager addCode:
     @"// Load a DAE \n"
     @"SCNScene *scene = [SCNScene #sceneNamed:#@\"dungeon.dae\"];"];

    SCNNode *image = [SCNNode asc_planeNodeWithImageNamed:@"daeAsResource" size:9 isLit:NO];
    image.position = SCNVector3Make(0, 3.2, 7);
    [self.groundNode addChildNode:image];
}

@end
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideChapter3.m.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Sources-Slides-AAPLSlideMaterialLayer.m.md)

